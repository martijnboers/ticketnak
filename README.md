# Ticketnak

*IMPORTANT: Currently automatic reservation is not working because of changes in the Ticketswap site*

Project aimed to crawl Ticketswap listings on Facebook event and automatically opening the Ticketswap link in your browser
as soon as it's posted. This (automatically) reserves the ticket for the user and is faster than refreshing on your own and clicking on the link.
Uses official Facebook API and doesn't crawl Ticketswap making it possible to run for hours in the background without 
getting blocked by Ticketswap.

The current interval is 2 seconds and I'm testing Facebook's request limit.

### Prerequisites

Runs on:

* Python=>3.0
* Python facebook-sdk

### Installing

```
git clone https://github.com/MartijnDevNull/ticketnak.git
```

```
cd ticketnak
```
```
virtualenv --python=/usr/bin/python3 env
```
```
source env/bin/activate
```
```
pip3 install -r requirements.txt
```
```
cd src
```
```
cp facebook.ini-default facebook.ini
```
See Running for configration options

## Running

Make sure you have the configuration file (facebook.ini) setup with your Facebook event id. This can be found in the URL, for example:
* URL: https://www.facebook.com/events/1452202511485808/
* Eventid: 1452202511485808

Next create add your FB_APP_ID and FB_APP_SECRET found in [Facebook developer](https://developers.facebook.com/apps/). Create
a new app if none exist

After this login to Ticketswap and get the session cookie so the ticket is automatically added to cart (*TODO*: set ticket amount, now default 1)

You can run Ticketnak with:
```
python3.x ticketnack.py
```
Replace with your version of Python 3


## Built With

* [Facebook SDK](https://github.com/mobolic/facebook-sdk) - Python SDK for Facebook's Graph API
* [TicketScoop](https://github.com/matthisk/TicketScoop) - Automatic reservation of tickets is based on this project
## License

This project is licensed under the GPL v3 - see the [LICENSE](LICENSE) file for details
