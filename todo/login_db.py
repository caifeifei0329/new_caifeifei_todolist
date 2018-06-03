import sqlite3

class Login():
    def init_logindb(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('create table user(id integer primary key AUTOINCREMENT,username varchar(200) UNIQUE, pwd varchar(40) )')
        cursor.close()
        conn.commit()
        conn.close()








if __name__=="__main__":
    login=Login()
