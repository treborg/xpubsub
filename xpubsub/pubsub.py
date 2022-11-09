from enum import Enum, auto

# from icecream import ic


class Alerts(Enum):
    ADD = auto()
    ALL = auto()
    NEW = auto()
    REMOVE = auto()
    SEND = auto()


def fix(topic_list):
    if isinstance(topic_list, list):
        return topic_list
    return [topic_list]


class PubSub:
    def __init__(self):
        self.__topics = dict()

    def new_topic(self, topic):
        self.__topics[topic] = set()

    def remove_topic(self, topic):
        del self.__topics[topic]

    def get_topics(self):
        return set(self.__topics.keys())

    def subscribers(self, topic):
        topics = self.__topics
        if topic not in topics:
            self.new_topic(topic)
        return topics[topic]

    def add(self, topic_list, callback):
        for topic in fix(topic_list):
            subs = self.subscribers(topic)
            subs.add(callback)

    def remove(self, topic_list, callback):
        for topic in fix(topic_list):
            subs = self.subscribers(topic)
            subs.remove(callback)
            if not len(subs):
                self.remove_topic(topic)

    # TODO: alert if no subscribers?
    def send(self, topic_list, message):
        subs = self.subscribers
        for topic in fix(topic_list):
            self._send(topic, subs(topic), message)

    def _send(self, topic, subs, message):
        for cb in self.subscribers(topic):
            cb(topic, message)
            self._alert(Alerts.ALL, topic, message)

    def _alert(self, alert, topic, message):
        assert isinstance(alert, Alerts)
        for cb in self.subscribers(alert):
            cb(alert, topic, message)
