import time
import sys

def loading_screen(seconds):
    print("Loading...")
    for i in range(seconds):
        sys.stdout.write("\r")
        sys.stdout.write("[{}{}]".format('=' * i, ' ' * (seconds - i - 1)))
        sys.stdout.flush()
        time.sleep(1)
    print("\nLoading complete!")

# Example usage:
loading_screen(10)  # Simulates a 5-second loading process