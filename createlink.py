import datetime


def rounding(num):
    return int(num * pow(10, 1)) / pow(10, 1)


def create_link_payments(amount, information, contract, seller_address):
    link_payments = (f"https://t.me/TezerPlatformBot?start=X{seller_address}-{int(rounding(float(amount)) * 10)}-"
                     f"{information}-{contract}")
    return link_payments, str(datetime.datetime.now())[:19]




