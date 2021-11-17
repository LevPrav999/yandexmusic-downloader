# -*- coding: utf-8 -*-
import os
import json
import yandex_music  # pip install yandex_music
import time
from colorama import Fore  # pip install colorama


def main():
    os.system('cls')
    os.system("title Yandex Music Downloader - start")
    try:

        if "run" not in os.listdir():
            os.system("mkdir run")

        if "settings.json" not in os.listdir("./run/"):
            os.system("cd ..")

            text_file = open("settings.json", "w")
            text_file.write("""{"email": "", "password": ""}""")
            text_file.close()

            os.replace("settings.json", "./run/settings.json")

    except Exception as error:
        print(f"{error}")
    time.sleep(4)

    with open("./run/settings.json", 'r') as f:
        settings = json.load(f)

    if settings["email"] == "":
        print(f"Аккаунт яндекс музыки не обнаружен!")
        print(f"Давайте заполним ваши данные!")
        email = str(input(f"Ваш E-mail: "))
        settings["email"] = email

    if settings["password"] == "":
        password = str(input(f"Ваш пароль: "))
        settings["password"] = password

    try:
        try:
            client = yandex_music.Client.from_credentials(f"{settings['email']}", f"{settings['password']}")
        except:
            os.system('cls')
            print(f"Аккаунт яндекс музыки введен неверно. Перезапустите программу!")

            settings["password"] = ""
            settings["email"] = ""

            with open("./run/settings.json", 'w') as f:
                json.dump(settings, f)

            time.sleep(120)

        os.system('cls')
        print(f"{Fore.RESET} {Fore.GREEN}Успешно авторизованы")
        time.sleep(0.5)
        print(f"{Fore.RESET} {Fore.GREEN}Скачивание начнется через 1 секунду")
        time.sleep(1)

    except:
        print(f"{Fore.RESET} {Fore.RED}ОШИБКА! Данные неверные!")

    with open("./run/settings.json", 'w') as f:
        json.dump(settings, f)

    os.system('cls')
    if "downloads" not in os.listdir():
        os.system("mkdir downloads")

    os.system("cd ./downloads")

    for i in enumerate(client.users_likes_tracks(), 0):

        track = i[1].fetch_track()
        tracktitle = track.title.strip("'!?,.\\")

        try:

            if f"{tracktitle}.mp3" not in os.listdir("./downloads/"):
                track.download(f'./downloads/{tracktitle}.mp3')

        except:
            print(f"{Fore.RESET} {Fore.RED}Трек с названием {tracktitle} не скачан!" + Fore.RESET)

        art = []
        for g in enumerate(track.artists, 0):
            art.append(str(g[1]['name']))
            
        print(
            f"{Fore.RESET}Трек с названием{Fore.GREEN} {track.title}{Fore.RESET} скачан!"+
            f" | Артисы: {Fore.YELLOW} {', '.join(art)}\n{Fore.RESET}"+
            "Скачано: {Fore.CYAN}{i}/{len(client.users_likes_tracks())}\n\n"
            + Fore.RESET
        )

        art.clear()

    time.sleep(10)
    os.system('cls')
    print(f"{Fore.RESET}{Fore.GREEN}УСПЕШНО СКАЧАНО!")


if __name__ == '__main__':
    main()
