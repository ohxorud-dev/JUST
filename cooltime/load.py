import json,os

class cooltime_load():
    def query(self,query):
        os.chdir("C:/Users/otk12/PycharmProjects/discord/JUST")
        with open("./cooltime/detail.json",'r') as file:
            self.invest_data = json.load(file)
            try:
                return self.invest_data[str(query)] != query.datetime.today().strftime('%m%d')

            except:
                return True

