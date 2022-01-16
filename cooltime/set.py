import json,datetime

class cooltime_set():
    def set(self,chainge):
        with open("./cooltime/detail.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = datetime.datetime.today().strftime('%m%d')

        with open("./cooltime/detail.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)