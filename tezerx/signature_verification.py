import datetime
import os
import sys
from Crypto.Hash import SHA256  # pip install pycryptodome
from Crypto.PublicKey import RSA  # --^
from Crypto.Signature import pkcs1_15  # --^

script_dir = os.path.dirname(sys.argv[0])
with open(f"{script_dir}\\TezerPaymentSystem\\tezerx\\public.key", "rb") as k:
    public_key = RSA.importKey(k.read())  # Получение public.key от контракта TezerX


def days_to_seconds(days):
    return days * 24 * 60 * 60


def hours_to_seconds(hours):
    return hours * 60 * 60


def minutes_to_seconds(minutes):
    return minutes * 60


def verify_signature(check, time_button_press, amount, information_login, use_contract, seller_address,
                     checking_information):
    try:
        message_str, signature_str = check.split("/", 1)
        (type_transaction,
         logo, contract,
         buy_address,
         sell_address,
         amount_str,
         information,
         time_transaction) = message_str.split(
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
            if contract.lower() == use_contract:
                if float(amount) == float(amount_str):
                    if seller_address == sell_address:
                        if checking_information:
                            if information == information_login:
                                return True
                            else:
                                return "The information does not match"
                        elif not checking_information:
                            return True
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
