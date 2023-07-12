import csv


class handleBreathHeartData:
    def __init__(self):
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
        self.csv_init()

    def execute(self, data):
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
            print(e)
        finally:
            self.write_csv()
            self.cleanList()

    def write_csv(self):
        self.swap()
        with open('BreathHeartbeatdata.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for data in self.data_dict.values():
                csv_writer.writerow(data)

    def swap(self):
        with open('BreathHeartbeatdata.csv', 'r', newline='') as csv_file:
            rows = csv.reader(csv_file)
            for row in rows:
                if row[0] in self.data_dict.keys():
                    newdata = self.data_dict[row[0]]
                    self.data_dict[str(row[0])] = row+newdata

    def cleanList(self):
        for data_list in self.data_dict.values():
            data_list.clear()

    def csv_init(self):
        with open('BreathHeartbeatdata.csv', 'w', newline='') as csv_file:
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
