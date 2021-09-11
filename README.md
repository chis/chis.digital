# chis.digital
Following the mega flask tutorial created by Miguel Grinberg I have implemented some basic functionality towards a personal blog website. As this is a learning experience I will find myself reinventing the wheel when it comes to implementation that is found on most popular blogging websites.

The website is hosted on a DigitalOcean Droplet which can be found [here](https://chis.digital)

There is still some functionality I would like to add, but in the meantime here is the installation instructions if you would like to test it yourself.

# Install

### Create a virtual environment
```bash
python -m venv venv
```
### Clone repository
```bash
git clone git@github.com:chis/chis.digital.git
```
### Source environment
```bash
source venv/bin/activate
```
### Install requirements
```bash
pip install -r requirements.txt
```
### Initialise flask-sqlalchemy database
```bash
flask db init
flask db migrate -m "First migration"
flask db upgrade
```
### Run application
```bash
flask run
```
