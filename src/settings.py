import configparser
import os


class Settings:
    FB_APP_ID = ''
    FB_APP_SECRET = ''
    FB_EVENT_ID = ''

    def __init__(self):
        config = configparser.ConfigParser()
        try:
            print('{}/facebook.ini'.format(os.getcwd()))
            config.read('{}/facebook.ini'.format(os.path.dirname(os.path.realpath(__file__))))
        except Exception as e:
            print('Please make sure facebook.ini is set')
            exit()

        if config['TICKETNAK']['FB_APP_ID'] and config['TICKETNAK']['FB_APP_SECRET'] and config['TICKETNAK'][
            'FB_EVENT_ID']:
            self.FB_APP_ID = config['TICKETNAK']['FB_APP_ID'].strip('\'')
            self.FB_APP_SECRET = config['TICKETNAK']['FB_APP_SECRET'].strip('\'')
            self.FB_EVENT_ID = config['TICKETNAK']['FB_EVENT_ID'].strip('\'')
        else:
            raise Exception("Missing configuration")
