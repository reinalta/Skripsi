
# Perekaman Kehadiran Daring Otomatis

Perekaman Kehadiran Daring Otomatis adalah sebuah program untuk melakukan perekaman kehadiran bagi
Mahasiswa dan Dosen Universitas Katolik Parahyangan. Program ini menggunakan bahasa pemrograman Python dan 
Selenium yang merupakan sebuah open-source framework untuk pengujian otomatisasi untuk browser web.

## Persyaratan

1. Memiliki browser Google Chrome (link untuk mendownload: https://www.google.com/chrome/).
2. Memiliki Python3 (link untuk mendownload: https://www.python.org/downloads/).
3. Install Selenium (jika belum ter-install).  
   Input command di bawah ini pada Command Prompt :
	```sh
	pip install selenium
	```
4. Chromedriver.exe sudah disediakan dengan versi 104.0.5112.79 , Sesuaikan chromedriver.exe dengan 
   versi Browser Google Chrome masing-masing (link untuk download: https://chromedriver.chromium.org/downloads

## Cara Pemakaian

Setelah kebutuhan perangkat lunak dan instalasi sudah terpenuhi semua. Berikut ini cara menjalankan 
program :

--Ketentuan Untuk Mahasiswa--
1. Buka Folder Program dan lakukan perubahan pada file database.ini seperti ketentuan dibawah ini.
2. Ubah email di bawah ini ("2017730035@student.unpar.ac.id") sesuai email milik anda untuk melakukan perekaman kehadiran daring.  
	```sh
	3 = sendkeys #username 2017730035@student.unpar.ac.id
	```
3. Ubah password di bawah ini ("12345") menjadi password email anda.  
	```sh
	5 = sendkeys #password 12345
	```
4. Save file database.ini.
5. Buka Command Prompt dengan directory file automatedTesting.py
6. Input command di bawah ini pada comman prompt
	```sh
	python automatedTesting.py
	```
7. Browser akan terbuka secara otomatis untuk melakukan Perekaman Kehadiran Daring Otomatis.

--Ketentuan Untuk Dosen--
1. Hapus script pada file database.ini
2. Copy dan Paste script dibawah ini pada file database.ini
	```sh
	[database_config]
	1 = open https://akuhadir.unpar.ac.id
	2 = sendkeys #username 2017730035@student.unpar.ac.id
	3 = click #next_login
	4 = sendkeys #password 12345
	5 = click button[name=submit]
	6 = click a[href='https://akuhadir.unpar.ac.id/absensi?tab=tab2']
	7 = click a[onclick='checkin_home()']
	```
3. Ubah email di bawah ini ("2017730035@student.unpar.ac.id") sesuai email milik anda untuk melakukan perekaman kehadiran daring.  
	```sh
	2 = sendkeys #username 2017730035@student.unpar.ac.id
	```
4. Ubah password di bawah ini ("12345") menjadi password email anda.  
	```sh
	4 = sendkeys #password 12345
	```
5. Save file database.ini.
6. Buka Command Prompt dengan directory file automatedTesting.py
7. Input command di bawah ini pada comman prompt
	```sh
	python automatedTesting.py
	```
8. Browser akan terbuka secara otomatis untuk melakukan Perekaman Kehadiran Daring Otomatis.

