#  -*- coding: utf-8 -*-
import datetime
import mimetypes
import os

import shutil
import smtplib
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtpd import COMMASPACE

subject = "Test"
text = "test"
data = [
    {
        "folder": "Arnika",
        "emails": {"b.v.omelchenko.fitis17@chdtu.edu.ua", "omelchenko1971@gmail.com"}
    }, {
        "folder": "Piven",
        "emails": "omelcenko44@gmail.com"
    }, {
        "folder": "Frau",
        "emails": "b.v.omelchenko.fitis17@chdtu.edu.ua"
    }
]

now = datetime.datetime.now()


def send_email(addr_to, msg_subj, text, files):
    addr_from = "ombogdan22@gmail.com"  # Відправник
    password = "o2000zxcvb"  # Пароль
    msg = MIMEMultipart()
    msg['From'] = addr_from
    if type(addr_to) == str:
        logger("email один")
        msg['To'] = addr_to
    else:
        logger("поштових скриньок декілька")
        assert isinstance(addr_to, set)
        msg['To'] = COMMASPACE.join(addr_to)
    num_files = len([f for f in os.listdir(files[0])
                     if os.path.isfile(os.path.join(files[0], f))])
    if int(num_files) == 0:
        logger("немає нових файлів в папці " + files[0])
    else:
        logger("додаю тему до повідомлення")
        msg['Subject'] = msg_subj
        logger("додаю текст до повідомлення")
        msg.attach(MIMEText(text, 'plain'))
        logger("додаю файли до повідомлення")
        process_attachement(msg, files)
        logger("з'єднуюсь з сервером")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        logger("входжу в акаунт")
        server.login(addr_from, password)
        logger("відправляю повідомлення")
        server.send_message(msg)
        logger("виходжу з акаунта")
        server.quit()
        copy_and_delete(files)
        logger("повідомлення успішно відіслано")


def copy_and_delete(files):
    new_folder = files[0] + "/archive" + now.strftime("/%Y-%m-%d_%H-%M")
    logger("копіюю всі файли в папку " + new_folder)
    shutil.copytree(files[0], new_folder, ignore=shutil.ignore_patterns('archive'))
    logger("видаляю всі файли з папки" + files[0])
    for the_file in os.listdir(files[0]):
        file_path = os.path.join(files[0], the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                logger("файл " + file_path + " був видалений з папки успішно")
        except Exception as e:
            logger("файл " + file_path + " не був видалений з папки")
            print(e)


def process_attachement(msg, files):
    for f in files:
        if os.path.isfile(f):
            attach_file(msg, f)
        elif os.path.exists(f):
            logger("шлях не знайдений отже це директорія")
            dir = os.listdir(f)
            for file in dir:
                logger("додаєм кожний файл директорії в повідомлення")
                attach_file(msg, f + "/" + file)


def attach_file(msg, filepath):
    try:
        filename = os.path.basename(filepath)
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(filepath, 'rb') as fp:
            logger("відкриваєм файл")
            file = MIMEBase(maintype, subtype)
            logger("додаєм вміст файла")
            file.set_payload(fp.read())
            fp.close()
            logger("вміст кодується як Base64")
            encoders.encode_base64(file)
        logger("додаєм заголовки до файлів")
        file.add_header('Content-Disposition', 'attachment', filename=filename)
        logger("додаєм файл до повідомлення")
        msg.attach(file)
    except IOError:
        logger("В папці є ще одна папка %s" % filepath)


def logger(message):
    data = open("sender.log", 'a', encoding="utf-8")
    log = data.write(now.strftime("%Y-%m-%d %H:%M:%S ") + str(message) + "\n")
    data.close()
    print(message)


def send_message(subject, data, text):
    for i in range(0, len(data), 1):
        print(data)
        print(data[i]["emails"])
        print(data[i]["folder"])
        logger(now.strftime("%Y-%m-%d %H:%M:%S") + " Чекаю 5 секунд перед відправкою повідомлення")
        time.sleep(1)
        logger("Віправляю папку " + str(data[i]["folder"]) + " на емейли " + str(data[i]["emails"]))
        send_email(data[i]["emails"], subject, text, files=[data[i]["folder"]])


send_message(subject, data, text)
