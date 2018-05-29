
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    todo={
        '测试一',
        '测试二',
        '测试三',
        '测试四',
        '测试五'
    }
    return render_template('index.html',data=todo)
if __name__=='__main__':

    app.run(debug=True);