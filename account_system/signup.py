import json,datetime

class account_signup():
    def signup(self,user_id):
        with open("./account_system/account_list.json","r") as file:
            account_list = json.load(file)

        account_list[user_id] = str(datetime.datetime.today())

        with open("./account_system/account_list.json","w") as file:
            json.dump(account_list,file)

        with open("./money/money.json","r") as file:
            money_list = json.load(file)

        money_list[user_id] = "1000"

        with open("./money/money.json","w") as file:
            json.dump(money_list,file)

        with open("./invest/db/invest_inven.json","r") as file:
            invest_inven = json.load(file)

        invest_inven[user_id] = "0"

        with open("./invest/db/invest_inven2.json","r") as file:
            invest_inven2 = json.load(file)

        invest_inven2[user_id] = "0"

        with open("./invest/db/invest_inven.json","r") as file:
            json.dump(invest_inven,file)

        with open("./invest/db/invest_inven2.json","r") as file:
            json.dump(invest_inven2,file)