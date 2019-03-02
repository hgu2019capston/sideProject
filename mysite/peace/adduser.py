import subprocess
import crypt

def adduser(username, pwd):
    
    sudopwd = 'codud0724'
    command = 'sudo -S useradd -m -s /bin/bash -p'
    command = command.split()

    password = crypt.crypt(pwd,"22")

    p = subprocess.Popen(command + [password, username],stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    p.communicate(sudopwd + '\n')[1]


#    subprocess.call(['sudo','useradd','-m',"-s","/bin/bash", "-p" , password, username])
#    subprocess.call(['sudo','usermod','-a','-G','sudo',username])

