import os
import json
import glob
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from .filter_ambasador import filterAmbassador
from .assistans import random_sleep


class ParserGroups:

    def __init__(self, country, city, size_archive, phone, api_id, api_hash):
        self.size_archive = size_archive
        self.country = country
        self.city = city
        self.chats = []
        self.last_date = None
        self.chunk_size = 200
        self.count_of_peoples = 200000
        self.phone = phone
        self.api_id = api_id
        self.api_hash = api_hash

    async def parserGroup(self, name_group):
        self.client = TelegramClient(self.phone, self.api_id, self.api_hash)
        await self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone)
            self.client.sign_in(self.phone, input('Enter the code: '))
        random_sleep(1, 5, 'Client conected!')
        print(f'Go found @{name_group}\n')
        # get all groups of account
        result = await self.client(GetDialogsRequest(offset_date=self.last_date, offset_id=0, offset_peer=InputPeerEmpty(), limit=self.chunk_size, hash = 0))
        self.chats.extend(result.chats)
        # join group
        self.client(JoinChannelRequest(name_group))
        print(f'Group @{name_group} joined to my groups')
        # echo all groups of account (not necessary)
        print('My groups:\n')
        for chat in self.chats:
            try:
                if chat.username:
                    print(f'{chat.title} ------- @{chat.username}')
            except AttributeError as e:
                # print(f'\n-ERROR on chat:\n{chat}\n{e}\n')
                continue
        print('\n')
        # find and get all users of group
        this_chat = None
        for chat in self.chats:
            try:
                if chat.username == name_group:
                    this_chat = chat
                    break
            except AttributeError as e:
                # print(f'\n-ERROR:\n{e}\n')
                continue
        print(f'Group @{name_group} found')
        all_participants = []
        all_participants = await self.client.get_participants(this_chat, aggressive=True)
        await self.makeBioPhoto(all_participants, name_group)
        # leave of group
        self.client(LeaveChannelRequest(name_group))
        print(f'Group @{name_group} leaved of my groups')
        await self.client.disconnect()

    async def makeBioPhoto(self, all_participants, name_group):
        count_people = 0
        i = 0
        for user in all_participants:
            i += 1
            # if not self.active:
            #     print(f'\n\tPARSER STOPED\n')
            #     break
            if not user.photo:
                print(f'{i}: User_id {user.id} - NO PHOTO')
                continue
            user_id = user.id
            username = user.username if user.username else ""
            first_name = user.first_name if user.first_name else ""
            last_name = user.last_name if user.last_name else ""
            phone = user.phone if user.phone else ""
            try:
                os.makedirs(os.path.join('Loaded', (f'tg{user_id}')))
                info_json = os.path.join(f'Loaded/tg{user_id}', 'info.json')
                with open(info_json, 'w', encoding='utf-8') as f:
                    json.dump({
                        'source': 'Telegram', 
                        'tg_id': user_id, 
                        'username_tg': username, 
                        'first_name': first_name, 
                        'last_name': last_name, 
                        'mobile_phone': phone,
                        'group': name_group,
                        'country': {'title': self.country},
                        'city': {'title': self.city}
                        }, f, ensure_ascii=False)
                # download photos of user
                async for photo in self.client.iter_profile_photos(user, limit=5):
                    if photo.video_sizes:
                        continue
                    else:
                        await self.client.download_media(photo, file=f'Loaded/tg{user_id}')
                print(f'{i}: {first_name} - {last_name} - {username} - OK')
            except FileExistsError:
                print(f'{i}: {first_name} - {last_name} - {username} - File exist')
            except Exception as e:
                print(f'\n-EXCEPTION:\n{e}\n')
            if len(glob.glob('Loaded/*')) >= self.size_archive:
                filterAmbassador().makeArchive()
            count_people += 1
            if count_people >= self.count_of_peoples:
                break
        print(f'\n\tPARSER STOPED\nParser is parsed {i} members\nClient disconnected.\n')
        filterAmbassador().makeArchive()


# in v0.0.1 :
# python manage.py runserver --noreload --nothreading
