
# boluBOT

<div style="text-align: center;">
    <img src="https://th.bing.com/th/id/OIG1.VDfrbpS1yP337iQMobox?pid=ImgGn" alt="boluBOT himself" width="300">
</div>

Bolubot is a Twitch chat bot built using the Twitchio library. It is designed to interact with viewers, provide commands, and enhance the streaming experience on Twitch.

## Features

- **Custom Commands:** Easily add and manage custom commands for your channel.
- **Moderation Tools:** Automated moderation features to help manage chat.
- **Viewer Interaction:** Engage with your viewers through fun and interactive commands.

## Requirements

- **Python:** Version 3.6 or higher
- **Twitchio:** A Python library for interacting with the Twitch Chat.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/luiggisperandio/bolubot.git
   cd bolubot
   ```

2. **Install the required packages:**

   ```bash
   pip install twitchio
   ```

## Usage

1. **Configuration:**

   Create a `.env` file in the project root directory with the following information:

   ```env
    TMI_TOKEN= [oAuth2 for your twitch acount](https://twitchapps.com/tmi/)
    CLIENT_ID= [Your twitch app client ID](https://dev.twitch.tv/console/apps/create)
    BOT_NICK= Bot_name
    BOT_PREFIX= Command_prefix (recomended: !)
    CHANNEL="#Channel_name"
   ```

   Replace the placeholders with your Twitch token, client ID, and desired bot prefix.
   When fixed it should look something like the file bellow.

   ```env
    TMI_TOKEN=oauth:d1b2hjebdnjad7asd1jadsbk8casnk
    CLIENT_ID=d1b2hjebdnjad7asd1jadsbk8casnk
    BOT_NICK=boluBOT
    BOT_PREFIX=!
    CHANNEL="#tedesanuga"
   ```

2. **Configuring Actions (Optional but Recommended):**

    Inside `bot.py`, you can find various functions that serve as examples for Bolubot. These can be used as a starting point for creating your own functions.

    The `event_message()` function is executed every time a message is sent in the IRC. Within this function, you can implement checks for each message to determine whether the bot should respond. Since `ctx.content` is a string, you can use all string methods to process these messages. You can find more information in the [Twitchio documentation](https://twitchio.dev/en/latest/reference.html#twitchio.Message).

    To send a chat message as a response, simply call `await ctx.channel.send()` with the desired response as a string in the function's parameters, e.g., `await ctx.channel.send('Hello World!')`.

    To create a new command, define a function using the syntax below and add it to the `bot.py` file, below the `event_message()` function, to avoid conflicts.

    ```python
    @bot.command(name='command_call')
    async def custom_command(ctx):
        await ctx.send('command_response')
    ```

    The example above shows a basic working function. To create your own, replace the `command_call` and `command_response` strings with your desired command name and response.

    **Note:** To trigger a command, users must type `BOT_PREFIX` followed by `command_call` in the Twitch chat.


3. **Running the Bot:**

   Start the bot by running the main script:

   ```bash
   python bot.py
   ```

**Happy streaming!** 🎉

## Contact

For any questions or issues, please open an issue on GitHub.
