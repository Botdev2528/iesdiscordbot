import discord 
from discord.ext import commands
import random
import time




client = commands.Bot(command_prefix="/",case_insensitive=True)
owner_id="397648789793669121ss"
client.remove_command("help")


@client.event
async def on_ready ():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("That War Server"))
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")
    await member.send(f"Welcome to the Imperial Eagles Squadron Discord Server,{member}.sUse /register on the #bot-channel to register on the That War Server Forums. After registering you can use /clanpage to visit our clan's page in the forums.Enjoy your stay here .Long Live!")
    

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

@client.event
async def on_command_error(ctx,error):
    if isinstance (error,commands.CommandNotFound):
       await ctx.send("That command does not exist!") 


 


@client.command()
async def ping(ctx):
    lag=round(client.latency*1000)
    embed=discord.Embed(
        
        colour=discord.Colour.blue()
    )
    embed.add_field(name="Ping! :ping_pong:", value=lag)
    await ctx.send(embed=embed)

@client.command(aliases=["8ball"])
async def _8ball(ctx,*,question):
    responses = ["Yes","No"]

    await ctx.send(f"Question: {question} \n Answer: {random.choice(responses)}")

@_8ball.error
async def _8ball_error(ctx,error):
     if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please input the question as well.")

@client.command()
async def toss(ctx):
    responses =["Heads","Tails"]
    await ctx.send(f"You got a {random.choice(responses)}")

@client.command()

async def kick(ctx, member: discord.Member,*,reason=None):
    if ctx.message.author.guild_permissions.administrator:
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.send(f"Admin has kicked {member} for {reason}")
    else:
        await ctx.send(f"You don't have the necessary permissions to do this.")

@kick.error
async def kick_error(ctx,error):
     if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please specify the user to kick.")

@client.command()
async def ban(ctx, member : discord.Member,*, reason=None):
    if ctx.message.author.guild_permissions.administrator:
        await member.ban(reason=reason)
        await ctx.send(f"Admin has banned {member} for {reason}")
    else:
        await ctx.send(f"You don't have the necessary permissions to do this.")


@ban.error
async def  ban_error(ctx,error):
     if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please specify the user to ban.")

@client.command()
async def mute(ctx,member:discord.Member,reason=None):
   
    role=discord.utils.get(ctx.guild.roles,name="muted")
    if ctx.message.author.guild_permissions.administrator:
        await member.add_roles(role)
        await ctx.send(f"Muted {member}")
        await ctx.message.delete()
    else:
        await ctx.send(f"You don't have the necessary permissions to do this.")


@client.command()
async def unmute(ctx,member:discord.Member,*,reason=None):
    role=discord.utils.get(ctx.guild.roles,name="muted")
    await member.remove_roles(role)
    await ctx.send(f"Unmuted {member}")

@mute.error
async def  mute_error(ctx,error):
     if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please specify the user to mute..")

@unmute.error
async def  unmute_error(ctx,error):
     if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please speicfy the user to unmute.")

@client.command()
async def requesthelp(ctx,*,reason=None):
    channel=client.get_channel(458686184399437857)
    
    await ctx.message.delete()
    await channel.send (f"@here {ctx.message.author.name} has requested help. Reason: {reason}")
    






@client.command ()
async def dice(ctx):
    responses=["1","2","3","4","5","6"]
    await ctx.send(f"You got a {random.choice(responses)}.")
    






@client.command()
async def prefix(ctx):
    await ctx.send (f"My prefix is **>**")



@client.command()
async def rps(ctx,player):
    o=["rock","paper","scissors"]
    computer = random.choice(o)
    if player=="rock" or player=="paper" or player=="scissors":
        await ctx.send (computer)
    else:
        await ctx.send("Wrong input!")
        
    if player==computer:
        await ctx.send(f"Draw!")
    elif player=="rock" and computer=="paper":
        await ctx.send("You lost!")
    elif player=="rock" and computer =="scissors":
        await ctx.send("You won!")
    elif player=="scissors" and computer=="rock":
        await ctx.send("You lost!")
    elif player=="scissors" and computer=="paper":
        await ctx.send("You won")
    elif player=="paper" and computer=="rock":
        await ctx.send("You won")
    elif player=="paper" and computer =="scissors":
        await ctx.send("You lost")
    
@rps.error
async def rps_error(ctx,error):
     if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please input your choice.")


@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)








@client.command()
async def help(ctx):
    embed=discord.Embed(
        title= "Commands",
        description="These are the commands and their syntax",
        colour= discord.Colour.blue()

    )
    embed.set_footer(text="Contact Rusher#3394 to report bugs")  
    
    embed.set_author(name="Eagle bot.",
    icon_url="https://cdn.discordapp.com/attachments/589083129852198914/590191427376644124/l4tdfSV.png")
    embed.add_field(name="8ball",value="Answers a question with yes or no. You need to supply the question with the command.",inline=False)
    embed.add_field(name="ban",value="Bans a member.",inline=False)
    embed.add_field(name="kick",value="Kicks a member.",inline=False)
    embed.add_field(name="clear",value="Clears a given number of messages.Default value is 5. Syntax: clear (number)",inline=False)
    embed.add_field(name="dice",value="Rolls a dice.",inline=False)
    embed.add_field(name="requesthelp",value="Sends a message to the leadereship asking for help.",inline=False) 
   
    embed.add_field(name="mute",value="Mutes a member",inline=False)
    embed.add_field(name="unmute",value="Unmutes a member",inline=False)
    embed.add_field(name="help",value="Displays this message.",inline=False)
   
    embed.add_field(name="ping",value="Shows the latency.",inline=False)
    embed.add_field(name="prefix",value="Shows the bot prefix.",inline=False)
   
    embed.add_field(name="rps",value="Starts the rock paper scissors game. You should input your choice with the command.Syntax: rps (choice)",inline=False)
 
    embed.add_field(name="toss",value="Flips a coin.",inline=False)

    

    
    await ctx.author.send(embed=embed)
    await ctx.send("Check your DMs!")
   










client.run("NTkwMTg3Mzk1MDczNDQxODAy.XQek4Q.F4UikDblDiFrADIMUO3JfwvVTFI")



