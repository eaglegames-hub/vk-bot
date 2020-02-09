from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random



vk = vk_api.VkApi(token=(str(yagey)))

session_api = vk.get_api()
longpoll = VkLongPoll(vk)

videos = ['video-123021844_456239687', 'video-124479548_456239189', 'video-174607975_456239537', 'video-124969741_456239490', 'video-30316056_456292836', 'video-128842848_456239618', 'video-54441828_456248424', 'video-30316056_456299700', 'video-160381055_456239038', 'video-30316056_456300819', 'video-176605088_456239233', 'video-162772825_456239028', 'video-152083915_456247127', 'video343531963_456239443', 'video-152083915_456248098', 'video-56263398_456271201', 'video-177786309_456239068', 'video-45745333_456276407', 'video88427913_456239910', 'video-30316056_456313774', 'video357689020_456239236', 'video-45745333_456289485', 'video-167127847_456247225', 'video-167127847_456247459']
photos = ['photo-190840617_457239017', 'photo-187510308_457240293', 'photo-190840617_457239018', 'photo-190840617_457239019', 'photo-190840617_457239020', 'photo-190840617_457239021', 'photo-190840617_457239022', 'photo-190840617_457239023', 'photo-190840617_457239024', 'photo-190840617_457239025', 'photo-190840617_457239026', 'photo-190840617_457239027', 'photo-190840617_457239028', 'photo-190840617_457239029', 'photo-190840617_457239030', 'photo-190840617_457239031', 'photo-190840617_457239032', 'photo-190840617_457239033', 'photo-190840617_457239034', 'photo-190840617_457239035', 'photo-190840617_457239036', 'photo-190840617_457239037', 'photo-190840617_457239038', 'photo-190840617_457239039', 'photo-190840617_457239040', 'photo-190840617_457239041', 'photo-190840617_457239042', 'photo-190840617_457239043', 'photo-190840617_457239044', 'photo-190840617_457239045', 'photo-190840617_457239046', 'photo-190840617_457239047', 'photo-190840617_457239048', 'photo-190840617_457239049', 'photo-190840617_457239050', 'photo-190840617_457239051', 'photo-190840617_457239052', 'photo-190840617_457239053', 'photo-190840617_457239054', 'photo-190840617_457239055', 'photo-190840617_457239056', 'photo-190840617_457239057', 'photo-190840617_457239058', 'photo-190840617_457239059', 'photo-190840617_457239060', 'photo-190840617_457239061', 'photo-190840617_457239062', 'photo-190840617_457239063', 'photo-190840617_457239064', 'photo-190840617_457239065', 'photo-190840617_457239066', 'photo-190840617_457239067', 'photo-190840617_457239068', 'photo-190840617_457239069', 'photo-190840617_457239070', 'photo-190840617_457239071', 'photo-190840617_457239072', 'photo-190840617_457239073', 'photo-190840617_457239074', 'photo-190840617_457239075', 'photo-190840617_457239076', 'photo-190840617_457239077']
videos1 = ['video-146305289_456239726', 'video270010386_456239055', 'video-167127847_456251040', 'video-171492242_456241607', 'video208091938_456239075', 'video-167127847_456249998', 'video-73672378_456239044', 'video231667969_171741336', 'video439933189_456239446', 'video238052810_456239077', 'video-100477272_456248382', 'video-167127847_456243782', 'video-103083994_456244079', 'video-166884737_456243266', 'video-167127847_456244046', 'video-167127847_456244038', 'video275178431_170436718', 'video-167127847_456248599', 'video-179933989_456239124', 'video-98699940_456255899', 'video-98699940_456241691', 'video-98699940_456249068', 'video-98699940_456247996']
admins = [170244907, 526710962, 264817132]

vk.method("messages.send", {"peer_id": 170244907, "message": "Бот врубился", "random_id": random.randint(1, 2147483647)})


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'начать' or response == 'назад' or response == 'ютуб анал' or response == 'донат или реклама' or ('разраб' in response and response != 'разраб') or ('ютубер' in response and response != 'ютубер') or ('основатель' in response and response != 'основатель'):

        keyboard.add_button('Мем', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Видос', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Ютуб канал', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Связь с админами', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Донат или реклама', color=VkKeyboardColor.PRIMARY)


    elif response == 'связь с админами':
        keyboard.add_button('Основатель', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Ютубер', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Разраб', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('назад', color=VkKeyboardColor.DEFAULT)

    elif response == response == 'разраб' or response == 'ютубер' or response == 'основатель':
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk, id_type, id, message=None, attachment=None, keyboard=None):
    vk.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Время: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")) + " | " + 'id: ' + str(event.user_id) + " | " + 'Текст: ' + event.text, '\n')
        id = event.user_id
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "начать":
                send_message(vk, 'user_id', id, message='Добро пожаловать!', keyboard=keyboard)

            elif response == "связь с админами":
                send_message(vk, 'user_id', id, message= 'Выбери с кем хочешь связаться', keyboard=keyboard)

            elif response == 'разраб':
                text = "Введи сообщение для разраба или 'назад' для открытия меню" + '\n' + 'Пример:' + '\n' + "Разраб 'ваше сообение'"
                send_message(vk, 'user_id', id, message= text, keyboard=keyboard)
            elif response != 'разраб' and 'разраб' in response:
                send_message(vk, 'user_id', 170244907, message= (response[7:] + ' от id ' + str(event.peer_id)))

            elif response == 'ютубер':
                text = "Введи сообщение для ютубера или 'назад' для открытия меню" + '\n' + 'пример:' + '\n' + "Ютубер, 'ваше сообщение'"
                send_message(vk, 'user_id', id, message= text, keyboard=keyboard)
            elif response != 'ютубер' and 'ютубер' in response:
                send_message(vk, 'user_id', 526710962, message= response[7:] + ' от id ' + str(event.peer_id))

            elif response == 'основатель':
                text = "Введи сообщение для основателя или 'назад' для открытия меню" + '\n' + 'Пример:' + '\n' + "Основатель, 'ваше сообщение'"
                send_message(vk, 'user_id', id, message= text, keyboard=keyboard)
            elif response != 'основатель' and 'основатель' in response:
                send_message(vk, 'user_id', 264817132, message = response[11:] + ' от id ' + str(event.peer_id))

            elif response == 'назад':
                send_message(vk, 'user_id', event.user_id, message='Вы в главном меню', keyboard=keyboard)

            elif response == 'ютуб канал':
                text = 'подпишись на канал' + '\n' + 'https://www.youtube.com/channel/UCAkmJUeB1aWRy80iRKUO0rw'
                vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': random.randint(1, 2147483647)})

            elif response == 'донат или реклама':
                send_message(vk, 'user_id', id, message="переходите по ссылке и выбираете https://donate.qiwi.com/payin/TPAHCnOPTHblE_MEMbl", keyboard=keyboard)

            elif response == 'мем':
                vk.method('messages.send', {'user_id': id, 'message': '', 'random_id': random.randint(1, 2147483647), "attachment": random.choice(photos)})

            elif response == 'видос':
                vk.method('messages.send', {'user_id': id, 'message': '', 'random_id': random.randint(1, 2147483647), "attachment": random.choice(videos)})

            else:
                vk.method('messages.send', {'user_id': id, 'message': 'Я тебя не понял, напиши "начать"', 'random_id': random.randint(1, 2147483647)})