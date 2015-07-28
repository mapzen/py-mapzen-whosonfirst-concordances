# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sqlite3
import os.path
import logging
import csv

class base:

    def __init__(self):

        self.conn = None
        self.curs = None

    def this_id(self, that_id):
        
        that_id = unicode(that_id)

        sql = "SELECT this_id FROM concordances WHERE that_id=?"

        self.curs.execute(sql, (that_id,))
        row = self.curs.fetchone()

        if row:
            return row[0]

        return 0

    def that_id(self, this_id):

        this_is = unicode(this_id)

        sql = "SELECT that_id FROM concordances WHERE this_id=?"

        self.curs.execute(sql, (this_id,))
        row = self.curs.fetchone()

        if row:
            return row[0]

        return 0

class importer(base):

    def __init__(self, db):

        base.__init__(self)
        self.db = db

        if os.path.exists(db):

            self.conn = sqlite3.connect(db)
            self.curs = self.conn.cursor()

        else:

            self.conn = sqlite3.connect(db)
            self.curs = self.conn.cursor()

            self.curs.execute("""CREATE TABLE concordances (this_id PRIMARY KEY ASC, that_id, that_isa)""")
            self.curs.execute("""CREATE UNIQUE INDEX by_woe ON concordances(this_id, that_id, that_isa)""")
            self.conn.commit()

    # generic csv importer tool thingy where the first row is always
    # assumed to be the woe id and an INTEGER as per above (which maybe
    # we want to change... (20150622/thisisaaronland)

    def import_csv(self, path):

        path = os.path.abspath(path)

        fh = open(path, 'r')
        reader = csv.reader(fh)
        
        for row in reader:
            this_id, that_id, that_isa = row

            self.import_concordance(this_id, that_id, that_isa)

    # https://github.com/foursquare/twofishes/raw/master/data/computed/concordances.txt

    def import_twofishes(self, path):

        path = os.path.abspath(path)
        fh = open(path, 'r')

        for ln in fh.readlines():

            ln = ln.strip()
            gnid, woeid = ln.split('\t')
            
            ignore, gnid = gnid.split(':')
            ignore, woeid = woeid.split(':')

            self.import_concordance(woeid, gnid, 'geonames')

    def import_concordance(self, this_id, that_id, that_isa=''):

        sql = "INSERT INTO concordances VALUES ('%s', '%s')" % (this_id, that_id, that_isa)
        
        try:
            self.curs.execute(sql)
            self.conn.commit()
        except Exception, e:
            logging.error(e)
            logging.debug(sql)

class lookup(base):

    def __init__(self, db):
        
        base.__init__(self)

        self.conn = sqlite3.connect(db)
        self.curs = self.conn.cursor()
