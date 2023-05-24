import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from utils.telegram_bot.bot import TelegramBot


@csrf_exempt
def webhook(request):
    try:
        data = json.loads(request.body.decode())
        chat_id = data['message']['chat']['id']
        bot = TelegramBot()
        bot.send_msg(data, chat_id)
    except Exception:
        pass
    return JsonResponse({'ok': True})


# income examples
request_from_telegram_chat = {
    'update_id': 368150044,
    'message': {
        'date': 1676938892,
        'from': {
            'id': 931965146,
            'first_name': 'Vitaly',
            'last_name': '2',
            'is_bot': False,
            'language_code': 'ru'
        },
        'text': 'test 4',
        'chat': {
            'id': 931965146,
            'first_name': 'Vitaly',
            'last_name': '2',
            'type': 'private'
        },
        'message_id': 31
    }
}

request_grom_telegram_group = {
    'update_id': 368150047,
    'message': {
        'from': {
            'id': 931965146,
            'first_name': 'Vitaly',
            'last_name': '2',
            'is_bot': False,
            'language_code': 'ru'
        },
        'text': '/start',
        'chat': {
            'id': -808218187,
            'all_members_are_administrators': True,
            'title': 'tg_bot_test',
            'type': 'group'
        },
        'message_id': 36,
        'date': 1676939154,
        'entities': [
            {
                'offset': 0,
                'length': 6,
                'type': 'bot_command'
            }
        ]
    }
}

callback_query = {
    'callback_query': {
        'message': {
            'from': {
                'is_bot': True,
                'username': 'Zhiviprostoru_bot',
                'id': 6244639121,
                'first_name': 'ЖивиПросто.ру'
            },
            'message_id': 54,
            'reply_markup': {
                'inline_keyboard': [
                    [
                        {
                            'callback_data': '1111111',
                            'text': 'ЗОЖ Консультация'
                        }
                    ],
                    [
                        {
                            'callback_data': '2222222',
                            'text': 'Психолог'
                        }
                    ]
                ]
            },
            'chat': {
                'id': 931965146,
                'last_name': '2',
                'first_name': 'Vitaly',
                'type': 'private'
            },
            'date': 1676945597,
            'text': 'так и так какой сервис выберем'
        },
        'from': {
            'is_bot': False,
            'id': 931965146,
            'last_name': '2',
            'first_name': 'Vitaly',
            'language_code': 'ru'
        },
        'data': '2222222',
        'id': '4002759824606379088',
        'chat_instance': '9215371325317788008'
    },
    'update_id': 368150060}
