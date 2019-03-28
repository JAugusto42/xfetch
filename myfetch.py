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

        path = "/var/lib/pacman/local/"
        count = 0
        for f in os.listdir(path):
            count += 1
        total_count = count - 1

        self.show_info(system, user, hostname, architecture, kernel, total_count)

    @staticmethod
    def show_info(system, user, hostname, architecture, kernel, total_count):
        infos = """
             {username}@{hostname}
           -----------------------
    OS          : {sys} {architecture}
    Kernel      : {kernel}
    Host        :
    DE          :
    Packages    : {packages}
    Shell       :
    CPU         :
    GPU         :
    Memory      :
    """.format(username=user,
               hostname=hostname,
               sys=system,
               architecture=architecture,
               kernel=kernel,
               packages=total_count
               )

        print(infos)


Main()
