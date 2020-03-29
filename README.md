# COVID-19 Support

The aim of this project is offer different utilities to be used on epidemy management including:
- Home screening
- Different triage levels
This application will manage the APIs to store and process information received from different surces and is supported for IA models.

## Dependencies - prerequisites

You need a working installation/setup of `postgresql`.

**For Debian/ubuntu:** `sudo apt-get install libpq-dev`
**For Archlinux:** `sudo pacman -S postgresql postgresql-libs`

## How to use it (local)?

1. Clone repository
```
git clone https://github.com/combios/covid19-support-backend.git
```
2. Install dependencies using `pipenv`
```
pip3 install pipenv
pipenv install
```
3. Start the server
```
pipenv run app/manage.py runserver
```
4. Open your admin interface from http://localhost:8000/admin
