import disnake
from datetime import datetime
from disnake.ext import commands

app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print(f"{app.user.name}가 종료됨")
    await app.change_presence(status=disnake.Status.online, activity=disnake.Game("Just"))
    await app.get_channel(909300077783302155).send(embed=disnake.Embed(title="JUST가 종료됨",
                                                                       description="JUST가 종료되었습니다",
                                                                       timestamp=datetime.now(),
                                                                       color=disnake.Colour.red()))
    exit()

app.run('OTA5MDUwMzMwMDQ0NTYzNDU3.YY-pGA.HPPhEFpXM-7PiHUA5QoGVl_rLPM')