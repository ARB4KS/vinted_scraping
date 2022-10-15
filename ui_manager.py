from discord.ui import Button, View
import asyncio
from discord.ext import tasks, commands
import discord


def make_embed(database,request,loop):
    message = discord.Embed()
    embed = discord.Embed(title=database["title"][loop], url=database["url"][loop])
    embed.set_image(url=request.json()["items"][loop]["photo"]["url"])
    embed.description = "**" + database["brand_title"][loop] + "** " + database["price"][loop] + "€" + "/" + \
                         database["size_title"][loop]
    return embed

def buttons (database,loop):
    str_id = "id"
    view = View()
    button1 = Button(label="Détails", style=discord.ButtonStyle.link, url=database["url"][loop])
    button2 = Button(label="Buy", style=discord.ButtonStyle.link,
                     url=f"https://www.vinted.fr/checkout?transaction_id={database[str_id][loop]}")
    view.add_item(button1)
    view.add_item(button2)
    return view