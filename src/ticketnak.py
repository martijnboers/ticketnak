import datetime

import facebook
import requests
import time
import logging
import webbrowser

# noinspection PyMethodMayBeStatic
from settings import Settings


class TicketNak:
    graph = None
    settings = None
    fb_api = 'https://graph.facebook.com'
    known_post = []
    logger = None

    def __init__(self):
        self.settings = Settings()
        self.graph = facebook.GraphAPI(access_token=self._get_acces_token(), version='2.9')
        self.logger = logging.basicConfig(level=logging.DEBUG)

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
            except KeyError:
                continue

            except Exception as e:
                self.logger.exception(e)

        return feed

    def _check(self, post):
        date = datetime.datetime.strptime(post['updated_time'], '%Y-%m-%dT%H:%M:%S+0000')
        if date > datetime.datetime.now() - datetime.timedelta(hours=1):
            if post['id'] not in self.known_post:
                self.known_post.append(post['id'])
                post_fb = self.graph.get_object(id=post['id'], fields='link')
                if "wanted" in post_fb['link']:
                    return
                self._notify(post_fb['link'])

    def _notify(self, link):
        webbrowser.open(link)

    def run(self):
        while 1:
            print('refreshed')
            self._filter_ticketswap_post(self._get_event_feed())
            time.sleep(2)


if __name__ == '__main__':
    ticketnak = TicketNak()

    ticketnak.run()
