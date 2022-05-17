
# Perekaman Kehadiran Daring Otomatis

Perekaman Kehadiran Daring Otomatis adalah sebuah program untuk melakukan perekaman kehadiran bagi
Mahasiswa Universitas Katolik Parahyangan. Program ini menggunakan bahasa pemrograman Python dan 
Selenium yang merupakan sebuah open-source framework untuk pengujian otomatisasi untuk browser web. 
Wajib memiliki Python dan browser Google Chrome.

## Persyaratan

1. Download ZIP proyek skripsi ini dan ekstrak filenya.
2. Buka Folder Program.
3. Install Python 3 (https://www.python.org/downloads/).
4. Install Selenium (jika belum ter-install, https://www.selenium.dev/documentation/webdriver/getting_started/install_library/).  
4.1 Buka Command Prompt  
4.2 Input command di bawah ini
	```sh
	pip install selenium
	```
5. Setup chromedriver.exe ke dalam PATH (https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).  
5.1 Buka Command Prompt.  
5.2 Input command di bawah ini (directory relatif dengan posisi chromedriver.exe di komputer anda)
	```sh
	setx PATH "%PATH%;C:Skripsi-master/Program"
	```
	
## Cara Pemakaian

1. Ubah nama file database-reinalta.properties menjadi database.ini .
2. Ubah email di bawah ini menjadi email studentportal anda.  
	```sh
	3 = sendkeys #username 2017730035@student.unpar.ac.id
	```
3. Ubah password di bawah ini menjadi password email studentportal anda.  
	```sh
	5 = sendkeys #password ******
	```
4. Save file database.ini.
5. Buka Command Prompt dengan directory file automatedTesting.py
6. Input command di bawah ini  
	```sh
	python automatedTesting.py
	```
7. Browser akan terbuka secara otomatis untuk melakukan Perekaman Kehadiran Daring Otomatis.
