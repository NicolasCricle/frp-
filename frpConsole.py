from sys import argv, exit

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui.wfl import Ui_mainWindow
from functions.frp import frpHandler
from work_function import AutoSearchFunc, FrpOnFunc, NginxFunc, SearchShowFunc
from functions.conf import confHandler
from functions.nginx_stream import nginxStream


class WFLMainWindow(Ui_mainWindow, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.frp = frpHandler
        self.confHandler = confHandler
        self.nginxStream = nginxStream

        self.autoSearchFunc = AutoSearchFunc(self.frp)
        self.autoSearchFunc.signal.connect(self.finish_auto_search)
        self.searchShowFunc = SearchShowFunc()
        self.searchShowFunc.signal.connect(self.search_show)

        self.frpOnFunc = FrpOnFunc(self.frp)
        self.frpOnFunc.signal.connect(self.run_frp_on)

        self.nginxFunc = NginxFunc(self.nginxStream)
        self.nginxFunc.signal.connect(self.run_nginx)
        # 主窗口关闭
        self.nginxFunc.windowSign.connect(self.nginx_off_event)

        self.init_conf_show()

    def init_conf_show(self):
        """
        读取conf配置文件 将其显示在各个控件
        :return:
        """
        conf = self.confHandler.conf
        self.dirNameEdit.setText(conf.get("frpDirPath", ""))
        self.serverIpEdit.setText(conf.get("serverIp", ""))
        self.serverUserEdit.setText(conf.get("serverUser", ""))
        self.serverPasswordEdit.setText(conf.get("serverPassword", ""))
        self.nginxStreamEdit.setText(conf.get("nginxStream", ""))


    def frp_on(self):
        frpDirPath = self.dirNameEdit.text()
        setattr(self.frp, "frpDirPath", frpDirPath)
        self.frpOnFunc.start()

    def frp_off(self):
        if self.frp.frpPopen is not None:
            self.frp.frpPopen.kill()
        self.outPrint.setText("frp 已经被关闭")

    def run_frp_on(self, s):
        self.outPrint.append(s)


    def auto_search(self):
        self.autoSearchFunc.start()
        self.searchShowFunc.start()

    def finish_auto_search(self, path):
        self.searchShowFunc.flag = False
        self.outPrint.append("当前搜索到frp所在目录为：{}".format(path))
        self.dirNameEdit.setText(path)

    def search_show(self, showStr):
        showStr = "自动搜索开始，请稍等" + showStr
        self.outPrint.setText(showStr)

    @property
    def nginx_params(self):
        serverIp = self.serverIpEdit.text()
        serverPassword = self.serverPasswordEdit.text()
        serverUser = self.serverUserEdit.text()
        stream = self.nginxStreamEdit.text()

        return {
            "host": serverIp,
            "user": serverUser,
            "password": serverPassword,
            "stream": stream
        }

    def nginx_on(self):
        self.nginxStream.init_params(**self.nginx_params)
        self.nginxStream.cmd = "y"
        self.nginxFunc.start()

    def nginx_off(self, mainWindowClose=None):
        if mainWindowClose:
            setattr(self.nginxFunc, "mainWindowClose", mainWindowClose)
        self.nginxStream.init_params(**self.nginx_params)
        self.nginxStream.cmd = "n"
        self.nginxFunc.start()

    def run_nginx(self, info):
        self.outPrint.append(info)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"您即将退出，nginx流将被关闭，frp即将被关闭，是否继续退出?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 退出之前 首先保存所有的conf的设置
            conf = {
                "frpDirPath": self.dirNameEdit.text(),
                "serverIp": self.serverIpEdit.text(),
                "serverPassword": self.serverPasswordEdit.text(),
                "serverUser": self.serverUserEdit.text(),
                "nginxStream": self.nginxStreamEdit.text()
            }
            self.confHandler.conf = conf

            # 同时关闭frp 以及 nginx流
            if conf.get("serverIp") and conf.get("serverPassword") and conf.get("serverUser") and conf.get("nginxStream"):
                self.frp_off()
                self.nginx_off(True)
                self.outPrint.setText(u"正在关闭frp 以及 nginx stream, 请稍等")
                event.ignore()
            else:
                event.accept()

        else:
            event.ignore()

    def nginx_off_event(self):
        self.outPrint.setText(u"frp 以及 nginx stream 均已经关闭，程序即将退出")
        QApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(argv)
    w = WFLMainWindow()
    w.show()
    exit(app.exec_())

