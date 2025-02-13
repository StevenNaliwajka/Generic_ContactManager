import os
import sys

from CodeBase.Parse.message import Message
from CodeBase.Parse.secret import Secret
from CodeBase.send_email import send_email

if __name__ == "__main__":
    # Define where codebase should look for "secret" location
    secret_folder = os.path.join(os.path.dirname(__file__), "Config")
    secret_name = "secret.env"
    secret_path = os.path.join(secret_folder, secret_name)
    # Define where messages folder should be generated
    messages_folder = os.path.join(os.path.dirname(__file__), "Messages")

    # Create Secret Object
    secret = Secret(secret_path)

    try:
        message_path = sys.argv[1]
    except IndexError:
        print("ERROR: Please provide the path to a JSON message file on calling of program.")
        sys.exit(1)

    message = Message(message_path)
    send_email(message, secret)
