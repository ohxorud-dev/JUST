from account_system.signup import account_signup
import json

def check(user_id):

    signup = account_signup()

    with open("./account_system/account_list.json") as file:
        account_list = json.load(file)

    for account in account_list:
        if str(account) == str(user_id):
            return True

    signup.signup(user_id)
    return False

    del signup