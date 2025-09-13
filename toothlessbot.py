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
    "rnb": "😩︱𝑅𝓃𝐵",
    "pop": "🧚‍♀️︱𝒫𝑜𝓅",
    "rock/metal": "🤘︱𝑅𝑜𝒸𝓀・𝑀𝑒𝓉𝒶𝓁",
    "hip-hop": "🎤︱𝐻𝒾𝓅・𝐻𝑜𝓅",
    "afrobeats": "🪘︱𝒜𝒻𝓇𝑜𝒷𝑒𝒶𝓉𝓈",
    "yn-music": "🥷︱𝒴𝒩・𝑀𝓊𝓈𝒾𝒸",
    "k-pop": "🫰︱𝓀・𝓅𝑜𝓅",
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
    "water": "🌊︱𝖶𝖺𝗍𝖾𝗋・𝖳𝗋𝗂𝖻𝖾",
    "fire": "🔥︱𝖥𝗂𝗋𝖾・𝖭𝖺𝗍𝗂𝗈𝗇",
    "earth": "🪨︱𝖤𝖺𝗋𝗍𝗁・𝖪𝗂𝗇𝗀𝖽𝗈𝗆",
    "air": "🌪️︱𝖠𝗂𝗋・𝖭𝗈𝗆𝖺𝖽𝗌",
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
    "15", "16", "17": "😎︱𝙉𝙤・𝙪𝙣𝙘・𝙯𝙤𝙣𝙚",
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

