import qrcodeT

name = "Nikita"

telegram_account = "Storozhuk"

application_msg = f"Привет, я {name}! прошу добавить меня в Кодильню, мой телеграм: http://t.me/{telegram_account}"

qrcodeT.qrcodeT(application_msg)
