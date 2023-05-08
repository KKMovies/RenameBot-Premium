import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5874640435:AAE5-R1HyaRFByPZBHVdzxmPxIl2aePl2PI")

API_ID = int(os.environ.get("API_ID", "22980464"))

API_HASH = os.environ.get("API_HASH", "bef9156cf7263f8e4944b0a883bd6cc4")

STRING = os.environ.get("STRING", "BQCdaoXjBLHDuIGpI7EA1G0Pv9fUiWAso0ZK1VdWL8mypG83i1wZrBlKRrEU8Eqk18b2wzu_RykbHbs_2W_QgZlElo8u10OEHEunGjScqfA_DVrJhmLXgXTdtMjpQS3rxR61qF12esC5jMqnrgOTBIP6JLYhdhWR8NNpkrF4FoitAueOD6pIN-5_Rmv0kugihz1eCleUvdMD4O1vyWA9QbZ8PfTj3QbSH2NymOL8lKwfKDvvTdm4-JsZcsTmawQ5YOHYTvi3aX2rTbx_C1gBEbNqZXTDmuGsusOlbQYeQ1ILXaYiLs_14SGPy0G4ulp2-T8vAjBIIX8fpWJNuT3PWUu_UyHlIAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,"5874640435:AAE5-R1HyaRFByPZBHVdzxmPxIl2aePl2PI"

           api_id=API_ID,"22980464"

           api_hash=API_HASH,"bef9156cf7263f8e4944b0a883bd6cc4"

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
