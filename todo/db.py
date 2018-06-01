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
        data=cursor.execute('select  id ,content from todo')
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
        cursor.execute('create table todo(id integer primary key AUTOINCREMENT,content varchar(200) )')
        cursor.close()
        self.conn.commit()
        self.conn.close()

    def delete(self, todo_id):
        # conn = sqlite3.connect('test.db')
        cursor = self.cursor()
        cursor.execute('delete from todo where id= ?',(todo_id,))
        cursor.close()
        self.commit()
        # self.conn.close()

    def read(self, todo_id):
        cursor = self.cursor()
        cursor.execute('select id ,content from todo where id= ?', (todo_id,))
        data=cursor.fetchone()
        print(data)
        cursor.close()
        return data

    def create(self, text):
        cursor = self.cursor()
        cursor.execute('insert into todo(content) values (?)', (text,))
        cursor.close()
        self.commit()



if __name__=='__main__':
    db=TodoDb()
    # db.init_db()
    db.read_all()
    # db.read(16)