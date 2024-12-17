import requests
import asyncio
from typing import List, Union
from urllib.parse import urlparse
import time
from datetime import datetime
from telegram import Bot

class WebsiteMonitor:
    def __init__(self, bot_token: str, chat_id: str):
        """
        Initialize the website monitor with Telegram bot credentials.
        
        Args:
            bot_token: Your Telegram Bot token
            chat_id: Your Telegram chat ID
        """
        self.bot = Bot(token=bot_token)
        self.chat_id = chat_id
        self.last_error_time = {}  # Track last error time per website to prevent spam

    async def send_telegram_alert(self, message: str) -> None:
        """
        Send a Telegram alert about a website error.
        """
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message, parse_mode="Markdown")
            print("Telegram message sent.")
        except Exception as e:
            print(f"Error sending message: {e}")

    def check_website_status(self, *websites: Union[str, List[str]], interval: int = 300) -> None:
        """
        Continuously check the status of websites and send Telegram alerts on errors.
        
        Args:
            *websites: Variable number of website URLs as strings or a list of URLs
            interval: Time in seconds between checks (default: 300 seconds / 5 minutes)
        """
        # Flatten the input in case a list was passed
        website_list = []
        for item in websites:
            if isinstance(item, list):
                website_list.extend(item)
            else:
                website_list.append(item)
        
        print(f"Starting website monitoring. Checking every {interval} seconds.")
        print("Press Ctrl+C to stop the monitoring.")
        
        try:
            while True:
                print(f"\n=== Check started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
                
                for website in website_list:
                    # Validate URL format
                    try:
                        result = urlparse(website)
                        if not all([result.scheme, result.netloc]):
                            error_msg = "Invalid URL format"
                            print(f"{website}: {error_msg}")
                            asyncio.run(self.send_telegram_alert(f"⚠️ Website Monitor Alert ⚠️\n\nSite: {website}\nError: {error_msg}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
                            continue
                    except Exception:
                        error_msg = "Invalid URL format"
                        print(f"{website}: {error_msg}")
                        asyncio.run(self.send_telegram_alert(f"⚠️ Website Monitor Alert ⚠️\n\nSite: {website}\nError: {error_msg}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
                        continue
                        
                    try:
                        # Use a session to handle connection pooling
                        with requests.Session() as session:
                            start_time = time.time()
                            response = session.head(
                                website,
                                timeout=5,
                                allow_redirects=True,
                                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                            )
                            response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
                            
                            if response.status_code == 200:
                                print(f"{website}: Online (Status: {response.status_code}, Response Time: {response_time:.0f}ms)")
                            else:
                                error_msg = f"Status Code {response.status_code} (Response Time: {response_time:.0f}ms)"
                                print(f"{website}: {error_msg}")
                                asyncio.run(self.send_telegram_alert(f"⚠️ Website Monitor Alert ⚠️\n\nSite: {website}\nError: {error_msg}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
                                
                    except requests.ConnectionError:
                        error_msg = "Connection Error"
                        print(f"{website}: Offline ({error_msg})")
                        asyncio.run(self.send_telegram_alert(f"⚠️ Website Monitor Alert ⚠️\n\nSite: {website}\nError: {error_msg}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
                    except requests.Timeout:
                        error_msg = "Timeout"
                        print(f"{website}: Offline ({error_msg})")
                        asyncio.run(self.send_telegram_alert(f"⚠️ Website Monitor Alert ⚠️\n\nSite: {website}\nError: {error_msg}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
                    except requests.TooManyRedirects:
                        error_msg = "Too Many Redirects"
                        print(f"{website}: Offline ({error_msg})")
                        asyncio.run(self.send_telegram_alert(f"⚠️ Website Monitor Alert ⚠️\n\nSite: {website}\nError: {error_msg}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
                    except Exception as e:
                        error_msg = str(e)
                        print(f"{website}: Error ({error_msg})")
                        asyncio.run(self.send_telegram_alert(f"⚠️ Website Monitor Alert ⚠️\n\nSite: {website}\nError: {error_msg}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
                
                print(f"=== Check completed. Waiting {interval} seconds for next check ===")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            return

# Example usage:
if __name__ == "__main__":
    # Your Telegram bot token and chat ID
    BOT_TOKEN = 'YOUR_BOT_TOKEN'  # Add your bot token here
    CHAT_ID = 'YOUR_CHAT_ID'  # Add your chat ID here
    
    # Initialize the monitor
    monitor = WebsiteMonitor(
        bot_token=BOT_TOKEN,
        chat_id=CHAT_ID
    )
    
    # List of websites to monitor
    websites = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.example.com",
        "https://www.example50.com",
    ]
    
    # Start monitoring with checks every 600 seconds
    monitor.check_website_status(websites, interval=600)
