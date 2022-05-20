import psycopg2


class config:
    def __init__(self, connectiondata):
        self.connectiondata = connectiondata

    def setParameters(self):
        self.connectiondata = {
            'host': 'localhost',
            'dbname': 'northwind',
            'user': 'postgres',
            'password': 'postgres'
        }
        return self

    def alterDatabase(self, query, values):
        connection = None
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
            if connection is not None:
                connection.close()
        return 'Success'

    def consultDatabase(self, query, values):
        conn = None
        try:
            # connect to the PostgreSQL database
            connection = psycopg2.connect(
                config.setParameters(self).connectiondata)

            # create a new cursor (open a session)
            session = connection.cursor()

            # execute the command in ram
            session.execute(query, values)

            registers = session.fetchall()
            colnames = [desc[0] for desc in session.description]

            # commit the changes to the database
            connection.commit()

            # close the session
            session.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if connection is not None:
                connection.close()
        return (colnames, registers)
