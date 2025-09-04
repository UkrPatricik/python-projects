import threading
import sys

def timeout():
    print("\nTime is up! Program closed due to inactivity.")
    sys.exit(0)

# set timer for 30 seconds
timer = threading.Timer(30.0, timeout)
timer.start()

name = input("Enter your name: ")
timer.cancel()  # cancel timer if input was received
print(f"Hello {name}!")
