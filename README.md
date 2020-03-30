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
3. Configure environment
```
export AWS_REGION=XXXX-X
export AWS_USER_POOL=XXXX-X_XXXXXX
export AWS_CLIENT_ID=XXXX
```
4. Migrations 
view https://code.djangoproject.com/ticket/22563 for LogEntry.user Fails
```
pipenv run app/manage.py migrate
```
1. Start the server
```
pipenv run app/manage.py runserver
```
6. Open your admin interface from http://localhost:8000/admin

## Lambdas
```
# autoconfirm user on preSignUp
def lambda_handler(event, context):
    # default confirm user
    event['response']['autoConfirmUser'] = True
    # Return to Amazon Cognito
    return event
```