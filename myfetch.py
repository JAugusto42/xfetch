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

        # get host name
        file = open("/sys/class/dmi/id/product_family", "r")
        manufacture = file.read().strip()

        # get DE or WM i think...
        desktop = os.environ.get('DESKTOP_SESSION')

        # getting current shell
        shell = os.environ['SHELL']
        current_shell = shell[5:]

        # getting cpu name
        with open('/proc/cpuinfo') as file:
            for line in file:
                if line.strip():
                    if line.rstrip('\n').startswith('model name'):
                        model_name = line.rstrip('\n').split(':')[1]
                        break

        self.show_info(system,
                       user,
                       hostname,
                       architecture,
                       kernel,
                       total_count,
                       manufacture,
                       desktop,
                       current_shell,
                       model_name
                       )

    @staticmethod
    def show_info(system,
                  user,
                  hostname,
                  architecture,
                  kernel,
                  total_count,
                  manufacture,
                  desktop,
                  current_shell,
                  model_name):
        infos = """
             {username}@{hostname}
           -----------------------
    OS          : {sys} {architecture}
    Kernel      : {kernel}
    Host        : {manufacture}
    DE          : {desktop}
    Packages    : {packages}
    Shell       : {shell}
    CPU         : {model}
    """.format(username=user,
               hostname=hostname,
               sys=system,
               architecture=architecture,
               kernel=kernel,
               packages=total_count,
               manufacture=manufacture,
               desktop=desktop,
               shell=current_shell,
               model=model_name.strip()
               )

        print(infos)


Main()
