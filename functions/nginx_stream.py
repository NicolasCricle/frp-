# coding=utf-8
from socket import timeout as toe
from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException, NoValidConnectionsError


class NginxStreamHandler(object):

    def __init__(self, host=None, user=None, password=None, stream=None, port=22, timeout=5):
        super().__init__()
        self.host = host
        self.user = user
        self.password = password
        self.stream = stream
        self.port = port
        self.timeout = timeout
        self._cmd = "y"
        self.mainWindowClose = False

    def ssh_cmd(self):
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())

        try:
            ssh.connect(self.host, self.port, self.user, self.password, timeout=self.timeout)
        except AuthenticationException as e:
            outList = ["ssh服务器身份验证错误，请检查核对您的用户名以及密码", str(e)]
        except NoValidConnectionsError as e:
            outList = ["ssh服务器连接错误", str(e)]
        except toe:
            outList = ["ssh服务器连接超时，请重新试试"]
        else:
            sshCmdStr = "python /etc/nginx/fprNginx.py {} {}".format(self.stream, self.cmd)
            _, out, __ = ssh.exec_command(sshCmdStr)
            outList = out.readlines()
            for item in outList:
                if "upstream name do not exists" == item.strip():
                    break
            else:
                outList.append("成功！")
        finally:
            ssh.close()

        return "".join(outList)

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        if value not in ("y", "n"):
            raise ValueError("cmd 只能设置 y/n")
        self._cmd = value

    def init_params(self, host, user, password, stream, port=22, timeout=5):
        self.host = host
        self.user = user
        self.password = password
        self.stream = stream
        self.port = port
        self.timeout = timeout


nginxStream = NginxStreamHandler()
