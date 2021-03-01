import shutil
import os
import PySimpleGUI as sg

layout = [[sg.Text("""Salutare,
                   
Aplicația aceasta te va ajuta să muți toate fișierele de pe Desktop-ul tău într-un folder din Local Disk (D:)
Fișierele pot fi găsite în locația: 'D:/Fisiere Desktop/'

Dorești să muți toate fișierele în foldere ordonate?""")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Desktop Cleaner", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    if event == "OK":
        # Cream directorul in care vrem sa adaugam fisierele
        director = 'Fisiere Desktop'
        director_pdf = 'Documente pdf'
        director_doc = 'Documente word'
        director_img = 'Imagini'
        director_video = 'Video'
        director_audio = 'Audio'
        director_exe = 'Programe'
        director_zip = 'Arhive'
        dir_radacina = 'D:/'
        path_radacina = os.path.join(dir_radacina, director)

        try:
            os.mkdir(path_radacina)
        except OSError:
            pass

        # In directorul creat vom adauga si celelalte foldere
        try:
            dir_parinte = 'D:\\Fisiere Desktop\\'
        except:
            dir_parinte = 'C:\\Fisiere Desktop\\'
        path_pdf = os.path.join(dir_parinte, director_pdf)
        path_doc = os.path.join(dir_parinte, director_doc)
        path_img = os.path.join(dir_parinte, director_img)
        path_video = os.path.join(dir_parinte, director_video)
        path_audio = os.path.join(dir_parinte, director_audio)
        path_exe = os.path.join(dir_parinte, director_exe)
        path_zip = os.path.join(dir_parinte, director_zip)

        try:
            os.mkdir(path_pdf)
            os.mkdir(path_doc)
            os.mkdir(path_img)
            os.mkdir(path_video)
            os.mkdir(path_audio)
            os.mkdir(path_exe)
            os.mkdir(path_zip)
        except OSError:
            pass

        # Adaugam sursa de unde luam fisierele
        sursa = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        sursa = str(sursa) + "\\"

        # Adaugam destinatia pentru fiecare extensie in parte
        destinatia_pdf = dir_parinte + director_pdf
        destinatia_doc = dir_parinte + director_doc
        destinatia_img = dir_parinte + director_img
        destinatia_video = dir_parinte + director_video
        destinatia_audio = dir_parinte + director_audio
        destinatia_exe = dir_parinte + director_exe
        destinatia_zip = dir_parinte + director_zip

        # Cream o bucla care sa ia fiecare fisier din sursa si sa il adauge in ficare folder in parte
        for i in os.listdir(sursa):  # cautare fisier cu extensia data pe HDD
            e = os.path.splitext(i)[-1]
            if e == '.pdf':
                try:
                    shutil.move((sursa + f'{i}'), destinatia_pdf)
                except OSError as error:
                    print(error)

            elif (e == '.docx') or (e == '.doc') or (e == '.rtf') or (e == '.txt') or (e == '.ppt') or (e == '.pptx')\
                    or (e == '.pub') or (e == '.xls') or (e == '.xlsx') or (e == '.odp'):
                try:
                    shutil.move((sursa + f'{i}'), destinatia_doc)
                except OSError as error:
                    print(error)

            elif (e == '.jpg') or (e == '.jpeg') or (e == '.png') or (e == '.bmp') or (e == '.gif') or (e == '.svg'):
                try:
                    shutil.move((sursa + f'{i}'), destinatia_img)
                except OSError as error:
                    print(error)

            elif (e == '.mp3') or (e == '.wma') or (e == '.wav') or (e == '.au') or (e == '.aiff') or (e == '.flac')\
                    or (e == '.ogg'):
                try:
                    shutil.move((sursa + f'{i}'), destinatia_audio)
                except OSError as error:
                    print(error)

            elif (e == '.mp4') or (e == '.avi') or (e == '.mkv') or (e == '.wmv') or (e == '.mov') or (e == '.mpg')\
                    or (e == '.mpeg'):
                try:
                    shutil.move((sursa + f'{i}'), destinatia_video)
                except OSError as error:
                    print(error)

            elif e == '.exe':
                try:
                    shutil.move((sursa + f'{i}'), destinatia_exe)
                except OSError as error:
                    print(error)

            elif (e == '.zip') or (e == '.rar'):
                try:
                    shutil.move((sursa + f'{i}'), destinatia_zip)
                except OSError as error:
                    print(error)
            else:
                print(f'{i} nu are o extensie care poate fi utilizata de program')
    else:
        event == sg.WIN_CLOSED
    break
window.close()
