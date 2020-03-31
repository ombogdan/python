import mimetypes
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtpd import COMMASPACE


def send_email(addr_to, msg_subj, files):
    addr_from = "@gmail.com"  # Отправитель
    password = ""  # Пароль

    msg = MIMEMultipart()
    msg['From'] = addr_from
    if type(addr_to) == str:
        msg['To'] = addr_to
        msg['Subject'] = msg_subj  # Тема сообщения
        process_attachement(msg, files)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Выходим
    else:
        assert isinstance(addr_to, list)
        msg['To'] = COMMASPACE.join(addr_to)
        msg['Subject'] = msg_subj  # Тема сообщения
        process_attachement(msg, files)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Выходим


def process_attachement(msg, files):
    for f in files:
        if os.path.isfile(f):
            attach_file(msg, f)
        elif os.path.exists(f):
            dir = os.listdir(f)
            for file in dir:
                attach_file(msg, f + "/" + file)  # ...добавляем каждый файл к сообщению


def attach_file(msg, filepath):  # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)
    ctype, encoding = mimetypes.guess_type(filepath)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        with open(filepath) as fp:  # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
            fp.close()  # После использования файл обязательно нужно закрыть
    else:  # Неизвестный тип файла
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
            file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
            fp.close()
            encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
    file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки
    msg.attach(file)  # Присоединяем файл к сообщению


def send_message():
    all = [{'folder': 'Arnika', 'emails': ['@gmail.com', '@chdtu.edu.ua', '@gmail.com']},
           {'folder': 'Piven', 'emails': '@gmail.com'},
           {'folder': 'Frau', 'emails': '@chdtu.edu.ua'}]
    for i in range(0, len(all), 1):
        interim_dict = all[i]
        dict = list(interim_dict.values())
        send_email(dict[1], "Test", files=[dict[0]])


send_message()
