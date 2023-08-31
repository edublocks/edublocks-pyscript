import time
from js import prompt

def sleep(seconds):
	start = now = time.time()
	while now - start < seconds:
		now = time.time()

time.sleep = sleep
__builtins__.input = prompt
