import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 22284698))

    API_HASH = os.environ.get("API_HASH", "80114fbfcdb5b886a9e69f31a7e6b248")
