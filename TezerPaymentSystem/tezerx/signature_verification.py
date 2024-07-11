import json
import datetime
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


with open("TezerPaymentSystem/tezerx/public.key", "rb") as k:
    public_key = RSA.importKey(k.read())


def days_to_seconds(days):
    return days * 24 * 60 * 60


def hours_to_seconds(hours):
    return hours * 60 * 60


def minutes_to_seconds(minutes):
    return minutes * 60


with open(f"TezerPaymentSystem\\settings.json", "r", encoding='utf-8') as read_file:
    settings = json.load(read_file)


def verify_signature(check, time_button_press, amount, information_login):
    try:
        message_str, signature_str = check.split("/", 1)
        type_transaction, logo, contract, buy_address, sell_address, amount_str, information, time_transaction = message_str.split(
            "-", 7)

        signature = bytes.fromhex(signature_str)
        message_byte = str.encode(message_str)
        h = SHA256.new(message_byte)

        pkcs1_15.new(public_key).verify(h, signature)

        time_delta = (datetime.datetime.strptime(time_transaction, '%Y-%m-%d %H:%M:%S'))
        time_button_press_delta = (datetime.datetime.strptime(time_button_press, '%Y-%m-%d %H:%M:%S'))
        delta = (time_delta - time_button_press_delta)
        difference_second = (days_to_seconds(delta.days) +
                                 minutes_to_seconds(
                                     ((delta.seconds // 60) if delta.days >= 0 else (-delta.seconds // 60)) % 60) +
                                 hours_to_seconds((delta.seconds if delta.days >= 0 else -delta.seconds) // 3600) +
                                 delta.seconds)

        if int(difference_second) > 0:
            if contract.lower() == settings["contract_default"]:
                if float(amount) == float(amount_str):
                    if settings["seller_address"] == sell_address:
                        if settings["сheck_information"]:
                            if information == settings["information_default"]:
                                return True
                            else:
                                return "The information does not match"
                        elif not settings["сheck_information"]:
                            if information == information_login:
                                return True
                            else:
                                return "The information does not match"
                    else:
                        return "The seller's address does not match"
                else:
                    return "The number of tokens does not match"
            else:
                return "The payment contract does not match"
        else:
            return "CodeCheck is not relevant"
    except (ValueError, TypeError):
        return "The signature is not authentic"

