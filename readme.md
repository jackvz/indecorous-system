# [Indecorous System](https://system.indecorous.online/)

Run a virtualised Linux box in your web browser.

## About

### Built With

- [v86](https://copy.sh/v86/) - JavaScript x86 CPU and hardware emulator - [License](./v86-license)
- [SeaBIOS](https://www.seabios.org/SeaBIOS) - [License](./seabios-license)
- [Tiny Core Linux](http://tinycorelinux.net)
- [Topcoat](http://topcoat.io/)
<!-- - [Simple keyboard](https://virtual-keyboard.js.org/) -->

## About Tiny Core Linux

[The Tiny Core Linux Book](http://tinycorelinux.net/corebook.pdf)

Install packages with `tce-load`, e.g.
```sh
tce-load -wi [package]
```

[See a list of Tiny Core Linux 7's packages.](http://tinycorelinux.net/7.x/x86/tcz/)

[See a list of Tiny Core Linux 11's packages.](http://tinycorelinux.net/11.x/x86/tcz/)

## Setup

### Install [Python](https://www.python.org/) and [virtualenv](https://pypi.org/project/virtualenv/)

### [Set up a WebSockets Proxy](https://github.com/jackvz/websockets-proxy-on-google)

Set `network_relay_url` of `emulator` in the script in [index.html](./app/templates/index.html).

### Get Tiny Core Linux

Get Tiny Core Linux 7:
```sh
wget --directory-prefix=./static/system-images/ http://tinycorelinux.net/7.x/x86/release/Core-7.2.iso
```

Get Tiny Core Linux 11:
```sh
wget --directory-prefix=./static/system-images/ http://tinycorelinux.net/11.x/x86/release/Core-11.1.iso
```

Specify the system image as the `cdrom` of `emulator` in the script in [index.html](./app/templates/index.html). The source code here specifies version 7 because the [Node.js](https://nodejs.org/en/) package is available.

## Run

Start a Python virtual environment:
```bash
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

Run:
```bash
python3 app/wsgi.py
```

Browse to [http://localhost:8000/](http://localhost:8000/)

## Deploy

[Deploy to Heroku with Gunicorn.](https://devcenter.heroku.com/articles/python-gunicorn)

[Install the Heroku CLI.](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

```sh
heroku login
heroku git:remote -a [app-name]
git push heroku master --force
```
