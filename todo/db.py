import sqlite3


class TodoDb():
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
    def cursor(self):
        return self.conn.cursor()
    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()
    def read_all(self):
        # conn = sqlite3.connect('test.db')
        cursor = self.cursor()
        data=cursor.execute('select  id ,content , status from todo order by id desc')
        data=data.fetchall()
        # data=[d[0] for d in data]
        return data
    # def insert_db(self):
    #     conn = sqlite3.connect('test.db')
    #     cursor = conn.cursor()
    #     data=cursor.execute('insert into todo(content) values(?)')


    # def delete_db(self):
    #





    def init_db(self):
        # conn=sqlite3.connect('test.db')
        cursor=self.conn.cursor()
        cursor.execute('create table IF not EXISTS  todo(id integer primary key AUTOINCREMENT,content varchar(200) )')
        cursor.close()
        self.conn.commit()
        # self.conn.close()

    def delete(self, todo_id):
        # conn = sqlite3.connect('test.db')
        cursor = self.cursor()
        cursor.execute('delete from todo where id= ?',(todo_id,))
        cursor.close()
        self.commit()
        # self.conn.close()

    def read(self, todo_id):
        cursor = self.cursor()
        cursor.execute('select id, content, status  from todo where id= ?', (todo_id,))
        data=cursor.fetchone()
        cursor.close()
        return data

    def create(self, text):
        cursor = self.cursor()
        cursor.execute('insert into todo( content,status ) values ( ? ,?)', (text,'doing'))
        cursor.close()
        self.commit()

    def migrate_lates(self,todo_id):
        self.init_db()
        self.s2_sdd_status_column()

    def s2_sdd_status_column(self):
        cursor = self.cursor()
        cursor.execute('alter table todo add column status varchar(50) default "doing"')
        cursor.close()
        self.commit()
        self.close()

    #更新

    def updata_todo(self, todo_id, status):
        cursor = self.cursor()
        cursor.execute('update todo set status= ? where id=?', (status, todo_id))
        self.commit()
        cursor.close()
        self.close()



# 登录
#     def select_username(self, username):
#         cursor = self.cursor()
#         cursor.execute('select pwd from user where username= ?', (username,))
#         user = cursor.fetchone()
#         print(user)
#         cursor.close()
#         return user




if __name__=='__main__':
    db=TodoDb()
    # db.init_db()
    # db.read_all()
    # db.migrate_lates()
    # db.read(16)
    # db.updata_todo(5,'done')