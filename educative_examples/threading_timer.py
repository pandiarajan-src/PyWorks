
import subprocess
from sys import stderr
from threading import Timer

kill = lambda process : process.kill()
cmd = ["ping", "www.google.com"]
ping = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

timer = Timer(5, kill, [ping])

try:
    timer.start()
    stdout, stderr = ping.communicate()
finally:
    timer.cancel()

print(str(stdout))

