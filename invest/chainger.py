import json,random,time,os
from invest.load import invest_load

load = invest_load()

def main():
    Locus_price = None
    Locus2_price = None
    os.chdir("C:/Users/otk12/PycharmProjects/discord/JUST")
    with open("./invest/invest_detail.txt", "r") as invest_data:
        invest_data = invest_data.read()

    print(f"invest_data: {invest_data}")
    for name in ["Locus","Locus2"]:
        print(name)
        load.query_name = name
        now_price = load.query(name)
        print(now_price)
        now_price = get_price(now_price)
        if (name == "Locus"):
            Locus_price = now_price
        elif (name == "Locus2"):
            Locus2_price = now_price
    
    os.chdir("C:/Users/otk12/PycharmProjects/discord/JUST")
    with open("./invest/invest_detail.txt","w+") as dump_file:
        dump_file.flush()
        dump_file.write(f"{Locus_price};{Locus2_price}")


    wait(60)

def wait(now_time):
    time.sleep(1)
    with open("./invest/change_time.txt","w+") as file:
        file.flush()
        file.write(str(now_time))
    file.close()
    if (now_time <= 0): return 0
    else: return wait(now_time-1)

def get_price(val):

    # 퍼온것으로 의심 될까봐 적습니다
    # 이것은 퍼온것이 아닌 제가 저번에 루카님이 주식 알고리즘 만들어 달라고 했을때 만든것을 가져온것 입니다.
    # (DM에 기록 있음 11.19일경)


    val = int(val)
    up_down = random.randint(0, 1)
    change_min = 0;  # 1회 최소 변동가 (0추천)
    change_max = 100;  # 1회 최대 변동가 (100 주변 추천)

    if val < 1789:
        up_down = 0
    elif val > 32578:
        up_down = 1

    if up_down == 0:
        val += random.randint(change_min, change_max)
    if up_down == 1:
        val -= random.randint(change_min, change_max)

    return val