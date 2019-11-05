import gitlab
import subprocess
from git import Repo

import os
import sys
import time
path = os.path.dirname(__file__)
path = os.path.join(path, 'inits')


class Gitlab:

    def __init__(self):
        self.url = 'http://gitlab.kointernet.com'
        self.token = 'FJ9s8-rkSnUHzXavV-35'

    def login(self):
        gl = gitlab.Gitlab(self.url, self.token)
        projects = gl.projects.list(all=True)
        return projects

    def clone(self, name):
        projects = self.login()
        for pro in projects:
            if pro.name == name:
                # 获取代码仓库地址
                git_url = pro.http_url_to_repo
                # 拉取代码至指定路径
                Repo.clone_from(git_url, path)
                # 拉取代码
                # subprocess.call(['git', 'clone', git_url])


if __name__=="__main__":
    gl = Gitlab()
    # gl.login()
    gl.clone('tmp-auto')
