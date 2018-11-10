import discord
import random
import re
import asyncio
import datetime
import time
import threading
import yaml
from time import sleep
from datetime import datetime
from discord.ext import commands

client = commands.Bot('ry!')

YML_DATA = './data/data.yml'

@client.listen('on_message')
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user or message.author.bot:
        return

    if message.content.startswith('こんにちは！'):
        msg = '{0}さん、こんにちは！'.format(message.author.display_name)
        await message.channel.send(msg)

    if message.content.startswith('おやすみ！'):
        msg = '{0}さん\nおやすみなさい！\n明日も来てください！'.format(message.author.display_name)
        await message.channel.send(msg)

    if message.content.startswith('じゃねバイ'):
        msg = '{0}さん\nさようなら！\nまた後で来てくれ！！'.format(message.author.display_name)
        await message.channel.send(msg)

    if message.content.startswith('ただいまぁ'):
        msg = '{0}さん\nおかえり！\nお風呂にする？ご飯にする？\nそれとも...た、わ、し？'.format(message.author.display_name)
        await message.channel.send(msg)

    if message.content.startswith('帰ったぁ'):
        msg = '{0}さん\nおかえり\nお風呂にしやすか？\nご飯にしやすか？\nそれとも・・・サイコパス？'.format(message.author.display_name)
        await message.channel.send(msg)

    #BOTのアイコン表示
    if message.content.startswith('君のアイコン見せて！'):
        embed = discord.Embed(title='私のアイコンです。',colour=0x0000ff)
        embed.set_image(url=client.user.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith('面白い曲お願い！'):
        fun = ['https://www.youtube.com/watch?v=VfdigdNWkb0', 'https://www.youtube.com/watch?v=LZnwKq-kbbA', 'https://www.youtube.com/watch?v=MYqT3SOtQro','https://www.youtube.com/watch?v=4D4O3RJsAjA&t=4s','https://www.youtube.com/watch?v=mBqZT35qDic']
        await message.channel.send( random.choice(fun))

    if message.content.startswith('いい曲教えて！'):
        good = ['https://www.youtube.com/watch?v=9aJVr5tTTWk',
          'https://www.youtube.com/watch?v=arSkpLlofGQ',
          'https://www.youtube.com/watch?v=qaQP0efeAQQ',
          'https://www.youtube.com/watch?v=H51Xj5aEgkA',
          'https://www.youtube.com/watch?v=od8CNHDkIJA',
          'https://www.youtube.com/watch?v=2hTnAKvnDrA',
          'https://www.youtube.com/watch?v=KmvYJtdJoEw',
          'https://www.youtube.com/watch?v=j0e9dESM60c',
          'https://www.youtube.com/watch?v=w9V3x61D994',
          'https://www.youtube.com/watch?v=MslES96hLeo',
          'https://www.youtube.com/watch?v=q9iozQDEO_U',
          'https://www.youtube.com/watch?v=gsVGf1T2Hfs',
          'https://www.youtube.com/watch?v=d6QEOFjqHcM']
        await message.channel.send( random.choice(good))

    if message.content.startswith('オススメのBGM教えて！'):
        recommendation = ['https://www.youtube.com/watch?v=VR1H9njDd9w', 
        'https://www.youtube.com/watch?v=n8X9_MgEdCg', 
        'https://www.youtube.com/watch?v=3fxq7kqyWO8',
        'https://www.youtube.com/watch?v=B7xai5u_tnk',
        'https://www.youtube.com/watch?v=kL8CyVqzmkc',
        'https://www.youtube.com/watch?v=YqrxIimmiqs',
        'https://www.youtube.com/watch?v=kzr5RQE0tZs']
        await message.channel.send( random.choice(recommendation))

    if message.content.startswith('トガちゃんの画像くれ！'):
        plese = ['https://cdn.discordapp.com/attachments/457827767707238411/486475315171033097/2ab09638ac4010d5.jpg',
        'https://cdn.discordapp.com/attachments/457827767707238411/486475474583683072/18.jpg',
        'https://cdn.discordapp.com/attachments/457827767707238411/486475571748929537/11.jpg',
        'https://cdn.discordapp.com/attachments/457827767707238411/486475676682027008/2.jpg']
        await message.channel.send( random.choice(plese))

    #BOTに喋らせるコマンド(DM用)
    global channel
    if isinstance(message.channel,discord.DMChannel) and message.author.id == 433868838707396628:
        if message.content.startswith('!?ch'):
            split = message.content.split()
            channel = client.get_channel(int(split[1]))
            await message.channel.send('{0}に設定しました！'.format(channel.mention))
        else:
            await channel.send(message.content)

    #ユーザーアイコン
    if message.content.startswith('r!icon'):
        embed = discord.Embed(title='{0}のアイコン'.format(message.author.display_name),colour=0x0000ff)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    #通知オン役職を付けるコマンド
    if message.content.startswith('r!on'):
        role = message.guild.get_role(508155004922626058)
        await message.author.add_roles(role)
        await message.channel.send('通知オンを付けました！')

    if message.content.startswith('r!developer'):
        role = message.guild.get_role(505803681774567424)
        await message.author.add_roles(role)
        await message.channel.send('BOTdeveloperを付けました！')

    #通知オン役職を外すコマンド
    if message.content.startswith('r!off'):
        role = message.guild.get_role(508155004922626058)
        await message.author.remove_roles(role)
        await message.channel.send('通知オンを外しました。')

    #if message.content == (''):
    #    await message.delete()
    #    member = message.author
    #    await member.ban(reason='暴言を言ったためBANです',delete_message_days=1)
    #    await message.channel.send('不適切な発言はやめてください。')

    if message.content == ('死ね'):
        await message.delete()
        await message.channel.send('不適切な発言はやめてください。')

    #特定のメッセージを消すコマンド(delete)
    if message.content == ('r!invite'):
        await message.delete()

    #招待リンク取得用コマンド
    if message.content.startswith('r!invite'):
        embed = discord.Embed(title='**INVITE-LINK**',description='[私の招待リンクです！](https://discordapp.com/api/oauth2/authorize?client_id=485053429983608853&permissions=8&scope=bot)',colour=0x53b3dd)
        embed.add_field(name='あなたのサーバーにも、ぜひ入れてみてください！',value='入れるためにはそのサーバーの管理者権限が必要です。\n[このBOTのサポートサーバー](https://discord.gg/BF5pVqD)')
        await message.channel.send(embed=embed)

    #特定の人に役職を付けるコマンド
    splietd = message.content.split()
    if splietd[0] == 'l!':
        member = message.author
        role = message.guild.get_role(499214282110664714)
        if role in member.roles:
            member = message.guild.get_member(int(splietd[1]))
            role = message.guild.get_role(499214328206196736)
            role1 = message.guild.get_role(499214651024736265)
            await member.add_roles(role,role1)

    #時刻表示
    if message.content.startswith('r!time'):
        now = datetime.datetime.now()
        embed = discord.Embed(title='今の日時',description='今の日時は\n**{0:%Y.%m/%d %p.%I:%M:%S}**です。'.format(now),colour=0x00ff67)
        await message.channel.send(embed=embed)

    #help表示コマンド
    if message.content.startswith('r!help'):
        embed = discord.Embed(title='**コマンド一覧**',description='\nこんにちは！\nおやすみ！\nじゃねバイ\nただいまぁ\n帰ったぁ\n君のアイコン見せて！\n面白い曲お願い！\nいい曲教えて！\nオススメのBGM教えて！\nトガちゃんの画像くれ！',colour=0x0000ff)
        embed.add_field(name='**サーバーステータス**',value='ry!server')
        embed.add_field(name='**ユーザー情報**',value='r!user')
        embed.add_field(name='**BOT更新情報**',value='r!updates')
        embed.add_field(name='**ユーザーアイコン表示**',value='r!icon')
        embed.add_field(name='**現在の日時**',value='r!time')
        embed.add_field(name='**BOTのバージョン表示**',value='ry!version')
        embed.add_field(name='**ryuu´sBOT-Community専用コマンド表示**',value='r!Shelp')
        embed.add_field(name='**BOTの招待**',value='r!invite')
        await message.channel.send(embed=embed)

    #サポートサーバー限定helpコマンド
    if message.content.startswith('r!Shelp'):
        embed = discord.Embed(title='**ryuu´sBOT-Community専用コマンド**',description='このコマンドは[**ryuu´sBOT-Community**](https://discord.gg/BF5pVqD)専用のコマンドです',colour=0x0000ff)
        embed.add_field(name='**役職付与、剥奪**',value='__**通知オン**__\n**付与：**r!on\n**剥奪：**r!off\n__**BOTdeveloper**__\n**付与：**r!developer')
        embed.add_field(name='**アカウント登録**',value='ry!agree')
        await message.channel.send(embed=embed)

    #更新情報
    if message.content.startswith('r!updates'):
        embed = discord.Embed(title='**ryuuBOTの更新情報**',description='BOTのアイコンをクリスマスバージョンに変更しました。',colour=0x00ffff)
        embed.add_field(name='**今後のアップデート情報**',value='サーバー情報に、そのサーバーの招待コードを加えようと思っています。')
        await message.channel.send(embed=embed)

    # user info
    if message.content.startswith('r!user'):
        if(message.author.status == discord.Status.online):
            status = "オンライン"
        elif(message.author.status == discord.Status.offline or message.author.status == discord.Status.invisible):
            status = "オフライン"
        elif(message.author.status == discord.Status.dnd or message.author.status == discord.Status.do_not_disturb):
            status = "起こさないで"
        elif(message.author.status == discord.Status.idle):
            status = "退席中"
        else:
            status = "その他"

        # ニックネームの有無で分岐
        if(message.author.nick != None):
            embed = discord.Embed(title='Userinfo',
            description='名前: ' + message.author.name + '\nニックネーム: ' + message.author.nick + 
            '\nアカウント作成日: ' + str(message.author.created_at) + '\nサーバ参加日: ' + str(message.author.joined_at) + '\n現在のステータス: ' + status,
            colour=0x2ea9ff)
        else:
            embed = discord.Embed(title='Userinfo',
            description='名前: ' + message.author.name + '\nアカウント作成日: ' + str(message.author.created_at) +
            '\nサーバ参加日: ' + str(message.author.joined_at) + '\n現在のステータス: ' + status
            ,colour=0x2ea9ff)
        await message.channel.send(embed=embed)

with open(YML_DATA) as stream:
    data = yaml.load(stream)
    greeting = data["greeting"]

loop = asyncio.get_event_loop()
client.loop.create_task(greeting_schedule(client.get_channel(greeting),loop))


async def on_greeting(channel):
    embed = discord.Embed(title='21:00になりました',colour=0x2ea9ff)
    await channel.send(embed=embed)

# 挨拶を実行する
@asyncio.coroutine
async def greeting_schedule(channel, loop):
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='21:00:00':
            await on_greeting(channel)

#BOTのバージョン管理
@client.command()
async def version(ctx):
    v = '**1.12.1**'
    embed = discord.Embed(title='**ryuuBOTの現在のバージョン**',colour=0x0000ff, description=f'{v}v')
    await ctx.send(embed=embed)

# サーバステータス表示
@client.command()
async def server(ctx):
    guild = ctx.guild
    description = '''
    **Server NAME:**{0.name}
    **Server OWNER:**{0.owner.mention}
    **Server MEMBER:**{0.member_count}
    **チャンネルの数:**{1}
    **役職の数:**{2}
    **サーバーが作成された日:**{0.created_at}
    **Server ID:**{0.id}
    '''.format(guild, len(guild.channels),len(guild.roles))
    embed = discord.Embed(title='サーバー情報', description=description,colour=0x0000ff)
    embed.set_thumbnail(url=guild.icon_url)
    await ctx.send(embed=embed)

#BAN,BAN解除コマンド
#@client.command()
#async def on_member_ban(guild, user):
#    splietd = message.content.split()
#    if splietd[0] == 'r!ben':
#        member = message.author
#        await member.ban(reason='迷惑行為をしたためBANされました')

#@client.command()
#async def on_member_unban(guild, user):
#    splietd = message.content.split()
#    if splietd[0] == 'r!unban':
#        member = message.author
#        await member.unban()

#アカウント登録コマンド
@client.command()
async def agree(ctx):
    ユーザー = ctx.guild.get_role(451411887448391691)
    if ユーザー not in ctx.author.roles:
        # 送信する文章指定。
        content = """
{0}さんの
アカウントが登録されました！
まずは<#505807427279519769>で自己紹介をしてください！
""".format(ctx.author.mention)
        # ユーザーのメンションに置き換える
        # 役職付与
        await ctx.author.add_roles(ユーザー)
        # メッセージ送信
        await ctx.send(content)
    else:
        await ctx.send('登録終わってるじゃん')

#入退出メッセージ
@client.event
async def on_member_join(member):
    if 'discord.gg' in member.display_name:
        await member.ban(reason='招待リンクが、名前に含まれていたため、BANされました', delete_message_days=1)
    name = member.display_name
    now = datetime.datetime.now()
    embed = discord.Embed(title='{0}さんがサーバーに参加しました！'.format(name),colour=0x2ea9ff,description='ようこそ{0}さん！\nよろしくお願いします！！\nこのサーバーの現在の人数は{1}人です。\n{2}に作られたアカウントです。'.format(name,member.guild.member_count,member.created_at))
    embed.add_field(name='入室時間',value='{0:%p.%H:%M:%S}'.format(now))
    embed.set_thumbnail(url=member.avatar_url)
    channel = next(c for c in member.guild.channels if c.name == '雑談')
    await channel.send(embed=embed)


@client.event
async def on_member_remove(member):
    name = member.display_name
    now = datetime.datetime.now()
    embed = discord.Embed(title='{0}さんが退出しました。'.format(name),colour=0x2ea9ff,description='{0}さん、ご利用下さりありがとうございました。\nこのサーバーの現在の人数は{1}人です。'.format(name,member.guild.member_count))
    embed.add_field(name='退出時間',value='{0:%p.%H:%M:%S}'.format(now))
    embed.set_thumbnail(url=member.avatar_url)
    channel = next(c for c in member.guild.channels if c.name == '雑談')
    await channel.send(embed=embed)

@client.event
async def on_ready():
    print('ログインしました！')
    await client.change_presence(activity=discord.Activity(name='r!helpでコマンド一覧を見れます！',type=discord.ActivityType.playing))
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDg1MDUzNDI5OTgzNjA4ODUz.DsWM_A.wiuybGnfXbY_tuQVlghotymRKkY')