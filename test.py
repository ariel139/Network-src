import subprocess

devices = []
def ping():
    try:
        res = subprocess.check_output(["ping","-n","1","10.100.102.36"])
        if res != None:
            print(res.decode())
    except subprocess.CalledProcessError:
        return False

ping()
print(devices)