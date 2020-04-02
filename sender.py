import mimetypes
import os
import smtplib
from datetime import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from smtpd import COMMASPACE
import time


def send_email(addr_to, msg_subj, files):
    addr_from = "@gmail.com"  # Відправник
    password = ""  # Пароль
    msg = MIMEMultipart()
    msg['From'] = addr_from
    if type(addr_to) == str:
        msg['To'] = addr_to
        msg['Subject'] = msg_subj  # Тема повідомлення (прописується при виклику функції)
        process_attachement(msg, files)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)  # Відправляєм повідомлення
        server.quit()  # Виходим
    else:
        assert isinstance(addr_to, list)
        msg['To'] = COMMASPACE.join(addr_to)
        msg['Subject'] = msg_subj  # Тема повідомлення (прописується при виклику функції)
        process_attachement(msg, files)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)  # Відправляєм повідомлення
        server.quit()  # Виходим


def process_attachement(msg, files):
    for f in files:
        if os.path.isfile(f): # якшо це файл то додаєм файл
            attach_file(msg, f)
        elif os.path.exists(f): #якшо щлях не знайдений значить це директорія
            dir = os.listdir(f)
            for file in dir:
                attach_file(msg, f + "/" + file)  # додаєм кожний файл директорії в повідомлення


def attach_file(msg, filepath):  # Функция по додаванню конкретного файла до повідомлення
    try:
        filename = os.path.basename(filepath)
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)
            file.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(file)  # Вміст повинен кодуваться як Base64
        file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки до файлів
        msg.attach(file)  # додаєм файл до повідомлення
    except IOError: # якщо в папці є ще одна папка то просто виводиться повідомлення про назву цієї папки
        msg = "Є папка %s" % filepath
        print(msg)

def send_message():
    all = [{'folder': 'Arnika', 'emails': ['@chdtu.edu.ua', '@gmail.com']},
           {'folder': 'Piven', 'emails': '@gmail.com'},
           {'folder': 'Frau', 'emails': '@chdtu.edu.ua'}]
    subject = "Test"
    for i in range(0, len(all), 1):
        interim_dict = all[i]
        dict = list(interim_dict.values())
        time.sleep(5) # чекать перед відправкою повідомлення 5 секунд
        #dict[1] емейли на якы потрібно відсилать повідомлення
        #dict[0] папки які потрібно відсилать
        send_email(dict[1], subject, files=[dict[0]])


send_message()
