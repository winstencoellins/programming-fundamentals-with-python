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
Setelah selesai melakukan copy paste dan mengerti kode - kode diatas, buatlah sebuah file baru dan berikan nama `user_data.csv`. Di dalam `user_data.csv` tuliskan tiga kata tersebut sesuai dengan yang ada pada gambar dibawah dan tekan `enter` pada keyboard Anda. <strong><em>Ingat, jangan ada satupun spasi atau code kalian akan error</em></strong>

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

# Step 4: Finish the Login Page (Longest Problem)
Setelah semua telah berjalan dengan baik di step 3, maka selanjutnya adalah membuat login page. Login page akan menyuruh user untuk menginput username dan password. Jika kondisi terpenuhi, maka tampilan akan seperti pada gambar di bawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/loginValidCondition.png)

#### Invalid condition
1. Jika password ataupun username salah, maka program akan menyuruh user untuk menginput kembali username dan password mereka. Apabila user tidak pernah meregister account mereka di database, maka user harus menjalankan ulang program tersebut (exit the program and re-run it). Tampilan akan seperti pada gambar di bawah.

![alt_text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/ProjectGuide/images/loginInvalidCondition.png)
