import pymongo

class userInit:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['user']
        self.collection = self.db['userInfo']

    