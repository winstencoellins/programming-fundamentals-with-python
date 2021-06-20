from bank import Bank
import csv
import time

# Memeriksa apakah username dan password yang diinput oleh user benar
# Return True: jika password benar
# Return False: jika password salah
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

# Fungsi ini bertujuan untuk menarik data dari user_data.csv sesuai dengan username dan
# password yang digunakan untuk login dan mengembalikan sebuah list yang akan digunakan
# untuk mengisi parameter dari object Bank
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

# Fungsi ini bertujuan untuk meregistrasi username, password, dan credit ke dalam
# file user_data.csv apabila semua kondisi terpenuhi pada saat user memilih 
# "make a new account"
def register_account(usrname, pwd, credit):
  with open("user_data.csv", 'a') as csv_file:
    w = csv.writer(csv_file)
    w.writerow([usrname, pwd, credit])

# Fungsi ini bertujuan untuk memeriksa apakah username yang diisi oleh user
# telah ada di dalam file user_data.csv.
# Return True: jika username telah ada di dalam file user_data.csv
# Return False: jika username belum ada di dalam file user_data.csv
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

def main():
  usr_cond = True
  while usr_cond:
    print("=" * 10 + " CHI e-BANKING SYSTEM " + "=" * 10)
    print("How can we help you? ")
    print("1. Make a new account.")
    print("2. Log In")
    print("3. Exit")
    print("-" * 50)
    usr_inpt = int(input("Please enter your choice: "))
    print('\n')

    if usr_inpt == 1:
      print("=" * 10 + " NEW ACCOUNT APPLICATION PAGE " + "=" * 10)
      print("Preparing your application...")
      time.sleep(2)
      print("-" * 50)
      acc_cond = True
      credit_cond = True
      pwd_cond = True

      # Checking if account is in database (csv file)
      while acc_cond: # while acc_cond == True
        username = str(input("> Please enter a username: "))
        acc_cond = has_account(username) # acc_cond = F
        print("-" * 50)
        print("Checking username. Please wait a moment.")
        time.sleep(1)

        if acc_cond: # if acc_cond == True
          print("The username is already taken. Please select a different username.")
          print("-" * 50)
      
      print("Username is valid.")
      print("-" * 50)

      # Checking password condition
      while pwd_cond:
        pwd = str(input("> Please enter a password (length must be 4 - 6): "))
        print("-" * 50)
        print("Checking password validity...")

        time.sleep(2)

        if len(pwd) < 4:
          print("Your password is too short.")
          print("-" * 50)
        else:
          print("Password valid.")
          print("-" * 50)
          pwd_cond = False

      # Checking credit condition
      while credit_cond:
        credit = int(input("> Please enter an amount to be deposited (Minimum amount should be 500): "))
        print("-" * 50)
        print("Checking amount...")

        time.sleep(2)

        if credit >= 500:
          print("Transferring amount to bank account...")
          credit_cond = False
        else:
          print("The amount you entered is too low")
          print("-" * 50)

      print("Starting to register...")
      time.sleep(1)
      print("Registering your account into database...")

      register_account(username, pwd, credit)

      time.sleep(2)

      print("Register complete.")
      print("You can now log-in to our system.")
      print("-" * 50)
      print("\n")
    elif usr_inpt == 2:
      invalid = True
      print("=" * 10 + " LOGIN PAGE " + "=" * 10)

      while invalid:
        username = str(input("Enter your username: "))
        password = str(input("Enter your password: "))
        print("-" * 50)

        print("Checking username and password...")

        time.sleep(1)

        user_valid = check_is_user(username, password)

        if user_valid:
          invalid = False
          print("Logging in...")
          time.sleep(2)
          print("-" * 50)
          print("\n")
        else:
          print("Username or password might be wrong or not registered. Please check your username or password. If your account is not registered, please exit the program and re-run it.")
          print("-" * 50)
      
      user_info = pull_account(username)

      bank_user = Bank(user_info[0], user_info[1], int(user_info[2]))

      input_cond = True
      while input_cond:
        print("=" * 10 + " MAIN PAGE " + "=" * 10)
        print("Hello " + username + ". What can we do for you?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Get your current banking information")
        print("4. Change account password")
        print("5. Log Out")
        print("-" * 50)
        to_do = int(input("> Please enter your choice: "))
        print("\n")

        if to_do == 1:
          print("=" * 10 + " DEPOSIT " + "=" * 10)
          amt = int(input("> Please enter an amount to be deposited: "))
          print("-" * 50)
          print("Depositing amount...")
          time.sleep(1)
          start_credit = bank_user.credit
          curr_amt = bank_user.deposit(amt)
          print("Your starting amount was " + str(start_credit) + " has been added to " + str(curr_amt))
          print("-" * 50)
          print("\n")
        elif to_do == 2:
          print("=" * 10 + " WITHDRAWAL " + "=" * 10)
          amt = int(input("> Please enter an amount to be withdrawed: "))
          print("-" * 50)
          print("Withdrawing amount...")
          time.sleep(1)
          start_credit = bank_user.credit
          curr_amt = bank_user.withdraw(amt)
          print("Your starting amount was " + str(start_credit) + " has been decreased to " + str(curr_amt))
          print("-" * 50)
          print("\n")
        elif to_do == 3:
          info = bank_user.current_info()
          print("=" * 10 + " ACCOUNT INFORMATION " + "=" * 10)
          print("Fetching account information from database...")
          time.sleep(2)
          print("-" * 50)
          print("Username: " + info[0])
          print("Password: " + info[1])
          print("Credit: " + str(info[2]))
          print("-" * 50)
          print("\n")
        elif to_do == 4:
          print("=" * 10 + " CHANGE PASSWORD " + "=" * 10)
          print("Connecting to database...")
          time.sleep(2)
          print("-" * 50)
          pwd = str(input("Please enter your new password (length should be between 4 - 6 characters): "))
          print("-" * 50)
          new_pwd = bank_user.change_password(pwd)
          print("Changing password...")
          time.sleep(1)
          print("Your password has been changed to " + new_pwd)
          print("-" * 50)
          print("\n")
        elif to_do == 5:
          input_cond = False
          print("=" * 10 + " LOG OUT " + "=" * 10)
          print("Logging you out...")
          time.sleep(2)
          print("-" * 50)
          print("\n")
        else:
          print("=" * 10 + " ERROR NOTE " + "=" * 10)
          print("Please choose a valid number presented.")
          print("-" * 50)
          print("\n")
    elif usr_inpt == 3:
      usr_cond = False
      print("Thank you for using our application! Have a nice day!")
    else:
      print("=" * 10 + " ERROR NOTE " + "=" * 10)
      print("Please choose a valid number presented.")
      print("-" * 50)
      print("\n")
      
main()
