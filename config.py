import psycopg2


class config:
    def __init__(self, connectiondata):
        self.connectiondata = connectiondata

    def setParameters(self):
        self.connectiondata = {
            'host': 'localhost',
            'dbname': 'Northwind',
            'user': 'postgres',
            'password': 'postgres'
        }
