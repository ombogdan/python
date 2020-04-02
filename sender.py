#  -*- coding: utf-8 -*-
import mimetypes
import os
import smtplib
import sys
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtpd import COMMASPACE
import time
import shutil

subject = "Test"
text = "test"
data = [{'folder': 'Arnika', 'emails': ['@chdtu.edu.ua', '@gmail.com']},
        {'folder': 'Piven', 'emails': '@gmail.com'},
        {'folder': 'Frau', 'emails': '@chdtu.edu.ua'}]

now = datetime.datetime.now()

def send_email(addr_to, msg_subj, text, files):
    addr_from = "@gmail.com"  # Відправник
    password = ""  # Пароль
    msg = MIMEMultipart()
    msg['From'] = addr_from
    if type(addr_to) == str:
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " email один")
        msg['To'] = addr_to
    else:
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " поштових скриньок декілька")
        assert isinstance(addr_to, list)
        msg['To'] = COMMASPACE.join(addr_to)
    num_files = len([f for f in os.listdir(files[0])
                     if os.path.isfile(os.path.join(files[0], f))])
    if int(num_files) == 0:
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " немає нових файлів в папці " + files[0])
    else:
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " додаю тему до повідомлення")
        msg['Subject'] = msg_subj
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " додаю текст до повідомлення")
        msg.attach(MIMEText(text, 'plain'))
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " додаю файли до повідомлення")
        process_attachement(msg, files)
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " з'єднуюсь з сервером")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " входжу в акаунт")
        server.login(addr_from, password)
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " відправляю повідомлення")
        server.send_message(msg)
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " виходжу з акаунта")
        server.quit()
        copy_and_delete(files)
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " повідомлення успішно відіслано")


def copy_and_delete(files):
    new_folder = files[0] + "/archive" + now.strftime("/%Y-%m-%d_%H-%M")
    print(now.strftime("%Y-%m-%d %H:%M:%S") + " копіюю всі файли в папку " + new_folder)
    shutil.copytree(files[0], new_folder, ignore=shutil.ignore_patterns('archive'))
    print(now.strftime("%Y-%m-%d %H:%M:%S") + " видаляю всі файли з папки" + files[0])
    for the_file in os.listdir(files[0]):
        file_path = os.path.join(files[0], the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(now.strftime("%Y-%m-%d %H:%M:%S") + " файл " + file_path + " був видалений з папки успішно")
        except Exception as e:
            print(now.strftime("%Y-%m-%d %H:%M:%S") + " файл " + file_path + " не був видалений з папки")
            print(e)


def process_attachement(msg, files):
    for f in files:
        if os.path.isfile(f):
            attach_file(msg, f)
        elif os.path.exists(f):
            print(now.strftime("%Y-%m-%d %H:%M:%S") + " шлях не знайдений отже це директорія")
            dir = os.listdir(f)
            for file in dir:
                print(now.strftime("%Y-%m-%d %H:%M:%S") + " додаєм кожний файл директорії в повідомлення")
                attach_file(msg, f + "/" + file)


def attach_file(msg, filepath):
        try:
            filename = os.path.basename(filepath)
            ctype, encoding = mimetypes.guess_type(filepath)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            with open(filepath, 'rb') as fp:
                print(now.strftime("%Y-%m-%d %H:%M:%S") + " відкриваєм файл")
                file = MIMEBase(maintype, subtype)
                print(now.strftime("%Y-%m-%d %H:%M:%S") + " додаєм вміст файла")
                file.set_payload(fp.read())
                fp.close()
                print(now.strftime("%Y-%m-%d %H:%M:%S") + " вміст кодується як Base64")
                encoders.encode_base64(file)
            print(now.strftime("%Y-%m-%d %H:%M:%S") + " додаєм заголовки до файлів")
            file.add_header('Content-Disposition', 'attachment', filename=filename)
            print(now.strftime("%Y-%m-%d %H:%M:%S") + " додаєм файл до повідомлення")
            msg.attach(file)
        except IOError:
            print(now.strftime("%Y-%m-%d %H:%M:%S") + " в папці є ще одна папка %s" % filepath)

def send_message(subject, data, text):
    old_stdout = sys.stdout
    sys.stdout = open("sender.log", 'a', encoding='utf-8')
    for i in range(0, len(data), 1):
        interim_dict = data[i]
        dict = list(interim_dict.values())
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " Чекаю 5 секунд перед відправкою повідомлення")
        time.sleep(5)
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " Віправляю папку " + str(dict[0]) + " на емейли " + str(dict[1]))
        send_email(dict[1], subject, text, files=[dict[0]])


send_message(subject, data, text)
