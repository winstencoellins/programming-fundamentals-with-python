# Final Project (Banking System with OOP)
Pada project akhir ini, kalian akan membuat sebuah sistem banking yang sangat sederhana tentunya dengan semua skill yang telah kalian dapatkan selama 3 minggu ini.

# Guide to Start the Project
Tahap - tahap yang saya tulis akan menjadi panduan bagi kalian untuk menyelesaikan project tersebut. Bacalah dengan seksama dan usahakan untuk mengerti setiap baris dari kode yang akan ditulis. <strong><em>Saya tidak akan mengupload kode yang saya tulis sendiri di git hub, melainkan saya ingin Anda untuk bisa mengkoding dengan usaha Anda sendiri</em></strong>. Anda bisa meminta bantuan saya, google, teman Anda, ataupun kerabat Anda yang memiliki pengalaman di dunia pemrograman. Good luck!

# Step 1: Setup the Project
Copy paste kode dibawah ini ke `main.py`. Function python yang dituliskan ini akan membantu mempermudah pekerjaan Anda. Jadi pastikan kalian menggunakannya saat diperlukan dan <strong><em>pastikan kalian benar - benar mengerti apa yang dilakukan kode yang dituliskan di dalam function tersebut</em></strong>.
```python
from bank import Bank
import csv
```
```python
def check_is_user(usrname, pwd):
  d = {}
  with open("user_data.csv") as csv_file:
    r = csv.DictReader(csv_file)

    for row in r:
      d[row["username"]] = row["password"]
  
  for i in d:
    if d[i] == pwd:
      return True
  return False
```
```python
def pull_account(usrname):
  lst = []
  with open("user_data.csv") as csv_file:
    r = csv.DictReader(csv_file)
  
    for row in r:
      if row["username"] == usrname:
        for i in row:
          lst.append(row[i])
        break
  return lst
```
```python
def register_account(usrname, pwd, credit):
  with open("user_data.csv", 'a') as csv_file:
    w = csv.writer(csv_file)
    w.writerow([usrname, pwd, credit])
```
```python
def has_account(usrname):
  usern = []
  with open("user_data.csv") as csv_file:
    r = csv.DictReader(csv_file)

    for row in r:
      usern.append(row["username"])

  for name in usern:
    if usrname == name:
      return True
    
  return False
```
```python
def main():
  # Code here
```
Setelah selesai melakukan copy paste dan mengerti kode - kode diatas, buatlah sebuah file baru dan berikan nama `user_data.csv`. Di dalam `user_data.csv` tuliskan tiga kata tersebut sesuai dengan yang ada pada gambar dibawah dan tekan `enter` pada keyboard Anda. <strong><em>Ingat, jangan ada satupun spasi atau code kalian akan error</em></strong>. Semua code yang akan kalian tulis akan dicode di dalam function `main()`.

CSV Output:

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/csvImage.png)

# Step 2: Finish the Starting Page
Setelah melakukan tahap 1. Di tahap 2, kalian akan membuat sebuah front-end sederhana. Buatlah satu `main` function di file `main.py` dibawah kode yang telah kalian copy paste di atas. Pada saat run, tampilan pertama kalian akan terlihat seperti gambar di bawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/startPage.png)

Pastikan user bisa memilih input yang mereka inginkan.

# Step 3: Finish the New Application Account Page
Setelah berhasil mengoutput sesuai dengan gambar diatas, selesaikanlah `Make new account`. Ketika user memilih input 1, user akan disuruh untuk memasukkan username dan password. Gunakan function `has_account()` dan `register_account()` untuk membantu pekerjaan Anda. Output akan seperti dibawah. <strong><em>Jika semua kondisi terpenuhi</em></strong>

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/newAccPageValidCondition.png)

#### Invalid Condition
1. Jika username yang diinput telah ada di `user_data.csv`, <strong><em>maka program akan menampilkan error message dan menyuruh user untuk meninput username yang belum ada</em></strong>.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/usernameInvalidCondition.png)

2. Jika password yang diinput tidak memiliki karakter lebih dari 4, <strong><em>maka program akan menampilkan error message dan menyuruh user untuk menginput kembali password yang valid</em></strong>.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/pwdInvalidCondition.png)

3. Jika credit yang diinput tidak lebih atau sama dengan 500, <strong><em>maka program akan menampilkan error message dan menyuruh user untuk menginput kembali credit yang valid</em></strong>.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/creditInvalidCondition.png)

# Step 4: Finish the Login Page
### - Login Problem
Setelah semua telah berjalan dengan baik di step 3, maka selanjutnya adalah membuat login page. Login page akan menyuruh user untuk menginput username dan password. Jika kondisi terpenuhi, maka tampilan akan seperti pada gambar di bawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/loginValidCondition.png)

#### Invalid condition
1. Jika password ataupun username salah, maka program akan menyuruh user untuk menginput kembali username dan password mereka. Apabila user tidak pernah meregister account mereka di database, maka user harus menjalankan ulang program tersebut (exit the program and re-run it). Tampilan akan seperti pada gambar di bawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/loginInvalidCondition.png)

### - Object - Oriented Programming (OOP)
Setelah berhasil menjalankan program diatas, maka ini saatnya lah untuk melakukan transisi ke file baru. Buatlah file baru yang bernama `bank.py`. Disini, kalian akan menuliskan class yang akan berhubungan langsung dengan function `main()` di `main.py`. Copy paste kode python tersebut ke dalam `bank.py`.

```python
import csv

class Bank:
  def __init__(self, name, password, credit):
    # Constructor (write your code here)

  def deposit(self, amount):
    lst = []
    self.credit += amount

    with open("user_data.csv") as csv_file:
      r = csv.DictReader(csv_file)

      for row in r:
        if self.name == row["username"]:
          row["credit"] = self.credit
        lst.append(row)

    with open("user_data.csv", "w") as csv_file:
      fieldnames = ['username', 'password', 'credit']
      w = csv.DictWriter(csv_file, fieldnames)

      w.writeheader()
      
      for i in lst:
        w.writerow(i)
          
    return self.credit

  def withdraw(self, amount):
    # Hint: Kode hampir sama persis dengan kode
    # yang berada di function deposit. Saya tidak akan memberitahu
    # secara spesifik apa yang harus diganti, tetapi kalian hanya perlu mengganti
    # "1" kode saja.

  def change_password(self, pwd):
    # Hint: Kode juga hampir sama persis dengan deposit. Hanya saja,
    # kalian perlu mengganti beberapa kode agar password user bisa terganti

  def current_info(self):
    lst = [self.name, self.password, self.credit]

    return lst
```

##### Note: If you need to refresh your memory about csv file or wanted to know how it works, click the link provided to read the documentation and try it. (https://realpython.com/python-csv/)

### - Main Page
Setelah berhasil menyelesaikan OOP, kita akan melanjutkan kembali proses ke `main.py`. Tampilan dibawah merupakan tampilan dari user yang berhasil login. Buatlah front-end yang sesuai dengan gambar dibawah atau kalian boleh mendesign tampilan sendiri dengan fitur yang sama.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/mainPage.png)

##### Note: Di tampilan main page, nama `winstenc` harus sesuai dengan nama user yang login dengan username mereka.

### - Helper Variable and Function
Disinilah kita akan menggunakan bantuan dari OOP. Buatlah satu variabel yang merupakan `object`. Function `check_is_user()` dan `pull_account()` akan membantu kalian. Pikirkan bagaimana function `pull_account()` bisa membantu kalian mengisi parameter / argumen dari `object`.

### - Deposit
Pada proses deposit, program akan menanyakan user untuk menginput berapa jumlah uang yang akan mereka deposit. Setelah deposit berhasil, program akan menampilkan output seperti yang ada pada gambar dibawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/depositFrontEnd.png)

##### Note: Ingat, ketika uang telah ditambahkan, maka data yang berada pada file `user_data.csv` juga harus berubah menjadi jumlah tersebut dengan bantuan OOP `object.deposit()` dari `bank.py`.

### - Withdrawal
Pada proses withdrawal, program akan menanyakan user untuk menginput berapa jumlah uang yang akan mereka withdraw (tarik). Setelah penarikan berhasil, program akan menampilkan output seperti yang ada pada gambar dibawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/withdrawalFrontEnd.png)

##### Note: Ingat, ketika uang telah ditarik, maka data yang berada pada file `user_data.csv` juga harus berubah menjadi jumlah tersebut dengan bantuan OOP `object.withdarwal()` dari `bank.py`.

### - Get Current Information
Pada proses get current information, user akan mendapatkan semua data informasi mengenai dirinya. Output akan ditampilkan pada gambar dibawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/accountInformationFrontEnd.png)

##### Note: Gunakan bantuan OOP `object.current_info()` dari `bank.py`.

### - Change Password
Pada proses pergantian password, user akan menginput password baru dan password dari user tersebut akan diganti seperti tampilan dibawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/changePassword.png)

#### Invalid condition
1. Jika panjang password kurang dari 4, maka tampilkan error message dan program akan menyuruh user untuk menginput kembali password baru.
2. Tambahkan error message yang menyuruh user untuk menutup program kemudian re-run jika user tidak berniat untuk mengganti password dan ingin melanjutkan transaksi.

##### Note: Ketika password diganti, data yang berada pada `user_data.csv` juga harus terganti menjadi password yang baru.

### - Log Out
Pada proses log out, program akan menampilkan front-end seperti pada gambar dibawah dan kembali ke tampilan awal seperti pada gambar yang berada di step 2.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/logout.png)

# Step 5: Exit
Pada proses exit, jika user menginput 3 nomor yang sesuai, maka program akan mengucapkan kalimat perpisahan kemudian exit. Jika input tidak sesuai dengan yang terdapat pada fitur, maka program akan mengeluarkan error message dan menyusuh user untuk menginput nomor yang ada pada fitur.

# Congratulations
Selamat kepada Anda yang telah berhasil menyelesaikan project tersebut. Ini merupakan langkah awal menuju dunia pemrograman yang lebih nyata. Program diciptakan untuk membantu mengerjakan segala sesuatu menjadi lebih mudah. Jadi yang ingin saya tanamkan kepada Anda adalah pola pikir Anda harus sama seperti seorang <strong><em>problem solver</em></strong> karena tanpa adanya kita, maka masalah di dunia tidak akan menjadi lebih mudah. Belajarlah untuk terus haus akan ilmu karena ilmu teknologi adalah ilmu yang tidak akan ada habisnya dan teknologi bukanlah ilmu mati.
