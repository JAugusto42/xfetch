#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import platform
import getpass
import socket
import os


class Main:
    def __init__(self):
        architecture = platform.machine()
        system = platform.uname()[1].title()
        user = getpass.getuser()
        hostname = socket.gethostname()
        kernel = platform.uname()[2]

        self.show_info(system, user, hostname, architecture, kernel)

    @staticmethod
    def show_info(system, user, hostname, architecture, kernel):
        infos = """
             {username}@{hostname}
           -----------------------
    OS          : {sys} {architecture}
    Kernel      : {kernel}
    Host        :
    DE          :
    Packages    :
    Shell       :
    CPU         :
    GPU         :
    Memory      :
    """.format(username=user,
               hostname=hostname,
               sys=system,
               architecture=architecture,
               kernel=kernel)

        print(infos)


Main()
