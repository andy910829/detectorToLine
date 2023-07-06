import requests
import json


class sendToLine:
    def __init__(self,msg, token=''):
        self.msg = msg
        self.token = token
        self.headers = {'Authorization': 'Bearer r/rzYv3XXxi2gq1LtxV/n9ZSpTWoUWqlBlqLgvXkR9qP/3hXBl1R1/MFnbtqIu2iEfeS64Ca7ZPF2nPqxSfOgyBIi/+OYC5KXK0Z0vdn04JyR1Opf/rgpbnHRdz2UjffRKOHHSpaZ2wvj2180YHf7gdB04t89/1O/w1cDnyilFU=',
                        'Content-Type': 'application/json'}
        self.body = {
            'to': 'U33dcbe139d669eb71298956ab6e24a08',
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