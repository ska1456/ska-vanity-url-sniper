# IMPORTS
from datetime import datetime
from threading import Thread
from colorama import Fore
import requests
import psutil
import json

# Title : ska - Discord Vanity Sniper
# Date : 31/12/2021
# Author https://github.com/ska1456

# VARIABLES



with open('config.json') as config_file:
	config = json.load(config_file)

token = config["token"]
webhook = config["webhook_url"]

headers = {"authorization": token,
               "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

datetime = datetime.now().strftime('[On %Y-%m-%d @ %H:%M:%S]')
cpu_usage = psutil.cpu_percent()
ram_usage = psutil.virtual_memory().percent



# FUNCTIONS



def start():
	print(f"""
         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
   *  .  . *       *    .        .        .   *    ..  *    *            .      *   *         *   *    .  *      .        .  *   .
 .    *        .        .      .        .            *         *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
    *.   *          .     *      *        *    .     *.   *          .     *      *        *    .
         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
   .        ..    *    .      *  .  ..  *    .        ..    *    .      *  .  ..  *         *   *    .  *      .        .  *   .
         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .

    		                        {Fore.LIGHTBLUE_EX}:::    ::: :::{Fore.MAGENTA}  ::: ::::{Fore.BLUE}::::::: :::{Fore.LIGHTMAGENTA_EX}   :::  ::::::::  
    		                        {Fore.LIGHTBLUE_EX}:+:    :+: :+:{Fore.MAGENTA} :+:      {Fore.BLUE}:+:     :+:{Fore.LIGHTMAGENTA_EX}   :+: :+:    :+: 
    		                        {Fore.LIGHTBLUE_EX}+:+    +:+ +:+{Fore.MAGENTA}+:+       {Fore.BLUE}+:+      +:{Fore.LIGHTMAGENTA_EX}+ +:+  +:+    +:+ 
    		                        {Fore.LIGHTBLUE_EX}+#+    +#+ +#+{Fore.MAGENTA}+#+       {Fore.BLUE}+#+        {Fore.LIGHTMAGENTA_EX}+#+    +#+    +#+ 
    		                        {Fore.LIGHTBLUE_EX}#+#    #+# #+#{Fore.MAGENTA} #+#      {Fore.BLUE}#+#        {Fore.LIGHTMAGENTA_EX}#+#    #+#    #+# 
    		                         {Fore.LIGHTBLUE_EX}########  ###{Fore.MAGENTA}  ### ####{Fore.BLUE}#######    {Fore.LIGHTMAGENTA_EX}###     ######## 

    		                                           {Fore.LIGHTCYAN_EX}[DEVELOPER INFO]{Fore.RESET}
    		                      {Fore.LIGHTGREEN_EX}Donate {Fore.RESET}|{Fore.LIGHTGREEN_EX} bc1qarzdvq6z8tfj45f4runsajaqtmywlh4y76862m 
    		                         {Fore.LIGHTMAGENTA_EX}Dev {Fore.RESET}|{Fore.LIGHTMAGENTA_EX} https://github.com/how1456

{Fore.LIGHTCYAN_EX}{datetime} {Fore.LIGHTGREEN_EX}how was launched.
{Fore.LIGHTCYAN_EX}{datetime} {Fore.LIGHTGREEN_EX}Welcome to how.
{Fore.LIGHTCYAN_EX}{datetime} {Fore.RESET}[SYSTEM]{Fore.LIGHTCYAN_EX} Your RAM usage is at {ram_usage}% and your CPU usage is at {cpu_usage}%.{Fore.RESET}""")



def change_vanity():
   payload = {"code": vanity_url}
   response = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/vanity-url", headers=headers, json=payload)
   if response.status_code == 200:
      print(f"{Fore.LIGHTGREEN_EX}alindi : discord.gg/{vanity_url} gg ez")
      data = {"content" : f"how xd : discord.gg/{vanity_url} Başarılı :flushed: ||@everyone||", "username" : "how."}
      requests.post(webhook, json=data)
   else:
      print(f"{Fore.LIGHTRED_EX}url alinamadi discord.gg/{vanity_url}! hata kodu : {response.status_code} | bidahaki sefere:(")



def check_vanity():
   response = requests.get(f"https://discord.com/api/v9/invites/{vanity_url}?with_counts=true&with_expiration=true", headers=headers)
   if response.status_code == 404:
      change_vanity()
      exit()
   else:
      print(f'{Fore.LIGHTRED_EX}[ + ] url alındı{Fore.RESET}')

start()

vanity_url = input(f'{Fore.LIGHTCYAN_EX}Vanity To Snipe {Fore.RESET}> ')
guild_id = input(f'{Fore.LIGHTCYAN_EX}Guild To Apply Vanity After Sniping {Fore.RESET}> ')

while True:
   check_vanity()


