import json
import time
import requests as req
from ui_manager import make_embed,buttons
import cloudscraper
import pandas as pd
from pyVinted import Vinted
import webbrowser
import discord
from discord.utils import get
from discord.ext import commands
from discord.ui import Button, View
import asyncio
from discord.ext import tasks, commands
import discord
from database import *



vinted = Vinted()

items = vinted.items.search("https://www.vinted.fr/vetement?order=newest_first&price_to=60&currency=EUR",10,1)
scraper = cloudscraper.create_scraper()

embed = discord.Embed()
continue_running = True
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'
 }
r = scraper.get('https://www.vinted.fr')
#TOKEN="Ae9SZJbYXtAW78gT_p3xuWqyLmFrv-72"
TOKEN="MTAyOTY0MDg1NTMxODk2MjIzOA.GgVt_A.ENopuoz_yudpXMbLm2e1uHOGvL37B-MpPGCa1E"
intents = discord.Intents.all()
intents.members= True
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" )

user =discord.Client(intents=discord.Intents.all())
# async def background():
#    await user.wait_until_ready()
#    channel = client.get_channel(int(1029645377273606174))
#    await channel.send("Test")
#
# asyncio.run(background())

#
#
#

#


# # print(r.headers)
# r = scraper.get('https://www.vinted.fr/api/v2/catalog/items?catalog_ids=4&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&is_for_swap=0&page=1&per_page=899')
# # we can inspect the json response with print(r.json()), and we can only keep what we need
# # for demo purposes, let's print out the full normalized json dataframe
# df = pd.json_normalize(r.json()['items'])
def get_channel():
    channel = client.get_channel(1029645377273606174)
    print(channel)
    return channel

@client.event
async def on_ready():
    channel = client.get_channel(1029645377273606174)
    nike = scraper.get('https://www.vinted.fr/api/v2/catalog/items?catalog_ids=79&color_ids=&brand_ids=53&size_ids=&material_ids=&status_ids=&price_to=20&order=newest_first&is_for_swap=0&page=1&per_page=10')
    ralph_lauren = scraper.get('https://www.vinted.fr/api/v2/catalog/items?catalog_ids=79&color_ids=&brand_ids=88&size_ids=&material_ids=&status_ids=&price_to=25&order=newest_first&is_for_swap=0&page=1&per_page=10')
    nike_df = pd.json_normalize(nike.json()['items'])
    rl_df = pd.json_normalize(ralph_lauren.json()['items'])
    print(ralph_lauren.json()["items"])




    str_id = "id"
    for loop in range(10):

        embed = make_embed(nike_df, nike, loop)
        embed2 = make_embed(rl_df,ralph_lauren,loop)
        button = buttons(nike_df,loop)
        button2 = buttons(rl_df,loop)

        await channel.send(embed=embed)
        await channel.send(view=button)
        await channel.send(embed=embed2)
        await channel.send(view=button2)

# @client.event
# async def get_carhartt():
#     channel = client.get_channel(1029645377273606174)
#     if len(carharrt) > 0:
#         for loop in carharrt:
#             print(loop.title)
#             view = View()
#             button1 = Button(label="Détails", style=discord.ButtonStyle.link, url=loop.url)
#             button2 = Button(label="Buy", style=discord.ButtonStyle.link,
#                              url=f"https://www.vinted.fr/checkout?transaction_id={loop.id}")
#             view.add_item(button1)
#             view.add_item(button2)
#             embed = discord.Embed(title=loop.title, url=loop.url)
#
#             print(loop.price)
#             print(loop.title)
#             embed.description = f"{loop.price}€/{loop.size_title}"
#             embed.set_image(
#                 url=loop.photo)
#             await asyncio.sleep(1)
#             await channel.send(embed=embed)
#             await channel.send(view=view)
#
#
@client.command(pass_context=True)

async def start_bot(ctx):

    posts = []
    channel = client.get_channel(1029645377273606174)
    pulls_channel =client.get_channel(1029776624784252968)
    while continue_running == True:
        time.sleep(3)
        carharrt = vinted.items.search(
            "https://www.vinted.fr/vetements?currency=EUR&search_id=6610073971&order=newest_first&price_to=40.00&brand_id[]=872289&catalog[]=583&size_id[]=208&size_id[]=209",
            10, 1)
        pulls = vinted.items.search("https://www.vinted.fr/vetements?brand_id[]=53&brand_id[]=88&brand_id[]=304&brand_id[]=73952&brand_id[]=255&brand_id[]=362&brand_id[]=872289&catalog[]=79&price_to=30&currency=EUR&order=newest_first")
        if len(pulls) > 0:
            for loop in pulls:


                if loop.id not in posts:
                    posts.append(loop.id)
                    view = View()
                    button1 = Button(label="Détails", style=discord.ButtonStyle.link, url=loop.url)
                    button2 = Button(label="Buy", style=discord.ButtonStyle.link,
                                     url=f"https://www.vinted.fr/checkout?transaction_id={loop.id}")
                    view.add_item(button1)
                    view.add_item(button2)
                    embed = discord.Embed(title=loop.title, url=loop.url)

                    print(loop.price)
                    print(loop.title)
                    embed.description = f"{loop.price}€/{loop.size_title}/{loop.brand_title}"
                    embed.set_image(
                        url=loop.photo)
                    await asyncio.sleep(1)
                    await pulls_channel.send(embed=embed)
                    await pulls_channel.send(view=view)
                    time.sleep(2)
                else:
                    print("rien")
                    time.sleep(2)

        if len(carharrt) > 0:
            for loop in carharrt:

                if loop.id not in posts:
                    posts.append(loop.id)
                    print(loop.title)
                    view = View()
                    button1 = Button(label="Détails", style=discord.ButtonStyle.link, url=loop.url)
                    button2 = Button(label="Buy", style=discord.ButtonStyle.link,
                                     url=f"https://www.vinted.fr/checkout?transaction_id={loop.id}")
                    view.add_item(button1)
                    view.add_item(button2)
                    embed = discord.Embed(title=loop.title, url=loop.url)

                    print(loop.price)
                    print(loop.title)
                    embed.description = f"{loop.price}€/{loop.size_title}/{loop.brand_title}"
                    embed.set_image(
                        url=loop.photo)
                    await asyncio.sleep(1)
                    await channel.send(embed=embed)
                    await channel.send(view=view)
                    time.sleep(2)
                else:
                    print("Rien")
                    time.sleep(2)

@client.command(pass_context=True)
async def setup_notification(ctx):
    user_id = ctx.message.author.id
    content = str(ctx.message.content).split()
    add_notified_user(user_id,content[1],content[2])





client.run(TOKEN)
