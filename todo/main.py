
from flask import Flask, render_template, jsonify, request

from todo.db import TodoDb
from todo.login_db import Login

app = Flask(__name__)
@app.route('/')
def index():
    db=TodoDb()
    todo=db.read_all()
    print(todo)
    return render_template('index.html',data=todo)
@app.route('/todo/<int:todo_id>',methods=['DELETE'])
def delete(todo_id):
    db = TodoDb()
    todo = db.delete(todo_id)

    result=db.read(todo_id)
    db.close()
    return jsonify({'existed':True })if result else jsonify({'existed': False})
    # return 'ok'

@app.route('/todo',methods=['POST'])
def add():
    data=request.get_json()
    print(data)
    db=TodoDb()
    todo=db.create(data['text'])
    db.close()
    # print('add todo')
    return 'ok'

@app.route('/todo/<int:todo_id>',methods=['PUT'])
def update(todo_id):
    db=TodoDb()

    result = db.read(todo_id)
    if result:
        status=result[2]
        status='done' if status=='doing' else 'doing'
        print(status)
        db.updata_todo(todo_id,status)
    db.close()
    return 'hello'




'''
登录界面
'''
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     db = TodoDb()
#
#     if request.method=='POST':
#             username = request.form['username']
#             password = request.form['password']
#             result=db.select_username(username)
#             if password==result[2]:
#                 return render_template('login.html')




if __name__=='__main__':

    app.run(debug=True);