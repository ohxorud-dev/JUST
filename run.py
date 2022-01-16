import os

def run_bot():
    os.system("py bot.py")

def bot_shutdown():
    os.system(f"py shutdown_bot.py")

run_bot()

with open("reload.txt","r") as file:
    reload = file.read()
    reload = reload.split(";")
    if reload == "TRUE":
        run_bot()
    else:
        bot_shutdown()
