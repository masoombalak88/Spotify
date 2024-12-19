from pyrogram import Client, filters
import requests
from PURVIMUSIC import app


# Define the API base URL
API_URL = "https://chatwithai.codesearch.workers.dev/?chat="


# Define the /ask command handler
@app.on_message(filters.command("ask") & filters.private)
def ask_command(client, message):
    user_query = " ".join(message.command[1:])  # Get the query after the command
    if not user_query:
        message.reply_text("Please provide a query after the /ask command.")
        return

    try:
        # Query the API
        response = requests.get(API_URL + user_query)
        api_response = response.json().get("data", "Sorry, I couldn't get a response.")
    except Exception as e:
        api_response = "Oops! Something went wrong while fetching the response."

    # Send the response to the user
    message.reply_text(api_response)
