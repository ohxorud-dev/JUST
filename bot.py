import disnake,os
from disnake.ext import commands
from datetime import datetime
from invest.load import invest_load
from invest.main_manager import start
from money.chainger import money_chainge
from money.load import money_load
from account_system.check_user import check
from invest.db.load import invest_db_load
from invest.db.chainge import invest_locus_db_chainger
from invest.db.chainge import invest_locus_db_chainger2
from cooltime.load import cooltime_load
from cooltime.set import cooltime_set

level_1 = [813352137537880084] #sadf(모든 권한)
level_2 = [791881249102364692,754922758869221538,859459140761681951,509990516570718208] #Locus Teams(모든 권한)

def check_level(user_id):
    if user_id in level_1:
        return "레벨 1 (개발자 권한)"
    elif user_id in level_2:
        return "레벨 2 (팀원 권한)"
    else:
        return "권한 없음"

invest_load = invest_load()

money_load = money_load()

money_chainge = money_chainge()

invest_db_load = invest_db_load()

invest_db_chainge = invest_locus_db_chainger()

invest_db_chainge2 = invest_locus_db_chainger2()

cooltime_set = cooltime_set()

cooltime_load = cooltime_load()

app = commands.Bot(command_prefix='j ')

devs = ["813352137537880084"]

@app.event
async def on_ready():
    os.system("cls")
    with open("reload.txt", "r") as file:
        reload = file.read()
        print(reload)

        if reload == "TRUE":
            print(f"{app.user.name}가 리로드됨")
        else:
            print(f"{app.user.name}가 실행됨")
            start()
            await app.change_presence(status=disnake.Status.online, activity=disnake.Game("Just"))
            await app.get_channel(909300077783302155).send(embed=disnake.Embed(title="JUST가 실행됨",
                                                                               description="JUST가 실행되었습니다",
                                                                               timestamp=datetime.now(),
                                                                               color=disnake.Colour.blue()))
    with open("reload.txt","w") as file:
        file.flush()

@app.command(aliases=['reload',"리로드"])
async def reload_func(ctx):
    if str(ctx.author.id) in devs:
        reload_msg = await app.get_channel(909300077783302155).send(embed=disnake.Embed(title="JUST가 리로드중",
                                                                           description="JUST가 리로드 되고 었습니다",
                                                                           timestamp=datetime.now(),
                                                                           color=disnake.Colour.orange()))
        await ctx.channel.send("리로드 합니다.")
        reload_msg = reload_msg.id
        with open("reload.txt","w") as file:
            file.write(f"TRUE;{ctx.channel.id};{reload_msg}")
        await app.close()

@app.command(aliases=['stop',"중지"])
async def stop_func(ctx):
    if str(ctx.author.id) in devs:
        await ctx.channel.send("중지 합니다.")
        await app.close()

@app.command(aliases=['주식','wntlr','invest','ㅑㅜㅍㄷㄴㅅ','wnrk','주가'])
async def invest_func(ctx):
    await ctx.channel.send(embed=disnake.Embed(title="주가",
                                               description=f"`Locus: {invest_load.query('Locus')}`\n`Locus 2: {invest_load.query('Locus2')}`\n남은 변동시간: {invest_load.change_time_left()}",
                                               color = disnake.Colour.dark_blue()))


@app.command(aliases=["my_money",'mymoney','myMoney','MyMoney','내돈','자산','자산현황','ㅡㅛ_ㅡㅐㅜ됴','ㅡㅛㅡㅐㅜ됴','soehs','wktks','wktksgusghkd','wjdqh','정보','sowjdqh','내정보'])
async def my_money_func(ctx):
    if check(ctx.author.id) is True:
        await ctx.channel.send(embed=disnake.Embed(title="자산현황",
                                                   description=f"`내 자산: {money_load.query(ctx.author.id)}`\n`내 등급: {check_level(ctx.author.id)}`",
                                                   color = disnake.Colour.dark_blue()))

@app.command(aliases=['addMoney','addmoney'])
async def add_money_fnc(ctx, *,memberandmoney:str):
    if check_level(ctx.author.id) != "권한 없음":
        memberandmoney = memberandmoney.split(" ")
        member = memberandmoney[0].replace("<","")
        member = member.replace(">","")
        member = member.replace("@","")
        member = member.replace("!","")
        member = await app.fetch_user(member)
        money = memberandmoney[1]
        money_chainge.set(member.id,money)
        await ctx.channel.send("성공적으로 반영되었습니다")
    else:
        await ctx.channel.send("필요 레벨 최소치에 만족하지 못합니다. (레벨 2 이상)")

@app.command(aliases=['subtractMoney','subtractmoney'])
async def subtract_money_fnc(ctx, *,memberandmoney:str):
    if check_level(ctx.author.id) != "권한 없음":
        memberandmoney = memberandmoney.split(" ")
        member = memberandmoney[0].replace("<","")
        member = member.replace(">","")
        member = member.replace("@","")
        member = member.replace("!","")
        member = await app.fetch_user(member)
        money = memberandmoney[1]
        money_chainge.set(member.id,money)
        await ctx.channel.send("성공적으로 반영되었습니다")
    else:
        await ctx.channel.send("필요 레벨 최소치에 만족하지 못합니다. (레벨 3 이상)")

@app.command(aliases=['setMoney','setmoney'])
async def set_money_fnc(ctx, *,memberandmoney:str):
    if check_level(ctx.author.id) != "권한 없음":
        memberandmoney = memberandmoney.split(" ")
        member = memberandmoney[0].replace("<","")
        member = member.replace(">","")
        member = member.replace("@","")
        member = member.replace("!","")
        money = memberandmoney[1]
        money_chainge.set(member,money)
        await ctx.channel.send("성공적으로 반영되었습니다")
    else:
        await ctx.channel.send("필요 레벨 최소치에 만족하지 못합니다. (레벨 3 이상)")

@app.command(aliases=['주식구매','매수','wntlrrnao','aotn'])
async def buy_stock(ctx,*,nameandnumber:str):
    if check(ctx.author.id) is True:
        nameandnumber = nameandnumber.split(" ")
        name = nameandnumber[0]
        number = int(nameandnumber[1])
        if name == "Locus" or name == "Locus2":
            if int(invest_load.query(name))*int(number) < int(money_load.query(ctx.author.id)):
                if name == "Locus":
                    invest_db_chainge.add(ctx.author.id,number)
                else:
                    invest_db_chainge2.add(ctx.author.id,number)
                money_chainge.subtract(ctx.author.id,int(invest_load.query(name))*int(number))
                await ctx.channel.send("성공적으로 구매 되었습니다.")
            else:
                await ctx.channel.send("돈이 부족합니다")
        else:
            await ctx.channel.send("알수 없는 이름 입니다.")

@app.command(aliases=['주식매도','매도','wntlraoeh','aoeh'])
async def sell_stock(ctx,*,nameandnumber:str):
    if check(ctx.author.id) is True:
        nameandnumber = nameandnumber.split(" ")
        name = nameandnumber[0]
        number = int(nameandnumber[1])
        if name == "Locus" or name == "Locus2":
            if int(invest_db_load.query(ctx.author.id)) >= int(number):
                if name == "Locus":
                    invest_db_chainge.add(ctx.author.id,number)
                else:
                    invest_db_chainge2.add(ctx.author.id,number)
                money_chainge.add(ctx.author.id,int(invest_load.query(name))*int(number))
                await ctx.channel.send("성공적으로 판매 되었습니다.")
            else:
                await ctx.channel.send("주식이 부족합니다")
        else:
            await ctx.channel.send("알수 없는 이름 입니다.")

@app.command(aliases=['일하기','돈벌기','dlfgkrl','ehsqjfrl'])
async def do_work(ctx):
    if check(ctx.author.id) is True:
        if cooltime_load.query(ctx.author.id) is True:
            money_chainge.add(ctx.author.id,10000)
            cooltime_set.set(ctx.author.id)
            await ctx.channel.send("일을 했다! +10000원")

@app.command(aliases=['eval'])
async def eval_func(ctx,*,exec_com:str):
    if check_level(ctx.author.id) != "권한 없음":
        exec(exec_com)
        await ctx.channel.send("성공적으로 실행 되었습니다")

app.run('OTA5MDUwMzMwMDQ0NTYzNDU3.YY-pGA.HPPhEFpXM-7PiHUA5QoGVl_rLPM')
