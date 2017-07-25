from bs4 import BeautifulSoup
import requests

from settings import Settings


class Reserve:
    ticketswap = "https://www.ticketswap.com"
    access_token = None
    session = requests.session()
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"

    def __init__(self):
        settings = Settings()
        self.access_token = settings.TICKETSWAP_SESSION

    def _get_form_data(self, link):
        r = self.session.get(link, headers={
            "User-Agent": self.user_agent
        }, cookies=dict(session=self.access_token))

        soup = BeautifulSoup(r.text, "html.parser")
        form_data = {}
        form = soup.find("form", id="listing-reserve-form")
        if not form:
            raise Exception("Ticket already sold")

        csrf_token = ''

        meta = soup.findAll("meta", attrs={'name': 'csrf_token'})
        for tag in meta:
            csrf_token = tag["content"]

        # TODO: amount
        form_data = {
            "csfr": str(csrf_token),
            "data-endpoint": str(form.get("data-endpoint")),
            "token": str(form.find("input", {"name": "token"})["value"]),
            "reserve_token": str(form.find("input", {"name": "reserve[_token]"})["value"]),
            "amount": "1"
        }

        return form_data

    def _reserve_post(self, form_data):

        headers = {
            "User-Agent": self.user_agent,
            "x-csrf-token": form_data.get("csfr")
        }
        payload = {
            "token": form_data.get("token"),
            "reserve[_token]": form_data.get("reserve_token"),
            "amount": form_data.get("amount")
        }

        r = self.session.post(
            "{}{}".format(self.ticketswap, form_data.get("data-endpoint")),
            headers=headers,
            data=payload,
            cookies=dict(session=self.access_token)
        )

        if r.status_code == 200: return True
        return False

    def reserve_ticket(self, link):
        if not link: raise Exception("No link provided to reserve")
        return self._reserve_post(self._get_form_data(link))
