
# Perekaman Kehadiran Daring Otomatis

Perekaman Kehadiran Daring Otomatis adalah sebuah program untuk melakukan perekaman kehadiran bagi
Mahasiswa Universitas Katolik Parahyangan. Program ini menggunakan bahasa pemrograman Python dan 
Selenium yang merupakan sebuah open-source framework untuk pengujian otomatisasi untuk browser web.

## Persyaratan

1. Download ZIP proyek skripsi ini dan ekstrak filenya.
2. Buka Folder Folder Program.
3. Install Python 3 (https://www.python.org/downloads/)
4. Install Selenium (jika belum ter-install).  
5.1 Buka Command Prompt  
5.2 Input command di bawah ini
	```sh
	pip install selenium
	```
6. Setup chromedriver.exe ke dalam PATH.  
6.1 Buka Command Prompt.  
6.2 Input command di bawah ini (directory relatif dengan posisi chromedriver.exe di komputer anda)
	```sh
	setx PATH "%PATH%;C:Skripsi-master/Program"
	```


If you see an error that says unrecognized command, something like this...

```
'java' is not recognized as an internal or external command,
operable program or batch file.
```

... then you have to follow these steps:

1. You need to [download the Java Runtime Environment](https://www.java.com/en/download/)
to run this program.
2. You **may** need to set the path. If so, follow [this instruction](https://docs.oracle.com/javase/tutorial/essential/environment/paths.html)

## Usage

Once you have Java ready, take the jar from release page, then general usage is
as follow:

```
usage: java -jar BooksCrawler.jar
 -c,--crawler <arg>   crawler class to use (e.g. GramediaCrawler)
 -f,--from <arg>      page number to start from, defaults to 1
 -p,--perpage <arg>   number of items per page, defaults to 100
 -t,--to <arg>        page number to end to, defaults to 2
```

BooksCrawler will save to `output.csv`, appending to bottom if the file already
exists. The thumbnail will be saved to the same name as recorded in the server.
Refer to the CSV for each book thumbnail file name.

### Usage: GramediaCrawler

The [Gramedia's Buku Category](https://www.gramedia.com/categories/buku) has
collection of 68,904 products. Recommended usage to crawl this collection is
to take chunk of 100 books each, repeated 690 times.

Here is example of taking the first chunk:

```sh
$ java -jar BooksCrawler.jar -c GramediaCrawler -f 1 -t 1 -p 100
```

You may take several chunks at once. For example, here's how to take the 2nd
and 3rd chunk at once:

```sh
$ java -jar BooksCrawler.jar -c GramediaCrawler -f 2 -t 3 -p 100
```

Continue until the last chunk:

```sh
$ java -jar BooksCrawler.jar -c GramediaCrawler -f 690 -t 690 -p 100
```

When retrieval fails for one chunk, retry with smaller chunks.

For each chunk, it is recommended to start in a fresh directory, since it will
append `output.csv`.
