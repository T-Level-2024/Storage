import os, socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
username = os.getlogin()


print("IP: "+ip)
print("Hostname: "+hostname)
print("User: "+username)
