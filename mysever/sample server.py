from flask import Flask,request,jsonify



app = flask(__name__)

@app.route('/hello')
def hello():
    return"Hii"

if __name__=="__main__":
    app.run(port=5000)
