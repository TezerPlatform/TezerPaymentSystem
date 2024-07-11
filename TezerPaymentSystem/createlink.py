import datetime
import json

with open(f"TezerPaymentSystem\\settings.json", "r", encoding='utf-8') as read_file:
    settings = json.load(read_file)


def create_link_payments(amount, information, contract):
    now = str(datetime.datetime.now())[:19]
    amount = int(float(amount) * 10)
    link_payments = f"https://t.me/TezerPlatformBot?start=X{settings['seller_address']}-{amount}-{information}-{contract}"
    return link_payments, now




