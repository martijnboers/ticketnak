import configparser
import os


class Settings:
    FB_APP_ID = ''
    FB_APP_SECRET = ''
    FB_EVENT_ID = ''
    TICKETSWAP_SESSION = ''
    AMOUNT_TICKETS = 1

    def __init__(self):
        self._read_config()

    def _read_config(self):
        config = configparser.ConfigParser()
        try:
            config.read('{}/facebook.ini'.format(os.path.dirname(os.path.realpath(__file__))))
            self.FB_APP_ID = config['TICKETNAK']['FB_APP_ID'].strip('\'')
            self.FB_APP_SECRET = config['TICKETNAK']['FB_APP_SECRET'].strip('\'')
            self.FB_EVENT_ID = config['TICKETNAK']['FB_EVENT_ID'].strip('\'')
            self.TICKETSWAP_SESSION = config['TICKETSCOOP']['TICKETSWAP_SESSION'].strip('\'')
            self.AMOUNT_TICKETS = config['TICKETSCOOP']['AMOUNT_TICKETS']

        except Exception:
            exit("Please make sure facebook.ini is set")
