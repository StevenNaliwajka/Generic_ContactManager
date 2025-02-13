import os

from dotenv import load_dotenv


class Secret:
    def __init__(self, secret_path):
        # Loads SECRET and parses
        load_dotenv(secret_path)
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = os.getenv("SMTP_PORT")
        self.user_email_address = os.getenv("USER_EMAIL_ADDRESS")
        self.app_password = os.getenv("APP_PASSWORD")