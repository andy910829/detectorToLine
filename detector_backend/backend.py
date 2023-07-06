from flask import Flask, request, abort, jsonify

from sendToLine import sendToLine
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('r/rzYv3XXxi2gq1LtxV/n9ZSpTWoUWqlBlqLgvXkR9qP/3hXBl1R1/MFnbtqIu2iEfeS64Ca7ZPF2nPqxSfOgyBIi/+OYC5KXK0Z0vdn04JyR1Opf/rgpbnHRdz2UjffRKOHHSpaZ2wvj2180YHf7gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7e72932a10beff6321e39b813ef4d4f9')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@app.route('/receiveMsg', methods=["GET","POST"])
def recieveMsg():
    data = request.get_json()
    print(data)
    sendToLine(msg=data['status']).push_msg()
    return jsonify({"status":"ok"})

@app.route('/admin',methods=["GET"])
def admin():
    return "<html><body><h1>Admin Page</h1><input/></body></html>"

@app.route('/',methods=["GET","POST"])
def initial():
    return "OK"

if __name__ == "__main__":
    app.run()
    #app.run(host="192.168.137.179",port='8000')



