import datetime


def rounding(num):
    return int(num * pow(10, 1)) / pow(10, 1)


def create_link_payments(amount, information, contract, seller_address):
    offset = datetime.timezone(datetime.timedelta(hours=3))
    time_create_link = str(datetime.datetime.now(offset)).split(".", 1)[0]
    link_payments = (f"https://t.me/TezerPlatformBot?start=X{seller_address}-{int(rounding(float(amount)) * 10)}-"
                     f"{information}-{contract}")
    return link_payments, time_create_link




