import os
import sys

def custom_exit(message):
    print(message)  # Print the error message
    input("Press Enter to exit...")  # Pause the script
    sys.exit(1)  # Exit the script