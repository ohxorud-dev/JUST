import time,os
import global_settings

class invest_load():
    def __init__(self):
        self.query_name = None

    def query(self,query_name=None):
        self.query_name = query_name

        if self.query_name is None: #오류 방지
            return None;

        with open("./invest/invest_detail.txt","r") as invest_data:
            self.invest_data = invest_data #함수 내의 변수로 지정
            del invest_data #에러 방지용 메모리 영구삭제
            self.invest_data = self.invest_data.read()
            self.invest_data = self.invest_data.split(";")
            if (query_name == "Locus"):
                return self.invest_data[0]
            elif (query_name == "Locus2"):
                return self.invest_data[1]
    def change_time_left(self):
        with open("./invest/change_time.txt", "r") as lefttime:
            return lefttime.read()

