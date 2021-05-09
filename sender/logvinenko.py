import requests
message = "JJ"
requests.get("https://api.telegram.org/bot1368282448:AAHtHafsLIfMKkKGz6ySvmFFpseo_ozEs-c/sendMessage?chat_id=926584029&text={message}".format(message=message))