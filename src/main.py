import os
import discord
import wrapper
from discord.ext import commands
import wikipediaapi
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix='-', )


# Anime search
@bot.command(name="anime")
async def animesearch(ctx, *args):
    res = wrapper.jikan.search_anime(" ".join(args))
    # pylint: disable=no-member #type:ignore
    sendStr = f""" 
    **Title** : {res["title"]}
synopsis : {res["synopsis"]}
__{res["url"]}__
**score: {res["score"]}**
**episodes : {res["episodes"]}**
    """
    await ctx.reply(sendStr)


# Manga search
@bot.command(name="manga")
async def mangasearch(ctx, *args):
    res = wrapper.jikan.search_manga(" ".join(args))
    # pylint: disable=no-member type:ignore
    sendStr = f"""
    **{res["title"]}**\n
{res["synopsis"]}
__{res["url"]}__
**score: {res["score"]}**
**chapters : {res["chapters"]}**
    """
    await ctx.reply(sendStr)


@bot.command(name="wiki")
async def wikisearch(ctx, *args):
    wikisearch = wikipediaapi.Wikipedia('en')
    search_res = wikisearch.page(" ".join(args))
    if search_res.exists():
        await ctx.reply(
            f'**{search_res.title}**\n{search_res.summary[0:400]}...\n**read full at : {search_res.fullurl}**'
        )
    else:
        await ctx.reply("Page not found")


# Test command
@bot.command(name="goodbot")
async def goodbot(ctx, *args):
    if args.count("alien") >= 1:
        await ctx.reply(
            "**Hab U seen a alien pls** \n\n https://www.youtube.com/watch?v=EtxBvU21J28",
            mention_author=True)
    else:
        await ctx.send("Yes! :)")


bot.run(BOT_TOKEN)
