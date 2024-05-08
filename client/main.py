from ftplib import FTP
import os
import time
from termcolor import colored
import getpass

ftp = FTP()

def clear_screen():
    os.system("clear")

def print_colored(message, color):
    print(colored(message, color))

def pause(message, color, duration=1):
    print_colored(message, color)
    time.sleep(duration)
    clear_screen()

class FTPClient:
    def __init__(self):
        self.ftp = FTP()
        self.run()

    def run(self):
        clear_screen()
        print_colored("BM402_FTP Gözde Kalman 191180046", "yellow")
        print_colored("FTP Client", "yellow")
        self.connect()
        self.main_menu()

    def connect(self):
        while True:
            server_address = input("Sunucu Adresi: ")
            server_port = input("Sunucu Portu (Varsayılan 21): ") or '21'
            try:
                self.ftp.connect(server_address, int(server_port))
                print_colored("Bağlantı Başarılı", "green")
                break
            except Exception as e:
                print_colored("Bağlantı Başarısız: " + str(e), "red")
                time.sleep(1)

        self.login()

    def login(self):
        while True:
            username = input("Kullanıcı Adı: ")
            password = getpass.getpass("Şifre: ")
            try:
                self.ftp.login(username, password)
                print_colored("Giriş Başarılı", "green")
                break
            except Exception as e:
                print_colored("Giriş Başarısız: " + str(e), "red")

    def main_menu(self):
        options = {
            "1": ("Yerel İşlemler", self.local_operations),
            "2": ("Uzak Sunucu İşlemler", self.remote_operations),
            "3": ("Dosya Yükle", self.upload_file),
            "4": ("Dosya İndir", self.download_file),
            "5": ("Çıkış Yap", self.exit_client)
        }

        while True:
            clear_screen()
            for key, (desc, _) in options.items():
                print_colored(f"{key}) {desc}", "blue")
            
            choice = input("Seçim: ")
            action = options.get(choice)
            if action:
                _, action_method = action
                action_method()
            else:
                pause("Hatalı Seçim", "red")

    def local_operations(self):
        operations = {
            "1": ("Dizin Oluştur", self.create_local_directory),
            "2": ("Dizin Sil", self.remove_local_directory),
            "3": ("Dosya Adı Değiştir", self.rename_local_file),
            "4": ("Dosya Sil", self.delete_local_file),
            "5": ("Dizin Değiştir", self.change_local_directory),
            "6": ("Dosya Listele", self.list_local_files),
            "7": ("Ana Menüye Dön", None)
        }

        self.run_operations("Yerel İşlemler", operations)

    def remote_operations(self):
        operations = {
            "1": ("Dizin Oluştur", self.create_remote_directory),
            "2": ("Dizin Sil", self.remove_remote_directory),
            "3": ("Dosya Adı Değiştir", self.rename_remote_file),
            "4": ("Dosya Sil", self.delete_remote_file),
            "5": ("Dizin Değiştir", self.change_remote_directory),
            "6": ("Dosya Listele", self.list_remote_files),
            "7": ("Ana Menüye Dön", None)
        }

        self.run_operations("Uzak Sunucu İşlemler", operations)

    def run_operations(self, menu_name, operations):
        while True:
            clear_screen()
            print_colored(menu_name, "blue")
            for key, (desc, _) in operations.items():
                print_colored(f"{key}) {desc}", "blue")

            choice = input("Seçim: ")
            if choice == "7":
                break
            action = operations.get(choice)
            if action:
                _, action_method = action
                if action_method:
                    action_method()
            else:
                pause("Hatalı Seçim", "red")

    def create_local_directory(self):
        directory_name = input("Dizin Adı: ")
        try:
            os.mkdir(directory_name)
            pause("Dizin Oluşturuldu", "green", 2)
        except Exception as e:
            pause(f"Dizin Oluşturulamadı: {str(e)}", "red")

    def remove_local_directory(self):
        directory_name = input("Dizin Adı: ")
        try:
            os.rmdir(directory_name)
            pause("Dizin Silindi", "green", 2)
        except Exception as e:
            pause(f"Dizin Silinemedi: {str(e)}", "red")

    def rename_local_file(self):
        old_name = input("Eski Dosya Adı: ")
        new_name = input("Yeni Dosya Adı: ")
        try:
            os.rename(old_name, new_name)
            pause("Dosya Adı Değiştirildi", "green", 2)
        except Exception as e:
            pause(f"Dosya Adı Değiştirilemedi: {str(e)}", "red")

    def delete_local_file(self):
        file_name = input("Dosya Adı: ")
        try:
            os.remove(file_name)
            pause("Dosya Silindi", "green", 2)
        except Exception as e:
            pause(f"Dosya Silinemedi: {str(e)}", "red")

    def change_local_directory(self):
        directory_name = input("Dizin Adı (Geri Dönmek için .. yazınız): ")
        try:
            os.chdir(directory_name)
            pause("Dizin Değiştirildi", "green", 2)
        except Exception as e:
            pause(f"Dizin Değiştirilemedi: {str(e)}", "red")

    def list_local_files(self):
        try:
            print_colored("Yerel Dizin:", "blue")
            os.system("ls")
        except Exception as e:
            pause(f"Dosya Listelenemedi: {str(e)}", "red")

    def upload_file(self):
        file_name = input("Yüklenecek Dosya Adı: ")
        try:
            with open(file_name, 'rb') as file:
                self.ftp.storbinary(f'STOR {file_name}', file)
            pause("Dosya Yüklendi", "green", 2)
        except Exception as e:
            pause(f"Dosya Yüklenemedi: {str(e)}", "red")

    def download_file(self):
        file_name = input("İndirilecek Dosya Adı: ")
        try:
            with open(file_name, 'wb') as file:
                self.ftp.retrbinary(f'RETR {file_name}', file.write)
            pause("Dosya İndirildi", "green", 2)
        except Exception as e:
            pause(f"Dosya İndirilemedi: {str(e)}", "red")

    def exit_client(self):
        self.ftp.quit()
        print_colored("Çıkış Yapılıyor", "blue")
        time.sleep(1)
        clear_screen()
        exit()

    def create_remote_directory(self):
        directory_name = input("Dizin Adı: ")
        try:
            self.ftp.mkd(directory_name)
            pause("Dizin Oluşturuldu", "green")
        except Exception as e:
            pause(f"Dizin Oluşturulamadı: {str(e)}", "red")

    def remove_remote_directory(self):
        directory_name = input("Dizin Adı: ")
        try:
            self.ftp.rmd(directory_name)
            pause("Dizin Silindi", "green")
        except Exception as e:
            pause(f"Dizin Silinemedi: {str(e)}", "red")

    def rename_remote_file(self):
        old_name = input("Eski Dosya Adı: ")
        new_name = input("Yeni Dosya Adı: ")
        try:
            self.ftp.rename(old_name, new_name)
            pause("Dosya Adı Değiştirildi", "green")
        except Exception as e:
            pause(f"Dosya Adı Değiştirilemedi: {str(e)}", "red")

    def delete_remote_file(self):
        file_name = input("Dosya Adı: ")
        try:
            self.ftp.delete(file_name)
            pause("Dosya Silindi", "green")
        except Exception as e:
            pause(f"Dosya Silinemedi: {str(e)}", "red")

    def list_remote_files(self):
        try:
            print_colored("Uzak Dizin:", "blue")
            self.ftp.dir()
        except Exception as e:
            pause(f"Dosya Listelenemedi: {str(e)}", "red")

    def change_remote_directory(self):
        directory_name = input("Dizin Adı: ")
        try:
            self.ftp.cwd(directory_name)
            pause("Dizin Değiştirildi", "green")
        except Exception as e:
            pause(f"Dizin Değiştirilemedi: {str(e)}", "red")


if __name__ == "__main__":
    FTPClient()
