import requests


class TelegramBot:
    TOKEN = ''
    CHATS = {
        'cmeiiiho': 931965146,
    }
    DOMAIN = ''

    def send_msg(self, msg, chat_id=None, username='cmeiiiho'):
        chat_id = chat_id if chat_id else self.__class__.CHATS[username]
        data = {'text': msg, 'chat_id': chat_id}
        r = requests.post('https://api.telegram.org/bot{}/{}'.format(self.TOKEN, 'sendMessage'), data=data)

    def reset_webhook(self):
        data = {'drop_pending_updates': True}
        r = requests.post('https://api.telegram.org/bot{}/{}'.format(self.TOKEN, 'deleteWebhook'), data=data)
        data = {'url': f'https://{self.DOMAIN}/utils/telegram_webhook/'}
        return requests.post('https://api.telegram.org/bot{}/{}'.format(self.TOKEN, 'setWebhook'), data=data)

