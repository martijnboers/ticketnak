import datetime

import facebook
import requests
import time

import webbrowser

# noinspection PyMethodMayBeStatic
from src.settings import Settings


class TicketNak:
    graph = None
    settings = None
    fb_api = 'https://graph.facebook.com'
    known_post = []

    def __init__(self):
        self.settings = Settings()
        self.graph = facebook.GraphAPI(access_token=self._get_acces_token(), version='2.9')

    def _get_acces_token(self):
        r = requests.get(
            '{}/oauth/access_token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
                self.fb_api, self.settings.FB_APP_ID, self.settings.FB_APP_SECRET))

        return r.json()['access_token']

    def _get_event_feed(self):
        return self.graph.get_object(id='{}/feed'.format(self.settings.FB_EVENT_ID), fields='story,updated_time,id')[
            'data']

    def _filter_ticketswap_post(self, feed):
        for post in feed:
            try:
                if "shared a link to the event" in post['story']:
                    self._check(post)
            except Exception as e:
                continue
        return feed

    def _check(self, post):
        date = datetime.datetime.strptime(post['updated_time'], '%Y-%m-%dT%H:%M:%S+0000')
        if date > datetime.datetime.now() - datetime.timedelta(hours=10):
            if post['id'] not in self.known_post:
                self._notify(post)
                self.known_post.append(post['id'])

    def _notify(self, post):
        post = self.graph.get_object(id=post['id'], fields='link')
        webbrowser.open(post['link'])

    def run(self):
        while 1:
            print('refreshed')
            self._filter_ticketswap_post(self._get_event_feed())
            time.sleep(7)


if __name__ == '__main__':
    ticketnak = TicketNak()

    ticketnak.run()
