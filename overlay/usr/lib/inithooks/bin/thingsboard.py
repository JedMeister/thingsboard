#!/usr/bin/python
"""Set ThingsBoard admin email and password
Option:
    --pass=          unless provided, will ask interactively
    --email=         unless provided, will ask interactively
"""

import re
import sys
import getopt
import inithooks_cache

from dialog_wrapper import Dialog
from pgsqlconf import PostgreSQL
import bcrypt
import psycopg2

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'password=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""

    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--email':
            email = val
        elif opt == '--password':
            password = val

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "ThingsBoard System Administrator's Email",
            "Enter email address for ThingsBoard System 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    if not password:
        password = d.get_password(
            "ThingsBoard System Admin Password",
            "Enter new password for ThingsBoard system 'admin' account.")

    salt = bcrypt.gensalt()
    hashpass = bcrypt.hashpw(password, salt)

    p = PostgreSQL(database='thingsboard')
    id, email = p.execute("select id, email from tb_user where authority = 'SYS_ADMIN';")
    p.execute('UPDATE users SET password=\'%s\' WHERE username=\'admin\';' % hashpass)

if __na
