#!/usr/bin/python

import urllib2
import gzip
import rds_config  # references the local file rds_config.py. This is for demo purposes only, and is a horrible practice from a security perspective
import pymysql.cursors

db_name = rds_config.db_name
db_user = rds_config.db_user
db_pass = rds_config.db_pass
db_host = rds_config.db_host

try:
    # http://docs.aws.amazon.com/lambda/latest/dg/vpc-rds-deployment-pkg.html
    conn = pymysql.connect(db_host, user=db_user, passwd=db_pass, db=db_name)
except Exception as e:
    sys.exit()


def downloadGoogleHomePage():
    # http://www.pythonforbeginners.com/python-on-the-web/how-to-use-urllib2-in-python/
    try:
        googleIndex = urllib2.urlopen("www.google.com")
    except urllib2.URLError, e:
        print(str(e))
    output = open('google_index.html', 'wb')
    output.write(googleIndex.read())
    output.close()


def checkSqlVersion():
    cur = conn.cursor()
    cur.execute('show version()')
    result = cur.fetchone()
    print str(result)
    cur.close()
    conn.close()


def lambda_handler(event, context):
    # Entry point for lambda execution
    downloadGoogleHomePage()
    checkSqlVersion()


if __name__ == '__main__':
    # Entry point for local execution
    downloadGoogleHomePage()
    checkSqlVersion()
