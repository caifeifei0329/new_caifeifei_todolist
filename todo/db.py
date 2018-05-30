import sqlite3


class TodoDb():
    def read_all(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
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
        conn=sqlite3.connect('test.db')
        cursor=conn.cursor()
        cursor.execute('create table todo(id integer primary key AUTOINCREMENT,content varchar(200) )')
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self, todo_id):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('delete from todo where id=todo_id')
        cursor.close()
        conn.commit()
        conn.close()

        print('delete', todo_id)


if __name__=='__main__':
    db=TodoDb()
    # db.init_db()
    db.read_all()