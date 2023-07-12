import handleBreathHeartData
import handleExistData

class dataInput:
    def __init__(self,data):
        self.breath_serial_data = handleBreathHeartData.handleBreathHeartData()
        self.exist_serial_data = handleExistData.handleExistData()
        self.data = data


    def process_data(self,data):
        # try:
        if data[0] == "08":
            self.exist_serial_data.execute(data)
        else:
            self.breath_serial_data.execute(data)
        # except Exception as e:
        #     print(e)

    def execute(self):
        for data in self.data:
            print(data)
            self.process_data(data)

# serial_data.write_csv()
# ser.close()
# if __name__ == "__main__":
#     dataInput([["80","3","0","1","10","40","54","43","0","1","0","0","0","0","0","0","0","0","0","0"],["80","5","0","4","0","8d","0","5a","1c","54","0","0","0","0","0","0","0","0","0","0"],["80","5","0","4","0","8d","0","5a","1c","54","0","0","0","0","0","0","0","0","0","0"]]).execute()
