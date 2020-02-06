
# cnx = mysql.connector.connect(user='root', password='tuananh',
#                               host='127.0.0.1',
#                               database='exchange_books',
#                               auth_plugin='mysql_native_password')


# sql_select_Query = "select * from wp_posts where post_status = 'publish'"
# cursor = cnx .cursor()
# cursor.execute(sql_select_Query)
# records = cursor.fetchall()
# print("Total number of rows in python_developers is - ", cursor.rowcount)

# from mysql.connector import (connection)

# cnx = connection.MySQLConnection(user='root', password='awt@mariadb',
#                                  host='172.16.18.128',
#                                  database='bk',
#                                  auth_plugin='mysql_native_password')

# sql_select_Query = "select * from teachers'"
# cursor = cnx .cursor()
# cursor.execute(sql_select_Query)
# records = cursor.fetchall()
# print("Total number of rows in python_developers is - ", cursor.rowcount)


import mysql.connector

cnx = mysql.connector.connect(user='root', passwd='123456a@',
                              host='127.0.0.1',
                              db='bk',
                              auth_plugin='mysql_native_password')


def api_teachers():
    list_teachers = []
    sql_select_Query = "select * from teachers"
    cursor = cnx .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    # print("Total number of rows in python_developers is - ", cursor.rowcount)
    # print(records)
    # cnx.close()
    for obj in records:
        techerJson = {
            'teacher_id': obj[0],
            'name': obj[1],
            'phone': obj[2],
            'mail': obj[3]
        }
        list_teachers.append(techerJson)
    # print(list_teachers)
    return list_teachers


api_teachers()
