# (©)Codexbotz
# Recode By @lucarlossx

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_CHANNEL1,
    FORCE_SUB_CHANNEL2,
    FORCE_SUB_CHANNEL3,
    FORCE_SUB_CHANNEL4,
    FORCE_SUB_CHANNEL5,
    FORCE_SUB_CHANNEL6,
    FORCE_SUB_CHANNEL7,
    FORCE_SUB_CHANNEL8,
    FORCE_SUB_GROUP,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL1:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL1!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL1 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()
        
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali Nilai CHANNEL_ID, Nilai Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
            )
            sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL2!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL2 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_GROUP:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_GROUP)
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_GROUP dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Group Saat Ini: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali Nilai CHANNEL_ID, Nilai Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
            )
            sys.exit()
        if FORCE_SUB_CHANNEL3:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                self.invitelink5 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL3!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL3 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL4:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL4)
                self.invitelink6 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL4!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL4 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali Nilai CHANNEL_ID, Nilai Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
            )
            sys.exit()
        if FORCE_SUB_CHANNEL5:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL5)
                self.invitelink7 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL5!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL5 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL6:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL6)
                self.invitelink8 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL6!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL6 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali Nilai CHANNEL_ID, Nilai Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
            )
            sys.exit()
        if FORCE_SUB_CHANNEL7:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL7)
                self.invitelink9 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL7!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL7dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL8:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL8)
                self.invitelink10 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL8!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL8 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/L9BTX untuk Bantuan"
                )
                sys.exit()
        
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\n\nBOT Dibuat oleh @{OWNER}\nJika @{OWNER} Membutuhkan Bantuan, Silahkan Tanyakan ke https://t.me/L9BTX"
        )
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")