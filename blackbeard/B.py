import discord
import sys
import time
from pytube import YouTube
from pytubemp3 import YouTube
import tracemalloc

tracemalloc.start()


client = discord.Client()
@client.event
async def on_ready():
    print('prefix = +')
    activity = discord.Activity(name='YouTube', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)



@client.event
async def on_message(message):
    #message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content == '+commands':
        channel = client.get_channel(736569645011566613)
        await channel.send('+who \n+help \n+download')
    if message.content == '+who':
        channel = client.get_channel(736569645011566613)
        await channel.send('Im Capt.Blackbeard. Here to Help You with your video and music Pirating needs!')
    if message.content == '+help':
        channel = client.get_channel(736569645011566613)
        await channel.send('Type +download to get started')

    elif message.content == '+download':
        channel = client.get_channel(736569645011566613)
        await channel.send('Summoning Blackbeard...')
        await message.channel.send('Enter Link: ')
        youtube_link = await client.wait_for('message')
        await message.channel.send('Enter Format: ')
        form = await client.wait_for('message')
        url_entry  = youtube_link.content
        format = form.content
        await message.channel.send('\nFile Found!!! \nStand-By For Download...')
        try:
            if format=='MP4':
                yt_obj = YouTube(url_entry) 
                filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
                filters.get_highest_resolution().download()
            else:
                yt_obj = YouTube(url_entry) 
                YouTube(url_entry).streams.filter(only_audio=True).first().download()
            await message.channel.send('Downloading....')
            await message.channel.send('File Downloaded Successfully')
        except Exception as e:
            print(e)


client.run('NzYyMzQ3MzE4OTEyNzQ1NDcy.X3n1RA.zBppz2WUgWcjfCQRLMZgY4bcF7Q')
