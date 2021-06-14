# Final Project (Banking System with OOP)
Pada project akhir ini, kalian akan membuat sebuah sistem banking yang sangat sederhana tentunya dengan semua skill yang telah kalian dapatkan selama 3 minggu ini.

# Guide to Start the Project
Tahap - tahap yang saya tulis akan menjadi panduan bagi kalian untuk menyelesaikan project tersebut. Bacalah dengan seksama dan usahakan untuk mengerti setiap baris dari kode yang akan ditulis. <strong><em>Saya tidak akan mengupload kode yang saya tulis sendiri di git hub, melainkan saya ingin Anda untuk bisa mengkoding dengan usaha Anda sendiri</em></strong>. Anda bisa meminta bantuan saya, google, teman Anda, ataupun kerabat Anda yang memiliki pengalaman di dunia pemrograman. Good luck!

# Step 1
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
Setelah selesai melakukan copy paste dan mengerti kode - kode diatas, buatlah sebuah file baru dan berikan nama `user_data.csv`. Di dalam `user_data.csv` tuliskan tiga kata tersebut sesuai dengan yang ada pada gambar dibawah.

CSV Output:
![alt_text]()

# Step 2
