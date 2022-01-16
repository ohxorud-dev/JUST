import json

class invest_locus_db_chainger():
    def chainge(self,chainge,to_chainge):
        with open("./invest/db/invest_inven.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = to_chainge

        with open("./invest/db/invest_inven.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def add(self,chainge,add_chainge):
        with open("./invest/db/invest_inven.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = int(money_data[str(chainge)]) + add_chainge

        with open("./invest/db/invest_inven.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def subtract(self,chainge,subtract_chainge):
        with open("./invest/db/invest_inven.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = int(money_data[str(chainge)]) - subtract_chainge

        with open("./invest/db/invest_inven.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def set(self,chainge,set_chainge):
        with open("./invest/db/invest_inven.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = set_chainge

        with open("./invest/db/invest_inven.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)


class invest_locus_db_chainger2():
    def chainge(self,chainge,to_chainge):
        with open("./invest/db/invest_inven2.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = to_chainge

        with open("./invest/db/invest_inven2.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def add(self,chainge,add_chainge):
        with open("./invest/db/invest_inven2.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = int(money_data[str(chainge)]) + add_chainge

        with open("./invest/db/invest_inven2.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def subtract(self,chainge,subtract_chainge):
        with open("./invest/db/invest_inven2","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = int(money_data[str(chainge)]) - subtract_chainge

        with open("./invest/db/invest_inven2.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def set(self,chainge,set_chainge):
        with open("./invest/db/invest_inven2.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = set_chainge

        with open("./invest/db/invest_inven2.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)