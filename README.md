# Website Monitor with Telegram Alerts

## Introduction

This script monitors a list of websites at regular intervals and sends Telegram alerts for any errors such as site downtime or bad status codes. It is designed to be simple and flexible for personal or educational use.

## Features

- Monitors multiple websites at customizable intervals.
- Sends Telegram alerts for errors like site down or incorrect status codes.
- Handles exceptions such as connection errors, timeouts, and too many redirects.
- Easy configuration for Telegram bot token and chat ID.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages: `requests`, `asyncio`, `telegram`.

## Installation

1. **Install Dependencies**:

   ```bash
   pip install requests telegram
   ```

2. **Ensure Python 3.x is installed** on your system.

## Configuration

1. **Obtain Telegram Bot Token**:

   - Create a bot using [@BotFather](https://core.telegram.org/bots#6-botfather) on Telegram.
   - Retrieve your bot token from BotFather.

2. **Get Your Chat ID**:

   - Send a message to your bot.
   - Use the following script to retrieve your chat ID:

     ```python
     from telegram import Bot

     bot = Bot(token='YOUR_BOT_TOKEN')
     updates = bot.get_updates()
     for update in updates:
         print(update.message.chat.id)
     ```

3. **Replace Placeholder Values**:

   - Open the script and replace `'YOUR_BOT_TOKEN'` and `'YOUR_CHAT_ID'` with your actual bot token and chat ID.

## Usage

1. **Run the Script**:

   ```bash
   python script_name.py
   ```

2. **Modify Parameters** (Optional):

   - Update the `websites` list with your target websites.
   - Adjust the `interval` parameter to change the check frequency.

   Example:

   ```python
   monitor.check_website_status(websites, interval=600)
   ```

   This checks every 10 minutes.

## Error Handling

- The script catches exceptions such as `ConnectionError`, `Timeout`, `TooManyRedirects`, and others.
- Sends a Telegram alert with the error message and timestamp.
- Note: Rate limiting to prevent spam is not currently implemented but could be added.

## Stopping the Monitor

- Press `Ctrl+C` in the terminal to stop the script.

## Known Issues/Limitations

- No rate limiting for alerts.
- Ensure internet connectivity for accurate monitoring.

## Contributing

- Contributions are welcome! Fork the repository, make changes, and submit a pull request.
- Please adhere to the existing code style and add comments for clarity.

## License

- This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the maintainers of the `requests` and `telegram` libraries.

## Contact

- For questions or feedback, please open an issue or contact the script author.
