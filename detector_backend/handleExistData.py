import csv


class handleExistData:
    def __init__(self):
        self.data_dict = {
            "static_val": list(),
            "dis_static": list(),
            "dynamic_val": list(),
            "dis_move": list(),
            "speed": list()
        }
        self.datatype_dict = {
            4: "static_val",
            5: "dis_static",
            6: "dynamic_val",
            7: "dis_move",
            8: "speed"
        }
        self.limit_dict = {
            4: int("fa", 16),
            5: int("6", 16),
            6: int("fa", 16),
            7: int("8", 16),
            8: int("14", 16)
        }
        self.csv_init()

    def execute(self, data):
        try:
            if data[1] == "7":
                pass
            else:
                for index in range(6, 11):
                    if int(data[index], 16) > self.limit_dict[index]:
                        pass
                    else:
                        self.data_dict[self.datatype_dict[index]].append(
                            int(data[index], 16))
        except Exception as e:
            print(e)
        finally:
            self.write_csv()
            self.cleanList()

    def write_csv(self):
        self.swap()
        with open('humanExistdata.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for data in self.data_dict.values():
                csv_writer.writerow(data)

    def swap(self):
        with open('humanExistdata.csv', 'r', newline='') as csv_file:
            rows = csv.reader(csv_file)
            for row in rows:
                if row[0] in self.data_dict.keys():
                    newdata = self.data_dict[str(row[0])]
                    self.data_dict[str(row[0])] = row+newdata

    def cleanList(self):
        for data_list in self.data_dict.values():
            data_list.clear()

    def csv_init(self):
        with open('humanExistdata.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["speed"])
            csv_writer.writerow(["dis_static"])
            csv_writer.writerow(["static_val"])
            csv_writer.writerow(["dynamic_val"])
            csv_writer.writerow(["dis_move"])


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
