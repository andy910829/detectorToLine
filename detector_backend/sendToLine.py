import requests
import json


class sendToLine:
    def __init__(self,msg):
        self.msg = msg
        self.headers = {'Authorization': 'Bearer NLeJnartwjIp9qYn1CKzFL+l3ttMZa18YoEcsLfsOqdVpPk94MEvVNCGVXmjq3xbRAY2HfwOpHalKtZTxwDRfQTriBUwq3L7T0VSgdO+DtD5taMsIE5wFgfxwiGGaXAthIAjcpAXXIcvDS7CEkDlNAdB04t89/1O/w1cDnyilFU=',
                        'Content-Type': 'application/json'}
        self.body = {
            'to': 'Uaf01ae08be3ed19057a3e781a105f444',
            'messages': [{
                'type': 'text',
                'text': msg
            }]
        }

    def push_msg(self):
        requests.post('https://api.line.me/v2/bot/message/push',
                       headers=self.headers, data=json.dumps(self.body).encode('utf-8'))

if __name__ == "__main__":
    sendToLine().push_msg()