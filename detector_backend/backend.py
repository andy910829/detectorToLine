from flask import Flask, request, abort, jsonify

from sendToLine import sendToLine

app = Flask(__name__)

@app.route('/receiveMsg', methods=["GET","POST"])
def recieveMsg():
    data = request.get_json()
    print(data)
    sendToLine(msg=data['status']).push_msg()
    return jsonify({"status":"ok"})


if __name__ == "__main__":
    app.run()
    #app.run(host="192.168.137.179",port='8000')



