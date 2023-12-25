# devman_chat-bot-01

## Start and Config
- В корне необходимо скопировать файл `example.env` и вставить в ту же папку с именем `.env`.
- Указать корректные токены в соответствующие переменные.  
`MAIL_SENDER_LOGIN` - Логин почты с которой будут отправлены сообщения  
`TMAIL_SENDER_PASSWORD`- Пароль почты отправителя  

## Features
- Используй файл `config/config.json` для настройки реферральной ссылки, заголовков сообщения, списка клиентских данных и параметров SMPT-сервера.

## Config example
```
{
  "urls":
  {
    "ref_link": "https://dvmn.org/referrals/cHqg6YGb5iTvYMcW1rZJLctziAfOhbwepKOOHwwM/"
  },
  "mail_headers": {"sender_name": "Евгений", "subject": "Приглашение"},
  "clients": [
      {"name": "Александр", "mail": "test@mail.ru"}
  ],
  "smtp":
  [
      {"url": "smtp.yandex.ru", "port": 465}
  ]
}
```
