from common import request


class Pair(object):
    def __init__(self, name):
        self.name = name
        self.base, self.alternate = self.name.split("_")

    @property
    def lowest_ask(self):
        params = {"base" : self.base.upper(),
                "alt" : self.alternate.upper()}
        return request("lowest_ask", params)

    @property
    def highest_bid(self):
        params = {"base" : self.base.upper(),
                "alt" : self.alternate.upper()}
        return request("highest_bid", params)

    @property
    def last_trade(self):
        pass

    @property
    def volume(self):
        pass

    @property
    def info(self):
        pass

    @property
    def orderbook(self):
        pass

    def trades(self, since):
        pass

