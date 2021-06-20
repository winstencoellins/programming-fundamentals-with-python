import csv

class Bank:
  def __init__(self, name, password, credit):
    self.name = name
    self.password = password
    self.credit = credit

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
    lst = []
    self.credit -= amount

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

  def change_password(self, pwd):
    lst = []

    with open("user_data.csv") as csv_file:
      r = csv.DictReader(csv_file)

      for row in r:
        if self.name == row["username"]:
          row["password"] = pwd
        lst.append(row)

    with open("user_data.csv", "w") as csv_file:
      fieldnames = ['username', 'password', 'credit']
      w = csv.DictWriter(csv_file, fieldnames)

      w.writeheader()
      
      for i in lst:
        w.writerow(i)
      
      return pwd

  def current_info(self):
    lst = [self.name, self.password, self.credit]

    return lst