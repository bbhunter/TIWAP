# Imports
import sqlite3
from helper.db_manager import DBManager


# Global Objects
dbmanager = DBManager()


# SQL Injection - Low
def sqli_low(username, password):
    global dbmanager

    cur = dbmanager.get_db_connection().cursor()

    if dbmanager.check_user(username=username):
        return "User Exists"

    try:
        stmt = "SELECT userid, username FROM users WHERE username='%s' AND password='%s'" \
               % (str(username), str(password))

        result = cur.execute(stmt)

    except sqlite3.OperationalError as e:
        return e

    return result.fetchall()


# SQL Injection - Medium
def sqli_medium(userid):
    global dbmanager

    cur = dbmanager.get_db_connection().cursor()

    try:
        stmt = "SELECT userid, username FROM users WHERE userid='%s'" % (str(userid))

        result = cur.execute(stmt)

    except sqlite3.OperationalError as e:
        return e

    return result.fetchall()


# SQL Injection - Hard
def sqli_hard(usernameid):
    global dbmanager

    cur = dbmanager.get_db_connection().cursor()

    if "1'" in usernameid or "1'OR1=1" in usernameid or "1' OR 1=1" in usernameid or "1' OR '1'='1" in usernameid:
        return "Try Harder"

    if "#" in usernameid:
        usernameid = usernameid.replace("#", "'")

    try:
        stmt = "SELECT userid, username FROM users WHERE userid='%s'" % (str(usernameid))

        result = cur.execute(stmt)
    except sqlite3.OperationalError as e:
        return e

    return result.fetchall()


# Blind SQL Injection - Low
def blind_sqli_low(username, password):
    global dbmanager

    cur = dbmanager.get_db_connection().cursor()

    if dbmanager.check_user(username=username):
        return "User Exists"

    try:
        stmt = "SELECT userid, username FROM users WHERE username='%s' AND password='%s'" \
               % (str(username), str(password))

        result = cur.execute(stmt)

    except sqlite3.OperationalError:
        return ""

    return result.fetchall()


# Bling SQL Injection - Medium
def blind_sqli_medium(userid):
    global dbmanager

    cur = dbmanager.get_db_connection().cursor()

    try:
        stmt = "SELECT userid, username FROM users WHERE userid='%s'" % (str(userid))

        result = cur.execute(stmt)

    except sqlite3.OperationalError:
        return ""

    return result.fetchall()


# Blind SQL Injection - Hard
def blind_sqli_hard(usernameid):
    global dbmanager

    cur = dbmanager.get_db_connection().cursor()

    if "1'" in usernameid or "1'OR1=1" in usernameid or "1' OR 1=1" in usernameid or "1' OR '1'='1" in usernameid:
        return "Try Harder"

    if "#" in usernameid:
        usernameid = usernameid.replace("#", "'")

    try:
        stmt = "SELECT userid, username FROM users WHERE userid='%s'" % (str(usernameid))

        result = cur.execute(stmt)
    except sqlite3.OperationalError as e:
        return ""

    return result.fetchall()
