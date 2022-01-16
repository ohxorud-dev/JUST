import json

class money_chainge():

    def chainge(self,chainge,to_chainge):
        with open("./money/money.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = to_chainge

        with open("./money/money.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def add(self,chainge,add_chainge):
        with open("./money/money.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = int(money_data[str(chainge)]) + int(add_chainge)

        with open("./money/money.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def subtract(self,chainge,subtract_chainge):
        with open("./money/money.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = int(money_data[str(chainge)]) - int(subtract_chainge)

        with open("./money/money.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)

    def set(self,chainge,set_chainge):
        with open("./money/money.json","r") as file:
            money_data = json.load(file)

        money_data[str(chainge)] = set_chainge

        with open("./money/money.json", 'w+') as file:
            file.flush()
            json.dump(money_data,file)