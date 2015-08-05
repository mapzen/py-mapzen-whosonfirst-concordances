# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sys
import logging
import psycopg2

def cfg2dsn(cfg, sect):
        
    db_user = cfg.get(sect, 'db_user')
    db_pswd = cfg.get(sect, 'db_pswd')
    db_host = cfg.get(sect, 'db_host')
    db_name = cfg.get(sect, 'db_name')
    
    dsn = "dbname=%s user=%s password=%s host=%s" % (db_name, db_user, db_pswd, db_host)
    return dsn

class db:

    def __init__(self, dsn):

        conn = psycopg2.connect(dsn)
        curs = conn.cursor()

        self.conn = conn
        self.curs = curs

class index(db):

    def import_concordance(self, wof_id, other_id, other_src=''):

        sql = "INSERT INTO concordances (wof_id, other_id, other_src) VALUES (%s, %s, %s)"
        params = (wof_id, other_id, other_src)

        logging.debug("import %s" % str(params))

        try:
            self.curs.execute(sql, params)
            self.conn.commit()
        except psycopg2.IntegrityError, e:
            logging.debug("%s is already concordified with %s %s" % (wof_id, other_src, other_id))
            self.conn.rollback()
        except Exception, e:
            logging.error("failed to concordify %s because %s" % (wof_id, e))
            self.conn.rollback()
            raise Exception, e

class query(db):

    def by_wof_if(self, wof_id):
        pass
