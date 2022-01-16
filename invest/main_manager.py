import threading
from invest.chainger import main

def start():
    chainger_thread = threading.Thread(target=main)
    chainger_thread.start()