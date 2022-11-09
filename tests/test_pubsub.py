from xpubsub import PubSub, Alerts

# from icecream import ic


def test_topics_list():
    pub = PubSub()
    topics = pub.get_topics

    assert len(topics()) == 0
    pub.add("hello", "hi")
    assert topics() == {"hello"}

    subs = pub.subscribers
    assert subs("hello") == {"hi"}


def setup_single():
    pub = PubSub()

    # Add only single topics
    pub.add("goodbye", "by")
    pub.add("hello", "hi")
    pub.add("goodbye", "world")

    return pub


def test_add_single():

    pub = setup_single()
    subs = pub.subscribers

    topics = pub.get_topics()
    assert topics == {"hello", "goodbye"}

    assert subs("hello") == {"hi"}
    assert subs("goodbye") == {"by", "world"}


def test_remove_single():
    pub = setup_single()
    subs = pub.subscribers

    pub.remove("hello", "hi")
    assert pub.get_topics() == {"goodbye"}

    pub.remove("goodbye", "by")
    assert subs("goodbye") == {"world"}


def test_add_many():
    pub = PubSub()
    subs = pub.subscribers

    pub.add(["hello", "goodbye"], "world")
    pub.add("goodbye", "hi")

    assert subs("hello") == {"world"}
    assert subs("goodbye") == {"world", "hi"}


def test_remove_many():
    pub = PubSub()
    subs = pub.subscribers

    pub.add(["hello", "goodbye"], "world")
    pub.add(["great", "hello", "goodbye"], "buddy")
    pub.add("goodbye", "hi")

    assert subs("hello") == {"world", "buddy"}
    assert subs("great") == {"buddy"}
    assert subs("goodbye") == {"world", "buddy", "hi"}

    pub.remove(["great", "goodbye", "hello"], "buddy")

    assert subs("hello") == {"world"}
    assert subs("goodbye") == {"world", "hi"}
    assert "great" not in pub.get_topics()


def test_message():
    def callback1(topic, message):
        assert topic == "hello"
        assert message == "hi!"

    def callback2(topic, message):
        assert topic == "goodbye"
        assert message == "cu soon"

    pub = PubSub()

    pub.add("hello", callback1)
    pub.add("goodbye", callback2)

    pub.send("hello", "hi!")
    pub.send("goodbye", "cu soon")


def test_alert_all():
    xgood = False
    xalert = False

    def cbAlertAll(alert, topic, message):
        nonlocal xalert
        xalert = True

        assert alert == Alerts.ALL
        assert topic == "good"
        assert message == "morning"

    def cb(topic, message):
        nonlocal xgood
        xgood = True

        assert topic == "good"
        assert message == "morning"

    pub = PubSub()
    pub.add("good", cb)
    pub.add(Alerts.ALL, cbAlertAll)
    pub.send("good", "morning")
    assert xgood
    assert xalert
