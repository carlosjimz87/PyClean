#!/usr/bin/env python
#
# Created by carlosjimz on 24/11/2018 11:14
#
##############################################################


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Publisher:
    def __init__(self, events):
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who):
        callback = who.update
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


def main():
    pub = Publisher(['lunch', 'dinner'])

    bob = Subscriber('Bob')
    john = Subscriber('Alice')
    alice = Subscriber('John')

    pub.register('lunch', bob)
    pub.register('dinner', alice)
    pub.register('lunch', john)
    pub.register('dinner', john)

    pub.dispatch('lunch', "LUNCH IS SERVED!!!")
    pub.unregister('lunch', john)
    print("************************")
    pub.dispatch('dinner', "DINNER IS READY!!!")


if __name__ == '__main__':
    main()
