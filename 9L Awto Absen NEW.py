from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import stdiomask
import datetime


url = "https://e-learning.mtsn1malang.sch.id"
confirm = "N"
urutanKodeKelas = 1
indexKodeKelas = 0
isBrowserOpened = False
sudahConfirmAbsen = False
internetError = False
options = Options()



#LoginInfo
try :
    f=open("Info Login E-Learning.txt", "r")
except FileNotFoundError :
    f=open("Info Login E-Learning.txt", "w+")
    f.write(input("Masukkan Username : ") + ",")
    f.write(stdiomask.getpass(prompt='Masukkan Password : ', mask='*'))
f=open("Info Login E-Learning.txt", "r")
dataLogin = (f.read()).split(",")
try :
    username = dataLogin[0]
    password = dataLogin[1]
except IndexError:
    f=open("Info Login E-Learning.txt", "w+")
    f.write(input("Masukkan Username : ") + ",")
    f.write(stdiomask.getpass(prompt='Masukkan Password : ', mask='*'))
    f=open("Info Login E-Learning.txt", "r")
    dataLogin = (f.read()).split(",")
    username = dataLogin[0]
    password = dataLogin[1]

#LinkKelas
linkKelas = {
"1" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTE5MjFLOA==/SVgtTCBJUEE=/MTE5Mg==", #IPA
"2" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/Njg1R0ZNNQ==/QklORCA5TCAyMDIw/Njg1", #BIN
"3" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/ODc2MFZYTQ==/OUwgUFBLbg==/ODc2", #PPKN
"4" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/ODY2VlFENQ==/OUwgQmltYmluZ2FuICYgS29uc2VsaW5n/ODY2", #BK
"5" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/OTUySzROOA==/QklHIDlM/OTUy", #BING
"6" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTE2OEs5NQ==/OUwgT2xpbSBNQVRFTUFUSUtBIFNlbSAxIFRQIDIwMjAvMjAyMQ==/MTE2OA==", #MAT
"7" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTIxOFRLNw==/SVggTCAtIEJhaGFzYSBBcmFi/MTIxOA==", #BahasaArab
"8" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTE3OURKRg==/OUwgLSBRSA==/MTE3OQ==", #QH
"9" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/ODAySzlHTQ==/UGVuamFza2VzIDlM/ODAy", #PENJAS
"10" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTI5ODRTMw==/OUwgU0tJ/MTI5OA==", #SKI
"11" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTM1NlEyNA==/SVBTIDktTA==/MTM1Ng==", #IPS
"12" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTMxMDdENg==/OUwgUFJBS0FSWUE=/MTMxMA==", #PKY
"13" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTMyMEI4Sw==/OUwgTVRzLk4gMSBLb3RhIE1hbGFuZw==/MTMyMA==",#FQH
"14" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTM3OThIQw==/SVgtTCBBS0lEQUggQUtITEFL/MTM3OQ==", #AA
"15" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTQwN1Y5MA==/SVgtTCBLSVI=/MTQwNw==", #KIR
"16" : "https://e-learning.mtsn1malang.sch.id/studentkelas/me/MTQ1OUhTQw==/SVgtTCBTRU5JIEJVREFZQQ==/MTQ1OQ==" #SBY
}

automaticAbsenDB = {
                    "Mon" : "12, 7, 13, 3",
                    "Tue" : "14, 10, 1",
                    "Wed" : "6, 16, 4",
                    "Thu" : "2, 9, 11",
                    "Fri" : "8, 5, 15",
                    "Sat" : "17",
                    "Sun" : "17"
                    }


print(
"""
Halo, Mau absen mapel apa meng?\n
1.  IPA
2.  Bahasa Indonesia
3.  PPKN
4.  BK
5.  Bahasa Inggris
6.  MAT
7.  Bahasa Arab
8.  QH
9.  Penjaskes
10. SKI
11. IPS
12. PKY
13. FQH
14. AA
15. KIR
16. SBY
17. Home e-learning
18. Notif e-learning
19. List Tugas di e-learning
20. Ganti Username dan Password yg tersimpan
21. Otomatis (Berdasar Hari)
"""
)
kodeKelas =  str(input("Masukkan Pilihan : "))
if "," in kodeKelas:
    kodeKelasSiap = kodeKelas.split(",")
else :
    kodeKelasSiap = [kodeKelas]
if int(kodeKelasSiap[0]) == 21:
    x = datetime.datetime.now().strftime("%a")
    kodeKelasSiap = automaticAbsenDB[x].split(",")

def authPass(username, password) :
    driver.get(url)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('loginmadrasah').submit()
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(1)

akhirLoop = len(kodeKelasSiap)

while urutanKodeKelas <= akhirLoop :
    if int(kodeKelasSiap[indexKodeKelas]) == 17:
        if isBrowserOpened == True :
            pass
        elif isBrowserOpened == False:
            try:
                driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
                authPass(username, password)
                isBrowserOpened = True
            except ConnectionError:
                if internetError == False:
                    print("Ada masalah dengan internet bre")
                elif internetError == True:
                    pass
        time.sleep(1)
        driver.get("https://e-learning.mtsn1malang.sch.id/student")
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    elif int(kodeKelasSiap[indexKodeKelas]) == 18:
        if isBrowserOpened == True :
            pass
        elif isBrowserOpened == False:
            try:
                driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
                authPass(username, password)
                isBrowserOpened = True
            except ConnectionError:
                if internetError == False:
                    print("Ada masalah dengan internet bre")
                elif internetError == True:
                    pass
        time.sleep(1)
        driver.get("https://e-learning.mtsn1malang.sch.id/student/semuanotif")
    elif int(kodeKelasSiap[indexKodeKelas]) == 19:
        if isBrowserOpened == True :
            pass
        elif isBrowserOpened == False:
            try:
                driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
                authPass(username, password)
                isBrowserOpened = True
            except ConnectionError:
                if internetError == False:
                    print("Ada masalah dengan internet bre")
                elif internetError == True:
                    pass
        time.sleep(1)
        driver.get("https://e-learning.mtsn1malang.sch.id/studentmaster/tugas")
    elif int(kodeKelasSiap[indexKodeKelas]) == 20:
        print("\nUsername tersimpan saat ini : " + dataLogin[0])
        print("Password tersimpan saat ini : " + dataLogin[1] + '\n')
        f=open("Info Login E-Learning.txt", "w+")
        f.write(input("Masukkan Username Baru : ") + ",")
        newPassword = stdiomask.getpass(prompt='Masukkan Password Baru : ', mask='*')
        newPasswordToConfirm = stdiomask.getpass(prompt='Konfirmasi Password Baru : ', mask='*')
        if newPasswordToConfirm == newPassword :
            f.write(newPassword)
            print("Oke berhasil mengganti password lur")
        else:
            print("Maaf lur, Password baru dengan Konfirmasinya tidak sama")

    elif int(kodeKelasSiap[indexKodeKelas]) <= 16:
        if sudahConfirmAbsen == False:
            confirm = input("Apakah Anda Yakin (y/N)? ")
            sudahConfirmAbsen = True
        else :
            pass
        if confirm.lower() == "y":
            urutanIndexBuatAbsen = 0
            if isBrowserOpened == True :
                pass
            elif isBrowserOpened == False:
                try:
                    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                    authPass(username, password)
                    isBrowserOpened = True
                except ConnectionError:
                    if internetError == False:
                        print("Ada masalah dengan internet bre")
                    elif internetError == True:
                        pass
            time.sleep(1)
            driver.get(linkKelas[kodeKelasSiap[urutanIndexBuatAbsen]])
            time.sleep(1)
            driver.find_element_by_id('konfirmasikehadiran').click()
            time.sleep(2)

            if urutanKodeKelas == akhirLoop :
                driver.quit()
                isBrowserOpened = False
                print("""
                 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                █ ▄▄▀██ ▄▄▀██ ▄▄▄ ██ ▄▄▄██ ▀██ ████ ▄▄▀██ ▄▄▄██ ▄▄▀██ ██ █ ▄▄▀██ ▄▄▄ █▄ ▄██ ████
                █ ▀▀ ██ ▄▄▀██▄▄▄▀▀██ ▄▄▄██ █ █ ████ ▄▄▀██ ▄▄▄██ ▀▀▄██ ▄▄ █ ▀▀ ██▄▄▄▀▀██ ███ ████
                █ ██ ██ ▀▀ ██ ▀▀▀ ██ ▀▀▀██ ██▄ ████ ▀▀ ██ ▀▀▀██ ██ ██ ██ █ ██ ██ ▀▀▀ █▀ ▀██ ▀▀ █
                 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                """)

        else :
            print("""
            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
            █ ▄▄▀██ █▀▄██ ▄▄▄ █▄ ▄████ ▄▄▀█▄ ▄██ ▄▄▀█ ▄▄▀█▄▄ ▄▄█ ▄▄▀██ █████ █▀▄█ ▄▄▀██ ▀██ █
            █ ▀▀ ██ ▄▀███▄▄▄▀▀██ █████ ██ ██ ███ ▄▄▀█ ▀▀ ███ ███ ▀▀ ██ █████ ▄▀██ ▀▀ ██ █ █ █
            █ ██ ██ ██ ██ ▀▀▀ █▀ ▀████ ▀▀ █▀ ▀██ ▀▀ █ ██ ███ ███ ██ ██ ▀▀ ██ ██ █ ██ ██ ██▄ █
            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """)
    kodeKelasSiap.remove(kodeKelasSiap[0])
    urutanKodeKelas += 1
else :
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
