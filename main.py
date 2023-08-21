import discord   #discord API içe aktarıyoruz
import os
from dotenv import load_dotenv
import requests
import json
import openai

load_dotenv()  # .env dosyasındaki çevresel değişkenleri yükler
intents = discord.Intents.default() 
client = discord.Client(intents=intents)  #discord istemcisi oluşturuyoruz.
# botun discord ile iletişim kurmasını sağlayacak nesnedir.



@client.event #on ready on on message gibi olaylara bot tepki 
#versin diye yazdım.
async def on_ready():
    print("{0.user} isimli bot'a bağlanıldı ".format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:#eğer mesajı yazan başka
        #bir bot ise cevap verme.
        return
    
    if message.content.startswith("$merhaba"):
        await message.channel.send("$merhaba!")
    
    

client.run(os.getenv("TOKEN"))