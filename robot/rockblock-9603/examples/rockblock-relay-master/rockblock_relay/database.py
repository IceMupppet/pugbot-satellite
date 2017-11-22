import sys
import select
import psycopg2
import traceback
import logging as logging_module
from psycopg2.extras import RealDictCursor

from .config import config
from . import util

def connect():
    return psycopg2.connect(dbname=config["database"])

def cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)

def listen(callback):
    logger = logging_module.getLogger("rockblock_relay.database.listen")

    conn = connect()
    conn.autocommit = True

    cur = cursor(conn)
    cur.execute('LISTEN "messages_insert";')

    while True:
        try:
            select.select([conn], [], [], 600)
        except KeyboardInterrupt:
            break

        conn.poll()

        while conn.notifies:
            notify = conn.notifies.pop()
            id = int(notify.payload)

            cur.execute("SELECT * FROM messages WHERE id = %s", (id, ))
            row = cur.fetchone()
            logger.info("Handling %r", row)

            if row is not None:
                try:
                    callback(row)
                except KeyboardInterrupt:
                    raise
                except SystemExit:
                    raise
                except:
                    logger.exception("Exception while handling %s", id)
            else:
                logger.error("Failed to get row %s", id)

def insert(conn, message):
    logger = logging_module.getLogger("rockblock_relay.database")
    logger.info("insert %r", message)

    query = """
    INSERT INTO messages
    (source, imei, momsn, transmitted, latitude, longitude, latlng_cep, data)
    VALUES
    (%(source)s, %(imei)s, %(momsn)s, %(transmitted)s, %(latitude)s,
     %(longitude)s, %(latlng_cep)s, %(data)s)
    """

    with cursor(conn) as cur:
        cur.execute(query, message)

def main():
    setup_logging()
    listen(print)

if __name__ == "__main__":
    main()
