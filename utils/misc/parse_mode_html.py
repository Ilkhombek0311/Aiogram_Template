import asyncio


async def html_decoder(full_name: str):
    """
        html_decoder(full_name) Bu funksiyamiz telegram bot, aiogram peki
        uchun yozilgan foydalanuvchi nomida "<", ">" belgilar qatnashkan bo'lsa
        hato bermasligiga masul.
        :param full_name:
        :return: full_name:
        """

    # Agar foydalanuvchi nomida "<" shu belgi qatnashgan bolsa
    # Biz uni "❮" shu belgiga almashtirib qo'yamiz.
    if "<" in full_name:
        full_name = full_name.replace("<", "❮")

    # Agar foydalanuvchi nomida ">" shu belgi qatnashgan bolsa
    # Biz uni "❯" shu belgiga almashtirib qo'yamiz.
    if ">" in full_name:
        full_name = full_name.replace(">", "❯")

    return full_name
