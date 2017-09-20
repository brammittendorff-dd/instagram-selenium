# Python Selenium Bot For Instagram

## Installation

Create a file called `.env`. 

Fill in your credentials like below in the `.env`:

```
HOSTNAME=seleniumcontainer
USERNAME=username
PASSWORD=password
URL_INSTAGRAM=https://www.instagram.com/
URL_SELENIUM_HUB=http://seleniumcontainer:4444/wd/hub
```

And run docker compose:

```
docker-compose up --build
```