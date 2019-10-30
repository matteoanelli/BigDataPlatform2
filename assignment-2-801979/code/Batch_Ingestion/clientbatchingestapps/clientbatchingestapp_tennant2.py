
# read the input data

import sys, os
import csv
import pymongo

class sourceIngestion:
    def __init__(self, part_id, ts_date, ts_time, room):
        self.part_id = int(part_id)
        self.ts_date = int(ts_date)
        self.ts_time = ts_time
        self.room = room

    def map(self):
        data = {
            'part_id': self.part_id,
            'ts_date': self.ts_date,
            'ts_time': self.ts_time,
            'room': self.room
        }
        return data

client = pymongo.MongoClient(os.environ.get('MONGO_URL'))
db = client.get_database('test')
records = db.documents

with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]
insert = []
for i in data:
    line = sourceIngestion(*i)
    insert.append(line.map())

records.insert_many(insert)

os.remove(sys.argv[1])
