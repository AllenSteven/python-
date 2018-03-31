#-*- coding:utf-8 -*-
import pymysql

def connect_mysql_test():
    db = pymysql.connect("localhost","testuser","test123","TESTDB")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version:%s",data)
    db.close()

def create_db_list_test():
    db = pymysql.connect("localhost","testuser","test123","TESTDB")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    sql = """CREATE TABLE EMPLOYEE(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            AGE_INT,
            SEX CHAR(1),
            INCOME FLOAT)"""
    cursor.execute(sql)
    db.close()