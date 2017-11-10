# Setup telnet on server by using following commands
"""
1.Install telnet use this command in terminal:
sudo apt-get install xinetd telnetd

2.Edit /etc/inetd.conf with root permission, add this line:
telnet stream tcp nowait telnetd /usr/sbin/tcpd /usr/sbin/in.telnetd

3.Edit /etc/xinetd.conf,add following content in file:
defaults
{
    instances = 60
    log_type = SYSLOG authpriv
    log_on_success = HOST PID
    log_on_failure = HOST
    cps = 25 30
}

4.Use this command to start telnet server:
sudo /etc/init.d/xinetd restart
"""

import getpass
import telnetlib

HOST = "localhost"
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password.encode('ascii') + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()
