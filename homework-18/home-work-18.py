class Bot:
    def __init__(self, name):
        self.naming = name

    def send_message(self, massage):
        print(massage)

    def say_name(self):
        print(self.naming)

bot1 = Bot("Marvin")

bot1.send_message("Hello!")
bot1.say_name()

class TelegramBot(Bot):
    def __init__(self, name, url, chat_id):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def send_message(self, massage):
        print(f"{self.naming} bot says {massage} to chat {self.chat_id} using {self.url}")

    def set_chat_id(self, setting_chat_id):
        self.chat_id = setting_chat_id

    def set_url(self, setting_url):
        self.url = setting_url

telegram_bot =TelegramBot("TG", None, None)
telegram_bot.say_name()
telegram_bot.send_message("Hello")
telegram_bot.set_chat_id(1)
telegram_bot.set_url(2)
telegram_bot.send_message("Hello")