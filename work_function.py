from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal

class AutoSearchFunc(QThread):

    signal = pyqtSignal(str)

    def __init__(self, frp):
        super().__init__()
        self.frp = frp

    def run(self):
        frpDirPath = self.frp.get_dir()
        self.signal.emit(frpDirPath)


class SearchShowFunc(QThread):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        self.flag = True
        index = 1
        while self.flag:
            if index > 6:
                index = 1
            self.signal.emit("."*index)
            sleep(1)
            index += 1

    def stop(self):
        self.flag = False


class FrpOnFunc(QThread):

    signal = pyqtSignal(str)

    def __init__(self, frp):
        super().__init__()
        self.frp = frp

    def run(self):
        try:
            self.frp(self.frp.frpDirPath)
        except ValueError as e:
            self.signal.emit(str(e))
        else:
            while self.frp.frpPopen.poll() is None:
                sleep(0.3)
                self.signal.emit(self.frp.frpPopen.stdout.readline())


class NginxFunc(QThread):

    signal = pyqtSignal(str)
    windowSign = pyqtSignal()

    def __init__(self, nginx):
        super().__init__()
        self.nginx = nginx
        self.mainWindowClose = False

    def run(self):
        try:
            res = self.nginx.ssh_cmd()
        except Exception as e:
            if self.mainWindowClose:
                self.windowSign.emit()
            else:
                self.signal.emit(str(e))
        else:
            if self.mainWindowClose:
                self.windowSign.emit()
            else:
                self.signal.emit(res)





