# Python Selenium Bot For Instagram

## Installation

Create a file called `app/settings.py`. 

Fill in your credentials like below in the `app/settings.py`:

```
USERNAME = 'username'
PASSWORD = 'password'
URL = 'https://www.instagram.com/'
SELENIUM_HUB = 'http://selenium:4444/wd/hub'
```

And run docker compose:

```
docker-compose up --build
```