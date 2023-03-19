import responses
import discord
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s %(name)s %(message)s')


async def send_message(message, user_message, is_private):   # Send messages
    
    try:
        response = responses.handle_response(user_message)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        logging.exception("An exception occurred while sending the message")
        error_message = "error!"
        await message.author.send(error_message) if is_private else await message.channel.send(error_message)

def run_discord_bot():
    TOKEN = 'MTA4NDc0OTYwMjY4ODg2MDIwMA.G9WNrZ.2lkrSV-mUSxDYBBOdlBbv0lTpkUakgo2mn0-hU' 
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return
        

        # Get data about the user
        username = str(message.author)
        user_message = (message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})") #check

        print(f"user_message = '{user_message}'")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message and user_message[0] == '?':
            user_message = user_message[1:]   # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
