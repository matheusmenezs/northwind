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

    def alterDatabase(self, query, values):
        conn = None
        try:
            # connect to the PostgreSQL database
            connection = psycopg2.connect(
                config.setParameters(self).connectiondata)
            # create a new cursor (open a session)
            session = connection.cursor()

            # execute the command in ram
            session.execute(query, values)

            # commit the changes to the database
            connection.commit()

            # close the session
            session.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return 'Success'
