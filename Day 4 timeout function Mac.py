import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    print("\nNo activity detected. Program closed due to timeout.")
    sys.exit(0)

# set timeout to 30 seconds
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(30)   # 30 seconds

# example input
name = input("Enter your name: ")

# reset or extend timeout after successful input
signal.alarm(30)
age = input("Enter your age: ")

print(f"Hello {name}, you are {age} years old.")
