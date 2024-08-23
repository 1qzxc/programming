import getpass
import telnetlib

IP = "192.168.1.XXX"
user = input("enter username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(IP)

tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(user.encode("ascii") + b "\n")
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"hostname CoreSW\n")
tn.write(b"end\n")
tn.write(b"write memory\n")