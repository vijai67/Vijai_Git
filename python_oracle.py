import cx_Oracle
class Connection(cx_Oracle.Connection):
    log_file_name = "log.txt"

    def __init__(self):
        connect_string = cx_Oracle.connect(user="VIJAI", password="8147",
                               dsn='localhost/orcl')
        self._log("Connect to the database")
        return super(Connection, self).__init__(connect_string)

    def _log(self, message):
        with open(self.log_file_name, "a") as f:
            print(message, file=f)

    def execute(self, sql, parameters):
        self._log(sql)
        cursor = self.cursor()
        try:
            return cursor.execute(sql, parameters)
        except cx_Oracle.Error as e:
            error_obj, = e.args
            self._log(error_obj.message)
            raise

connection = Connection()
connection.execute("""
        select * from tab""", dict(id=270))