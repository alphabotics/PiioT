from orator import DatabaseManager, Schema, Model

DATABASES = {
    'default': 'mysql',
    'mysql': {
        # 'read': {
        #     'host': '192.168.1.1'
        # },
        # 'write': {
        #     'host': '192.168.1.2'
        # },
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'fastadmin',
        'user': 'root',
        'password': 'root',
        'prefix': '',
        'log_queries': True
    },
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "db_name",
        "user": "db_user",
        "password": "db_password",
        "prefix": "",
        "port": 5432
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)