import configparser
import os


class Settings:
    FB_APP_ID = ''
    FB_APP_SECRET = ''
    FB_EVENT_ID = ''

    def __init__(self):
        self._read_config()

    def _read_config(self):
        config = configparser.ConfigParser()
        try:
            config.read('{}/facebook.ini'.format(os.path.dirname(os.path.realpath(__file__))))
            self.FB_APP_ID = config['TICKETNAK']['FB_APP_ID'].strip('\'')
            self.FB_APP_SECRET = config['TICKETNAK']['FB_APP_SECRET'].strip('\'')
            self.FB_EVENT_ID = config['TICKETNAK']['FB_EVENT_ID'].strip('\'')

        except Exception:
            exit("Please make sure facebook.ini is set")
