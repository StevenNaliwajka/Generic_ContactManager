import os

from dotenv import load_dotenv

from CodeBase.Parse.validate_json_file import validate_json_file


class Message:
    def __init__(self, message_path):
        # Loads JSON file and parses
        data = validate_json_file(message_path)
        try:
            # Loads email recipients from 'data'
            self.recipients_list = []
            for email in data["TO_EMAILS"]:
                self.recipients_list.append(email)

            # loads subject and body.
            self.subject = data["SUBJECT"]
            self.body = data["BODY"]
        except:
            print("ERROR: Please verify the formating/contents of the JSON message file.")
            exit(1)
