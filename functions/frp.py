from string import ascii_uppercase
from os.path import isdir, exists
from os import walk, chdir
from subprocess import Popen, PIPE


class FrpHandler(object):

    def __init__(self):
        self.frpPopen = None

    @staticmethod
    def get_disk():
        diskList = []
        for char in ascii_uppercase:
            diskName = "{}:\\".format(char)
            if isdir(diskName):
                diskList.append(diskName)

        return diskList

    @staticmethod
    def get_dir():
        diskNameList = FrpHandler.get_disk()
        for diskName in diskNameList:
            for dirPath, dirName, fileName in walk(diskName):
                if "frp" in dirPath and "frpc.ini" in fileName and "frpc.exe" in fileName:
                    return dirPath
        else:
            return ""

    @staticmethod
    def start_frp(frpDir):
        chdir(frpDir)
        frpPopen = Popen("frpc.exe -c frpc.ini", universal_newlines=True, stdout=PIPE, stderr=PIPE)
        return frpPopen

    def __call__(self, frpDirPath):
        if not frpDirPath or not exists(frpDirPath):
            raise ValueError("未找到相应的frp文件夹信息，请手动添加或者自动搜索")
        self.frpPopen = self.start_frp(frpDirPath)


frpHandler = FrpHandler()






