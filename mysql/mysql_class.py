#!/usr/bin/python3
#-*-coding:utf-8-*-

import pymysql

class mysql_class:
    def create_db(self,db_host, db_user,db_passwd, db_name):
		print("create db "+db_name)
		db = pymysql.connect(db_host, db_user, db_passwd)
		cursor = db.cursor()
		cursor.execute('create database if not exists '+db_name)
		db.commit()
		db.close()
		
    def connect_mysql(self,sql_info):
        print("connect mysql database")
        db = pymysql.connect(sql_info[0],sql_info[1],sql_info[2],sql_info[3])
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("cursor.fetchone():%s"%data)
        return cursor,db


    def disconnect_mysql(self,db):
        print("disconnect mysql database")
        db.close()

    def create_table(self,cursor,sql):
        print(sql)
        cursor.execute(sql)

    #insert,update,delete
    def modify_database(self,db,cursor,sql):
        print("insert data to mysql:"+sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        print("insert successfull")

    def select_data(self,cursor,sql):
        print("select data form mysql")
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return result
        except:
            import traceback
            traceback.print_exc()
            print("Error:unable to fetch data")

def test_database():
    testdb = mysql_class()
    sql_info =["localhost","test","test123","DBxiaohua_2"]
    testdb.create_db(sql_info[0],sql_info[1],sql_info[2],sql_info[3])
    cursor,db = testdb.connect_mysql(sql_info)
    sql = "create table if not exists joke_table(id int(32) not null auto_increment,userName varchar(25) not null,userImg varchar(1024) null,jokeText varchar(1024) null, jokeImg varchar(4096)  null,jokeVideo varchar(1024)  null, primary key(id))engine=InnoDB default charset=utf8;"
    testdb.create_table(cursor,sql)
    testdb.disconnect_mysql(db)




def main():
    print("test mysql database")
    test_database()

if __name__ == '__main__':
    main()

