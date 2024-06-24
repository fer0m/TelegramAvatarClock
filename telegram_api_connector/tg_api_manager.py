from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import main_config


class TelegramApiManager:
    def __init__(self, user):
        self.user = user
        self.client = TelegramClient('anon', user.api_id, user.api_hash)

    async def connect(self):
        await self.client.connect()
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.user.phone)
        return self.client

    async def authorize(self, code=None):
        if code:
            await self.client.sign_in(self.user.phone, code)
        elif self.user.secret_tg_key:
            await self.client.sign_in(password=self.user.secret_tg_key)
        return self.client

    async def change_avatar(self):
        await self.connect()
        channel_entity = await self.client.get_me(input_peer=True)
        if await self.client.is_user_authorized():
            current_photo = await self.client.get_profile_photos(channel_entity)
            if current_photo:
                await self.client(DeletePhotosRequest(current_photo))

            await self.client(UploadProfilePhotoRequest(file=await self.client.upload_file(
                file=main_config.GENERATED_AVATAR_PATH)))
        await self.client.disconnect()
