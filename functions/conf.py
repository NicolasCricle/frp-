from os import mkdir
from os.path import exists, join
from json import load, dump
from constans import Const


class ConfHandler(object):

    def __init__(self):
        if not exists(Const.CONF_PATH):
            mkdir(Const.CONF_PATH)
            self.conf = dict()

    @property
    def path(self):
        return join(Const.CONF_PATH, Const.CONF_NAME)

    @property
    def conf(self):
        with open(self.path, "r") as conf:
            confDict = load(conf)
        return confDict

    @conf.setter
    def conf(self, value):
        with open(self.path, "w") as conf:
            dump(value, conf)


confHandler = ConfHandler()
