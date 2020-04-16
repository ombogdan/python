import requests
# message = "Дякуємо, вам також"
requests.get("https://api.telegram.org/bot1107388353:AAGPbr2BS14yIbxEe6LvbepF3G6ygMZZNu8/sendMessage?chat_id=-1001336276935&text={message}".format(message=message))