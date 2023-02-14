import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Create a Pyrogram client object
app = Client("5910218382:AAHqe2wBnNX6ET0xqoiiniqzwuQwrrUPaZY")

# Define a start message
start_message = """
Welcome to the Instagram Downloader Bot!
To use this bot, simply send me a link to an Instagram post or story.
"""

# Define a function to handle incoming messages
@app.on_message(filters.private & filters.text)
def handle_message(client, message):
    # Check if the message contains an Instagram link
    if "instagram.com" in message.text:
        # Create a keyboard with download options
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Download Post", callback_data="post")],
            [InlineKeyboardButton("Download Story", callback_data="story")]
        ])
        # Send a message with the keyboard
        message.reply_text("Select an option:", reply_markup=keyboard)
    else:
        # Send a message with the start message
        message.reply_text(start_message)

# Define a function to handle button clicks
@app.on_callback_query()
def handle_button(client, callback_query):
    # Get the download option from the button
    option = callback_query.data
    # Get the Instagram link from the original message
    message = callback_query.message.reply_to_message
    link = message.text
    # Download the media based on the option
    if option == "post":
        # Download the post image or video
        url = f"https://www.instagram.com/p/{link.split('/')[-2]}/?__a=1"
        response = requests.get(url)
        media_url = response.json()["graphql"]["shortcode_media"]["display_url"]
        filename = media_url.split("/")[-1]
        response = requests.get(media_url)
        with open(filename, "wb") as f:
            f.write(response.content)
        # Send the downloaded media
        message.reply_photo(filename)
        # Delete the file
        os.remove(filename)
    elif option == "story":
        # Download the story image or video
        url = f"https://www.instagram.com/stories/{link.split('/')[-2]}/?__a=1"
        response = requests.get(url)
        media_url = response.json()["graphql"]["user"]["reel"]["items"][0]["display_url"]
        filename = media_url.split("/")[-1]
        response = requests.get(media_url)
        with open(filename, "wb") as f:
            f.write(response.content)
        # Send the downloaded media
        message.reply_photo(filename)
        # Delete the file
        os.remove(filename)

# Start the Pyrogram client
app.run()
