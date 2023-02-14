import pyrogram
from pyrogram import Client, Filters

api_id=27063178
api_hash="82937245474af5065ab0f857e772aad8"
bot_token="5910218382:AAHqe2wBnNX6ET0xqoiiniqzwuQwrrUPaZY"
app = Client("my_account", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(Filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I'm an Instagram Downloader Bot. Please send me the link of the Instagram post you want to download.")

    
@app.on_message(Filters.regex('^https://www\.instagram\.com/p/.+'))
def download(client, message):

    # Extracting the post URL from the message 
    post_url = message.text

    # Generating a download button with the post URL 
    btn = pyrogram.InlineKeyboardButton('Download', url=post_url)

    # Generating a keyboard with the button 
    keyboard = pyrogram.InlineKeyboardMarkup([[btn]])

    # Sending a message with the keyboard 
    message.reply_text("Here's your download link:", reply_markup=keyboard)

    
app.run()
