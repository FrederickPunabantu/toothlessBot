import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import re
import random

from keep_alive import keep_alive

load_dotenv()

keep_alive()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Level 3 waiting roles to genre roles
ROLE_MAP = {
    "rnb_waiting": "rnb",
    "pop_waiting": "pop",
    "rock/metal_waiting": "rock/metal",
    "hip-hop_waiting": "hip-hop",
    "afrobeats_waiting": "afrobeats",
    "yn-music_waiting": "yn-music",
    "k-pop_waiting": "k-pop",
}

# Genre role names to channel names
CHANNEL_MAP = {
    "rnb": "😩︱𝙍𝙣𝙗・𝙃𝙞𝙥𝙃𝙤𝙥",
    "pop": "🧚‍♀️︱𝙋𝙤𝙥",
    "rock/metal": "🤘︱𝙍𝙤𝙘𝙠・𝙈𝙚𝙩𝙖𝙡",
    "hip-hop": "😩︱𝙍𝙣𝙗・𝙃𝙞𝙥𝙃𝙤𝙥",
    "afrobeats": "🪘︱𝘼𝙛𝙧𝙤𝙗𝙚𝙖𝙩𝙨",
    "yn-music": "🥷︱𝙔𝙉-𝙈𝙪𝙨𝙞𝙘",
    "k-pop": "🫰︱𝙆𝙥𝙤𝙥",
}

# Level 6 waiting roles to element roles
ELEMENT_ROLE_MAP = {
    "water_waiting": "water",
    "fire_waiting": "fire",
    "earth_waiting": "earth",
    "air_waiting": "air",
}

# Element roles to channels
ELEMENT_CHANNEL_MAP = {
    "water": "🌊︱𝙒𝙖𝙩𝙚𝙧・𝙩𝙧𝙞𝙗𝙚",
    "fire": "🔥︱𝙁𝙞𝙧𝙚・𝙣𝙖𝙩𝙞𝙤𝙣",
    "earth": "🪨︱𝙀𝙖𝙧𝙩𝙝・𝙠𝙞𝙣𝙜𝙙𝙤𝙢",
    "air": "🌪️︱𝘼𝙞𝙧・𝙣𝙤𝙢𝙖𝙙𝙨",
}

# Level 10 waiting roles to final roles
AGE_ROLE_MAP = {
    "13_waiting": "13",
    "14_waiting": "14",
    "15_waiting": "15",
    "16_waiting": "16",
    "17_waiting": "17",
    "18+_waiting": "18+",
}

AGE_CHANNEL_MAP = {
    "18+": "🔞︱18_𝘾𝙝𝙖𝙩",
}

ARCANE_ID = 437808476106784770

@bot.event
async def on_ready():
    print(f"Toothless is live as {bot.user}")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author.id == ARCANE_ID:
        match = re.search(r"<@!?(\d+)> has reached level \*\*(\d+)\*\*", message.content)
        if match:
            user_id, level = match.groups()
            guild = message.guild
            member = guild.get_member(int(user_id))

            if not member:
                print("[ERROR] Member not found")
                return

            if level == "3":
                # print(f"[DEBUG] Level 3 triggered for {member.display_name} ({member.id})")
                unlocked = []
                for wr_name, fr_name in ROLE_MAP.items():
                    wr = discord.utils.get(guild.roles, name=wr_name)
                    fr = discord.utils.get(guild.roles, name=fr_name)
                    # print(f"[DEBUG] Checking role {wr_name} -> {fr_name}: wr={wr}, fr={fr}, has_wr={wr in member.roles if wr else False}")
                    if wr in member.roles:
                        await member.remove_roles(wr)
                        await member.add_roles(fr)
                        unlocked.append(fr_name)
                        print(f"[DEBUG] Unlocked {fr_name} for {member.display_name}")

                # print(f"[DEBUG] Level 3 unlocked roles: {unlocked}")
                if unlocked:
                    role_msg = ", ".join(f"**{r}**" for r in unlocked)
                    await message.channel.send(f"🎉 {member.mention} hit level 3 and unlocked: {role_msg}!")
                    for r in unlocked:
                        ch_name = CHANNEL_MAP.get(r)
                        if ch_name:
                            ch = discord.utils.get(guild.text_channels, name=ch_name)
                            if ch:
                                await ch.send(f"Welcome {member.mention} to **{ch_name}**! They just hatched! 🐣")
                else:
                    pass
                    # print(f"[DEBUG] No roles unlocked for {member.display_name} at level 3")

            elif level == "6":
                # print(f"[DEBUG] Level 6 triggered for {member.display_name} ({member.id})")
                unlocked = []
                for wr_name, fr_name in ELEMENT_ROLE_MAP.items():
                    wr = discord.utils.get(guild.roles, name=wr_name)
                    fr = discord.utils.get(guild.roles, name=fr_name)
                    # print(f"[DEBUG] Checking element role {wr_name} -> {fr_name}: wr={wr}, fr={fr}, has_wr={wr in member.roles if wr else False}")
                    if wr in member.roles:
                        await member.remove_roles(wr)
                        await member.add_roles(fr)
                        unlocked.append(fr_name)
                        print(f"[DEBUG] Unlocked {fr_name} for {member.display_name}")

                # print(f"[DEBUG] Level 6 unlocked roles: {unlocked}")
                if unlocked:
                    role_msg = ", ".join(f"**{r}**" for r in unlocked)
                    await message.channel.send(f"🎉 {member.mention} hit level 6 and unlocked: {role_msg}!")
                    for r in unlocked:
                        ch_name = ELEMENT_CHANNEL_MAP.get(r)
                        if ch_name:
                            ch = discord.utils.get(guild.text_channels, name=ch_name)
                            if ch:
                                await ch.send(f"🎉 {member.mention} just joined the **{ch_name}**!")
                else:
                    pass
                    # print(f"[DEBUG] No element roles unlocked for {member.display_name} at level 6")

            elif level == "10":
                # print(f"[DEBUG] Level 10 triggered for {member.display_name} ({member.id})")
                unlocked = []
                for wr_name, fr_name in AGE_ROLE_MAP.items():
                    wr = discord.utils.get(guild.roles, name=wr_name)
                    fr = discord.utils.get(guild.roles, name=fr_name)
                    # print(f"[DEBUG] Checking age role {wr_name} -> {fr_name}: wr={wr}, fr={fr}, has_wr={wr in member.roles if wr else False}")
                    if wr in member.roles:
                        await member.remove_roles(wr)
                        await member.add_roles(fr)
                        unlocked.append(fr_name)
                        print(f"[DEBUG] Unlocked {fr_name} for {member.display_name}")

                # print(f"[DEBUG] Level 10 unlocked roles: {unlocked}")
                if unlocked:
                    for r in unlocked:
                        ch_name = AGE_CHANNEL_MAP.get(r)
                        if ch_name:
                            ch = discord.utils.get(guild.text_channels, name=ch_name)
                            if ch:
                                await ch.send(f"🎉 {member.mention} finally got to **{ch_name}**!")
                        # Handle individual age roles that map to hangout
                        elif r in ["13", "14", "15", "16", "17"]:
                            hangout_ch = discord.utils.get(guild.text_channels, name="😎・hangout")
                            if hangout_ch:
                                await hangout_ch.send(f"🎉 {member.mention} finally got to **😎・hangout**!")
                else:
                    pass
                    # print(f"[DEBUG] No age roles unlocked for {member.display_name} at level 10")

bot.run(os.getenv("DISCORD_TOKEN"))




