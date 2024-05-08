from ftplib import FTP
import time
from termcolor import colored
import getpass
import os

ftp = FTP('')


def main():

    uzak = Uzak()
    os.system("clear")
    print(colored("BM402_FTP Gözde Kalman 191180046", "yellow"))
    print(colored("FTP Client", "yellow"))
    print(colored("Sunucuya Bağlan", "yellow"))
    uzak.connect()
    print(colored("Sunucuya Giriş Yap", "blue"))
    uzak.login()
    common = Common()
    yerel = Yerel()
    os.system("clear")
    donguBilgi()
    while True:
        secim1 = input("Seçim: ")
        if secim1 == "1":
            os.system("clear")
            yerelBilgi()
        elif secim1 == "2":
            os.system("clear")
            uzakBilgi()
        elif secim1 == "3":
            yerel.dosyaListeleme()
            uzak.dosyaListeleme()
            common.dosyaYukle()
        elif secim1 == "4":
            yerel.dosyaListeleme()
            uzak.dosyaListeleme()
            common.dosyaIndir()
        elif secim1 == "5":
            print(colored("Çıkış Yapılıyor", "blue"))
            time.sleep(1)
            os.system("clear")
            break
        else:
            print(colored("Hatalı Seçim", "red"))
            time.sleep(1)
            os.system("clear")
            donguBilgi()
            continue
        while secim1 == "1":
            secim2 = input("Seçim: ")
            if secim2 == "1":
                yerel.dizinOlusturma()
            elif secim2 == "2":
                yerel.dizinSilme()
            elif secim2 == "3":
                yerel.dosyaAdıDegistirme()
            elif secim2 == "4":
                yerel.dosyaSilme()
            elif secim2 == "5":
                yerel.dizinDegistirmek()
            elif secim2 == "6":
                yerel.dosyaListeleme()
            elif secim2 == "7":
                os.system("clear")
                donguBilgi()
                break
            else:
                print(colored("Hatalı Seçim", "red"))
                time.sleep(1)
                os.system("clear")
                donguBilgi()
                break
        while secim1 == "2":
            secim2 = input("Seçim: ")
            if secim2 == "1":
                uzak.dizinOlusturma()
            elif secim2 == "2":
                uzak.dizinSilme()
            elif secim2 == "3":
                uzak.dosyaAdıDegistirme()
            elif secim2 == "4":
                uzak.dosyaSilme()
            elif secim2 == "5":
                uzak.dizinDegistirmek()
            elif secim2 == "6":
                uzak.dosyaListeleme()
            elif secim2 == "7":
                os.system("clear")
                donguBilgi()
                break
            else:
                print(colored("Hatalı Seçim", "red"))
                time.sleep(1)
                os.system("clear")
                donguBilgi()
                break


class Common:
    def dosyaYukle(self):
        try:
            dosyaadi = input("Yüklenecek Dosya Adı: ")
            ftp.storbinary('STOR '+dosyaadi, open(dosyaadi, 'rb'))
            print(colored("Dosya Yüklendi", "green"))
            time.sleep(5)
        except:
            print(colored("Dosya Yüklenemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            donguBilgi()

    def dosyaIndir(self):
        try:
            dosyaadi = input("İndirilecek Dosya Adı: ")
            dosya = open(dosyaadi, 'wb')
            ftp.retrbinary('RETR ' + dosyaadi, dosya.write, 1014)
            print(colored("Dosya İndirildi", "green"))
            time.sleep(5)
        except:
            print(colored("Dosya İndirilemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            donguBilgi()


# yerel

class Yerel:
    def dizinOlusturma(self):
        try:
            dizinadi = input("Dizin Adı: ")
            os.mkdir(dizinadi)
            print(colored("Dizin Oluşturuldu", "green"))
            time.sleep(5)
        except:
            print(colored("Dizin Oluşturulamadı", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            yerelBilgi()

    def dizinSilme(self):
        try:
            dizinadi = input("Dizin Adı: ")
            os.rmdir(dizinadi)
            print(colored("Dizin Silindi", "green"))
            time.sleep(5)
        except:
            print(colored("Dizin Silinemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            yerelBilgi()

    def dosyaAdıDegistirme(self):
        try:
            eskiDosyaAdi = input("Eski Dosya Adı: ")
            yeniDosyaAdi = input("Yeni Dosya Adı: ")
            os.rename(eskiDosyaAdi, yeniDosyaAdi)
            print(colored("Dosya Adı Değiştirildi", "green"))
            time.sleep(5)
        except:
            print(colored("Dosya Adı Değiştirilemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            yerelBilgi()

    def dosyaSilme(self):
        try:
            dosyaadi = input("Dosya Adı: ")
            os.remove(dosyaadi)
            print(colored("Dosya Silindi", "green"))
            time.sleep(5)
        except:
            print(colored("Dosya Silinemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            yerelBilgi()

    def dizinDegistirmek(self):
        try:
            dizin = input("Dizin Adı(Geri Dönmek için .. yazınız): ")
            os.chdir(dizin)
            print(colored("Dizin Değiştirildi", "green"))
            time.sleep(5)
        except:
            print(colored("Dizin Değiştirilemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            yerelBilgi()

    def dosyaListeleme(self):
        try:
            print(colored("Yerel Dizin:", "blue"))
            os.system("ls")
        except:
            print(colored("Dosya Listelenemedi", "red"))
            time.sleep(1)

# uzak


class Uzak:
    def connect(self):
        try:
            url = input("Sunucu Adresi: ")
            port = input("Sunucu Portu(Varsayılan 21): ")
            ftp.connect(url, int(port))
            print(colored("Bağlantı Başarılı", "green"))
        except:
            print(colored("Bağlantı Başarısız...\nTekrar Deneyin", "red"))
            time.sleep(1)
            self.connect()

    def login(self):
        try:
            name = input("Kullanıcı Adı: ")
            password = getpass.getpass("Şifre: ")
            ftp.login(name, password)
            print("Giriş Başarılı")
            time.sleep(1)
        except:
            print(colored("Giriş Başarısız...\nTekrar Deneyin", "red"))
            time.sleep(1)
            self.login()

    def dizinOlusturma(self):
        try:
            dizinadi = input("Dizin Adı: ")
            ftp.mkd(dizinadi)
            print(colored("Dizin Oluşturuldu", "green"))
            time.sleep(1)
        except:
            print(colored("Dizin Oluşturulamadı", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            uzakBilgi()

    def dizinSilme(self):
        try:
            dizinadi = input("Dizin Adı: ")
            ftp.rmd(dizinadi)
            print(colored("Dizin Silindi", "green"))
            time.sleep(1)
        except:
            print(colored("Dizin Silinemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            uzakBilgi()

    def dosyaAdıDegistirme(self):
        try:
            eskiDosyaAdi = input("Eski Dosya Adı: ")
            yeniDosyaAdi = input("Yeni Dosya Adı: ")
            ftp.rename(eskiDosyaAdi, yeniDosyaAdi)
            print(colored("Dosya Adı Değiştirildi", "green"))
            time.sleep(1)
        except:
            print(colored("Dosya Adı Değiştirilemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            uzakBilgi()

    def dosyaSilme(self):
        try:
            dosyaadi = input("Dosya Adı: ")
            ftp.delete(dosyaadi)
            print(colored("Dosya Silindi", "green"))
            time.sleep(1)
        except:
            print(colored("Dosya Silinemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            uzakBilgi()

    def dosyaListeleme(self):
        try:
            print(colored("Uzak Dizin:", "blue"))
            ftp.dir()
        except:
            print(colored("Dosya Listelenemedi", "red"))
            time.sleep(1)

    def dizinDegistirmek(self):
        try:
            dizin = input("Dizin Adı: ")
            ftp.cwd(dizin)
            print(colored("Dizin Değiştirildi", "green"))
            time.sleep(1)
        except:
            print(colored("Dizin Değiştirilemedi", "red"))
            time.sleep(1)
        finally:
            os.system("clear")
            uzakBilgi()


def donguBilgi():
    print(colored("FTP Client", "blue"))
    print(colored("1) Yerel İşlemler", "blue"))
    print(colored("2) Uzak Sunucu İşlemler", "blue"))
    print(colored("3) Dosya Yükle", "blue"))
    print(colored("4) Dosya İndir", "blue"))
    print(colored("5) Çıkış Yap", "red"))


def yerelBilgi():
    print(colored("Yerel İşlemler", "blue"))
    print(colored("1) Dizin Oluştur", "blue"))
    print(colored("2) Dizin Sil", "blue"))
    print(colored("3) Dosya Adı Değiştir", "blue"))
    print(colored("4) Dosya Sil", "blue"))
    print(colored("5) Dizin Değiştir", "blue"))
    print(colored("6) Dosya Listele", "blue"))
    print(colored("7) Ana Menüye Dön", "blue"))


def uzakBilgi():
    print(colored("Uzak Sunucu İşlemler", "blue"))
    print(colored("1) Dizin Oluştur", "blue"))
    print(colored("2) Dizin Sil", "blue"))
    print(colored("3) Dosya Adı Değiştir", "blue"))
    print(colored("4) Dosya Sil", "blue"))
    print(colored("5) Dizin Değiştir", "blue"))
    print(colored("6) Dosya Listele", "blue"))
    print(colored("7) Ana Menüye Dön", "blue"))


main()
