import psycopg2

class editor():
    def __init__(self, db, user, password, host, port):
        self.db = db
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.con = psycopg2.connect(database = db, user = user, password = password, host = host, port = port)

    def create_table(self, tablename, **kwargs):
        cur = self.con.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {tablename}")
        cur.execute(f"CREATE TABLE {tablename} ()")
        try:
            for row in kwargs["rows"]:
                cur.execute(f"ALTER TABLE {tablename} ADD COLUMN {row}")
        except:
            pass
        self.con.commit()

    def drop_table(self, tablename):
        cur = self.con.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {tablename}")
        self.con.commit()
    
    def run(self, command):
        cur = self.con.cursor()
        cur.execute(f"{command}")
        self.con.commit()
    