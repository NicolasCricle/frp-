from getpass import getuser

user = getuser()

class Const(object):
    CONF_PATH = "C:\\Users\\" + user + "\\AppData\\Local\\FRP"
    CONF_NAME = "conf.json"
