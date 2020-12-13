# FastAdmin

Build with FastAPI and VueJS.


## Quickstart

### Setup environment

```shell
# create virtualenv ith python 3.7
virtualenv -p python3.7 venv-py3.7
source venv-py3.7/bin/activate
pip install -r requirements.in

# Run Database Migrations
# alembic upgrade head

# Run FasiAPI App.on special port 
uvicorn App.main:app --reload --port 8009
```

### Run Testing

```shell
pytest App/Tests

# OR
./test.sh
```

#### Admin Dashboard

FastAdmin use Vue and Vuetify for build awesome Admin Dashboad with material design.

To start FastAdmin Restful API backend:

```shell
cd fast_admin
uvicorn App.main:App.--reload --port 8009
```

To start FastAdmin Dashboard UI (in development mode):

```shell
cd themes/admin
yarn serve
```

To start Vuetify

```shell
vue ui
```

