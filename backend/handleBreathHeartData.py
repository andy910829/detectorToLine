import csv
from pymongo import MongoClient
import uuid
import os 

class handleBreathHeartData:
    def __init__(self):
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.db = self.cluster["detector_data"]
        self.collection = self.db["board"]
        self.data_dict = {
            "heart_rate": list(),
            "breath_rate": list(),
            "bodysign_val": list(),
            "distance": list()
        }
        self.datatype_dict = {
            "85": "heart_rate",
            "81": "breath_rate",
            "80": {
                "3": "bodysign_val",
                "4": "distance"
            }
        }
        self.id=str()
        self.csv_file = str()
        self.folder_file = "/var/www/detectorData/"

    def execute(self, data, id):
        self.id = id 
        dir_path = f"{self.folder_file+str(self.id)}"
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        board_info = self.collection.find_one({"board_id": self.id})
        if board_info:
            self.csv_file = board_info["current_csv_file"]
        else:
            file_name = uuid.uuid4()
            self.collection.insert_one({"board_id": self.id, "current_csv_file": self.folder_file+str(self.id)+"/"+str(file_name)+".csv", "CSV_list":[self.folder_file+str(self.id)+"/"+str(file_name)+".csv"]})    
            self.csv_file = self.folder_file+str(self.id)+"/"+str(file_name)+".csv"
        data_type = data[0]
        try:
            if data_type == "80":
                value = int(data[4], 16)
                if data[1] == "4":
                    value = value * 256 + int(data[5], 16)
                self.data_dict[self.datatype_dict["80"][data[1]]].append(value)
            else:
                self.data_dict[self.datatype_dict[data_type]].append(
                    int(data[4], 16))
        except Exception as e:
            pass
        finally:
            self.write_csv()
            self.cleanList()

    def write_csv(self):
        self.swap()
        with open(self.csv_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for data in self.data_dict.values():
                csv_writer.writerow(data)

    def swap(self):
        change_file = False
        try:
            with open(self.csv_file, 'w', newline='') as csv_file:
                rows = csv.reader(csv_file)
                for row in rows:
                    if len(row) == 0:
                        self.csv_init()
                    elif len(row)>500:
                        change_file = True
                    if row[0] in self.data_dict.keys():
                        newdata = self.data_dict[row[0]]
                        self.data_dict[str(row[0])] = row+newdata
            if change_file:
                self.create_new_CSVfile()
        except FileNotFoundError:
            f = open(self.csv_file, 'w', newline='')
            f.close()
        except:
            pass

    def cleanList(self):
        for data_list in self.data_dict.values():
            data_list.clear()

    def create_new_CSVfile(self):
        self.csv_file = self.folder_file+str(self.id)+"/"+str(uuid.uuid4())+".csv"
        self.collection.update_many({"board_id": self.id}, {"$set": {"current_csv_file": self.csv_file},"$push": {"CSV_list": self.csv_file}})
    
    def csv_init(self):
        with open(self.csv_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["heart_rate"])
            csv_writer.writerow(["breath_rate"])
            csv_writer.writerow(["bodysign_val"])
            csv_writer.writerow(["distance"])


# if __name__ == "__main__":
#     handleData = handleData()
#     data = [
#         ["0", "0", "85", "0", "5", "10", "15", "20"],
#         ["0", "0", "85", "03", "6", "11", "16", "21"],
#         ["0", "0", "85", "2", "7", "12", "17", "22"],
#         ["0", "0", "85", "2", "7", "12", "17", "22"],
#         ["0", "0", "85", "3", "8", "13", "18", "23"],
#         ["0", "0", "85", "3", "8", "13", "18", "23"],
#     ]
#     for test_data in data:
#         handleData.execute(test_data)
