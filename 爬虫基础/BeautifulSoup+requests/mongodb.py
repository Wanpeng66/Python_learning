#  python 操作mongodb
import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("127.0.0.1",port=27017)
    testDb = client.testDb
    collection = testDb.qa
    collection.insert({"username":"wp"})

