import handleBreathHeartData
import handleExistData

class dataInput:
    def __init__(self,data,id):
        self.breath_serial_data = handleBreathHeartData.handleBreathHeartData()
        self.exist_serial_data = handleExistData.handleExistData()
        self.data = data
        self.id = id


    def process_data(self,data):
        # try:
        if data[0] == "8":
            self.exist_serial_data.execute(data,self.id)
        else:
            self.breath_serial_data.execute(data,self.id)
        # except Exception as e:
        #     print(e)

    def execute(self):
        for data in self.data:
            self.process_data(data)

# serial_data.write_csv()
# ser.close()
if __name__ == "__main__":
    dataInput([["80","3","0","1","10","40","54","43","0","1","0","0","0","0","0","0","0","0","0","0"],["80","5","0","4","0","8d","0","5a","1c","54","0","0","0","0","0","0","0","0","0","0"],["80","5","0","4","0","8d","0","5a","1c","54","0","0","0","0","0","0","0","0","0","0"]],"labby").execute()
