#!/usr/bin/python3
#-*-coding:utf-8-*-

import pymysql

class mysql_class:

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
            #print(result)
            return result
        except:
            import traceback
            traceback.print_exc()
            print("Error:unable to fetch data")

def test_database():
    testdb = mysql_class()
    sql_info =["localhost","test","test123","DBxiaohua_2"]
    cursor,db = testdb.connect_mysql(sql_info)
    sql = "select * from joke_table;"
    result = testdb.select_data(cursor,sql)
    print("result:")
    print(len(result[0]))
    for row in result:
        id = row[0]
        if row[1]:
            username = row[1].decode("utf-8")
        else:
            username = row[1]
        if row[2]:
            userimg = row[2].decode("utf-8")
        else:
            userimg = row[2]
        if row[3]:
            joketext = row[3].decode("utf-8")
        else:
            joketext = row[3]
        if row[4]:
            jokeimg = row[4].decode("utf-8")
        else:
            jokeimg = row[4]
        if row[5]:
            jokevideo = row[5].decode("utf-8")
        else:
            jokevideo = row[5]
        #print("id = %s name = %s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))
        print("******************************************")
        print(id)
        print(username)
        print(userimg)
        print(joketext)
        print(jokeimg)
        print(jokevideo)
        
    testdb.disconnect_mysql(db)




def main():
    print("test mysql database")
    test_database()

if __name__ == '__main__':
    main()

