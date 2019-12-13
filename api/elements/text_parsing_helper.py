from api.elements.textParsing.requestParsing import *
from webapp.models import UserData
from webapp.models import RegisrationData
from webapp.utils.time_helper import *
from api.utils.strings import Strings
from api.elements.textParsing.textKit.findDate import *

requestParsing = RequestParsing()
strings = Strings()
date = findDate()


def get_answer_alice(user_text, userId, newSession=False):
    if newSession == True:
        return strings.get('new_user')

    user = UserData.objects.filter(yandex_user_id=userId)

    if (len(user) == 0):
        return register_user(user_text, userId)

    else:
        return requestParsing.process(user_text, user[0].eljur_user_id)


def get_answer_ga(user_text, userId, detect_module, ga_params):
    user = UserData.objects.filter(yandex_user_id=userId)

    if (len(user) == 0):
        return register_user(user_text, userId)

    else:
        return requestParsing.process(user_text, user[0].eljur_user_id, detect_module, ga_params)


def get_card_ga(detect_module=None, answer_text=None):
    fulfillment_messages = []
    card_dict = dict()
    card = dict()
    card['title'] = 'card title'
    card['subtitle'] = 'card subtitle'
    card['imageUri'] = 'https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png'
    card['buttons'] = [
        {
            "text": "button text",
            "postback": "https://assistant.google.com/"
        }
    ]
    card_dict['card'] = card
    fulfillment_messages.append(card_dict)
    return fulfillment_messages

def register_user(user_text, userId):
    user_text = user_text.lower()
    user_text = user_text.replace(',', '')
    user_text = user_text.replace(' ', '')

    currentTime = get_current_time()

    RegisrationData.objects.filter(expires__lte=str(currentTime)).delete()
    regisration_user_data = RegisrationData.objects.filter(activation_phrase=user_text)

    if (len(regisration_user_data) == 0):
        return strings.get('retry_to_login')

    regisration_user_data = regisration_user_data[0]
    newUser = UserData(yandex_user_id=userId, eljur_user_id=regisration_user_data.eljur_user_id)
    newUser.save()
    return strings.get('successful_login')
