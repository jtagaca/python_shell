from subprocess import run
import subprocess
import os


# run('ls -al', shell=True,  text=True)
# # run('sudo su -', shell=True,
# #     stdin="1")


# sudoPassword = '1'
# command = 'ls -al /etc'
# # p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))


# run('cd /etc', shell=True,  text=True)

import subprocess

# sudo_password = '1'
# command = '-i -u root \n id'
# command = command.split()


# this will work as long as we are in the sudoers file

sudoPassword = '1'
command = "su root"
# os.system('sudo -S %s' % (command))


p1 = run('cd /etc', capture_output=True, shell=True,  text=True)
# print(p1.stdout)


# cmd1 = subprocess.Popen(['echo', sudo_password], stdout=subprocess.PIPE)
# cmd2 = subprocess.Popen(['sudo', '-S'] + command,
#                         stdin=cmd1.stdout, stdout=subprocess.PIPE)

# run("apt install pip", shell=True)

# output = cmd2.stdout.read()

# print output
