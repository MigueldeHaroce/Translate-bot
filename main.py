import discord
from discord.ext import commands
from googletrans import Translator
from langdetect import detect

# Initialize intents
intents = discord.Intents.default()
intents.messages = True  # Enable the message intenta
intents.message_content = True  # Enable the message content intent
# Initialize the Discord client with intents
client = commands.Bot(command_prefix='!', intents=intents)

# Initialize the translator
translator = Translator()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")
    if message.channel.id == 1041098518858838037:
        # Split the message into sentences
        sentences = message.content.split('\n')
        translated_message = ''
        for sentence in sentences:
            # Detect the language of the sentence
            try:
                src_lang = detect(sentence)
            except:
                src_lang = 'unknown'
            # If the language is English, translate the sentence
            if src_lang == 'en':
                # Split the sentence into parts of 5000 characters each
                parts = [sentence[i:i+5000] for i in range(0, len(sentence), 5000)]
                for part in parts:
                    translated_part = translator.translate(part, dest='es').text
                    translated_message += translated_part
            else:
                translated_message += sentence
            translated_message += '\n'
        # Send the translated message to the target channel
        target_channel = client.get_channel(1041098389250637917)
        # Split the translated message into parts of 2000 characters each
        messages = [translated_message[i:i+2000] for i in range(0, len(translated_message), 2000)]
        for msg in messages:
            await target_channel.send(f"**Translated**: {msg}")
client.run('MTA0MTA5ODEwNjM5MDk3MDQ1OQ.GoAfmV.UjPdJJoENshSNzHaNjbYYDfW5iUCBezjLanUiM')
