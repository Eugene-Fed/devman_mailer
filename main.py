import smtplib
import os
import json

from dotenv import load_dotenv


def load_config():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.json')

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    if not os.environ.get('MAIL_SENDER_LOGIN') or not os.environ.get('MAIL_SENDER_PASSWORD'):
        raise EnvironmentError("You should set your `.env` file. Please check README.md.")
    if os.path.exists(config_path):
        return json.load(open(config_path, "r", encoding="utf-8"))
    else:
        raise FileNotFoundError("File `config/config.json` not found. Please check README.md.")


def main():
    config = load_config()
    sender_login = os.environ['MAIL_SENDER_LOGIN']
    sender_password = os.environ['MAIL_SENDER_PASSWORD']

    server = smtplib.SMTP_SSL(config['smtp'][0]['url'], config['smtp'][0]['port'])
    server.login(sender_login, sender_password)

    ref_link = config['urls']['ref_link']
    client_name = config['clients'][0]['name']
    client_address = config['clients'][0]['mail']

    sender_name = config['mail_headers']['sender_name']
    sender_address = os.environ['MAIL_SENDER_LOGIN']
    mail_subject = config['mail_headers']['subject']

    with open('mail_text.txt', 'r', encoding="utf-8") as f:
        mail_text = f.read()
    with open('mail_template.txt', 'r', encoding="utf-8") as f:
        mail_template = f.read()

    mail_text = mail_text.replace(r'%website%', ref_link)
    mail_text = mail_text.replace(r'%friend_name%', client_name)
    mail_text = mail_text.replace(r'%my_name%', sender_name)

    letter = mail_template.format(
        from_address=sender_address,
        to_address=client_address,
        subject=mail_subject,
        text=mail_text)
    letter = letter.encode("UTF-8")

    server.sendmail(sender_address, client_address, letter)
    server.quit()


if __name__ == '__main__':
    main()


