import smtplib
import time
import requests
import os
import json
import telegram
import logging

from dotenv import load_dotenv


def main():
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)

    ref_link = r'https://dvmn.org/referrals/cHqg6YGb5iTvYMcW1rZJLctziAfOhbwepKOOHwwM/'
    friend_name = r'Александр'
    my_name = r'Юджин'
    from_address = r'me@e-fed.ru'
    to_address = r'petr@yandex.ru'
    mail_subject = r'Приглашение!'

    with open('mail_text.txt', 'r', encoding="utf-8") as f:
        mail_text = f.read()
    with open('mail_template.txt', 'r', encoding="utf-8") as f:
        mail_template = f.read()

    mail_text = mail_text.replace(r'%website%', ref_link)
    mail_text = mail_text.replace(r'%friend_name%', friend_name)
    mail_text = mail_text.replace(r'%my_name%', my_name)

    letter = mail_template.format(
        from_address=from_address,
        to_address=to_address,
        subject=mail_subject,
        text=mail_text)
    letter = letter.encode("UTF-8")
    print(letter)


if __name__ == '__main__':
    main()


