# irithm-cards
Sample Flask Rebar App


## Requirements
Tested on Python 3.6.5
Expected to work on Python >3.6

## Environment Setup
### Creation and Activation of Virtual Environment
```bash
pip install virtualenv
virtualenv --python=python3.6 venv
source venv/bin/activate
```
### Installation of Libraries
```bash
pip install -r requirements
```

### Database Creation
Requirement: Postgresql
```bash
service postgresql start
service postgresql status
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'password';"
sudo -u postgres createdb irithm
```

### Schema Migration
Run peewee-migrate cli
```bash
pem migrate
```

### Unit Tests
