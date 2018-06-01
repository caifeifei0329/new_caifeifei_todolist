
from flask import Flask, render_template, jsonify, request

from todo.db import TodoDb

app = Flask(__name__)
@app.route('/')
def index():
    db=TodoDb()
    todo=db.read_all()
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



if __name__=='__main__':

    app.run(debug=True);