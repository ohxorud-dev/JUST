import json,os

class invest_db_load():
    def query(self,query):
        os.chdir("C:/Users/otk12/PycharmProjects/discord/JUST")
        with open("./money/money.json",'r') as file:
            money_data = json.load(file)
            return money_data[str(query)]