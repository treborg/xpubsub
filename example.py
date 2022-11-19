from xpubsub import PubSub

pub = PubSub()


def hello(topic, message):
    print(topic, message)


def goodbye(topic, msg):
    print("😭", topic, msg)


pub.add("hi", hello)
pub.add(["SHTF!", "go away"], goodbye)

pub.send("hi", "👋😍")
pub.send("SHTF!", "Head For The Hills!")
pub.send("go away", "its over")

pub.remove("go away", goodbye)
pub.send("go away", "nothing happens")  # this does nothing!
