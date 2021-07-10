# Week4 Programming Assignment
## Object Oriented Programming (Constructor, toString, Attributes)

### Soal 1
Buatlah sebuah class bernama Student dan di dalam class tersebut terdapat attribute academic ability, physical ability, adaptability, social contribution, dan overall ability.
Setiap attribute akan mengembalikan (return) nilai dalam bentuk huruf (A, B, C, atau D). Nilai dibagi ke dalam kategori dengan ketentuan:
- A: 85 <=
- B: 70 <= nilai <= 84
- C: 45 <= nilai <= 69
- D: <= 44

Rumus untuk menghitung nilai overall: `(academic + physical + adapt + (social contribution * 0.5)) / 350 * 100` (rounded up)

Hint: untuk membulatkan nilai float ke bawah, gunakan `import math` di python lalu gunakan `math.ceil()`. Dokumentasi ini dapat membantu jika kalian tidak mengerti
cara untuk menggunakannya https://www.programiz.com/python-programming/modules/math

```python
class Student:
  # Constructor
  def __init__(self, class_name, name, academic, physical, adapt, social):
    pass
  
  # Attr
  def academic_ability(self):
    pass
    
  def physical_ability(self):
    pass
   
  def adaptability(self):
    pass
  
  def social_contribution(self):
    pass
    
  def overall_ability(self):
    pass
  
  # toString
  def __str__(self):
    pass
```

Output dari `__str__` method harus terlihat seperti ini:

```
[kelas] - [nama]
Academic Ability: [nilai huruf] ([nilai angka])
Physical Ability: [nilai huruf] ([nilai angka])
Adaptability: [nilai huruf] ([nilai angka])
Social Contribution: [nilai huruf] ([nilai angka])
Overall Ability: [nilai huruf] ([nilai angka])
```

Checking Work (copy and paste setelah selesai mengerjakan program diatas):
```python
student1 = Student("Class 1-B", "Ichinose Honami", 86, 54, 70, 96)
print(student1)
```

Expected Output:
```
Class 1-B - Ichinose Honami
Academic Ability: A (86)
Physical Ability: C (54)
Adaptability: B (70)
Social Contribution: A (96)
Overall Ability: B (74)
```

Note: `[]` di output bukan menandakan bahwa itu adalah list/array melainkan itu tergantung pada parameter yang diberikan kepada object.

### Soal 2

Game yang sedang booming sekarang yaitu Genshin Impact (Mihoyo), game dari China. Disini kita akan mengimplementasi OOP sederhana untuk game ini. Buatlah sebuah class
bernama GenshinChar yang memiliki attribute eat, walk, dan run.

```python
class GenshinChar:
  # Constructor
  def __init__(self, name, city, weapon, vision):
    pass
    
  # Attr
  def eat(self):
    pass
    
  def walk(self):
    pass
    
  def run(self):
    pass
    
  # toString
  def __str__(self):
    pass
```

Untuk attribute walk dan run, kita akan mengembalikan:
- `Running around [city] city...` untuk run attribute
- `Walking around [city] city...` untuk walk attribute

Untuk attribute eat, tergantung pada `city`:
- Jika karakter tersebut berasal dari Monstadt, maka akan mengembalikan (return) `Going to Good Hunter to eat...`
- Jika karakter tersebut berasal dari Liyue, maka akan mengembalikan (return) `Going to Wanmin Restaurant to eat...`

Output dari `__str__` harus terlihat seperti ini:

```
[name] - [vision]
City: [city]
Weapon Type: [weapon]
```

Checking Output (copy and paste kode ini setelah menyelesaikan program di atas):
```python
character1 = GenshinChar("Amber", "Monstadt", "Bow", "Pyro")
print(character1)
print(character1.walk())
print(character1.run())
print(character1.eat() + "\n")

character2 = GenshinChar("Zhongli", "Liyue", "Polearm", "Geo")
print(character2)
print(character2.walk())
print(character2.run())
print(character2.eat())
```

Expected Output:
```
Amber - Pyro
City: Monstadt
Weapon Type: Bow
Walking around Monstadt city
Running around Monstadt city
Going to Good Hunter to eat

Zhongli - Geo
City: Liyue
Weapon Type: Polearm
Walking around Liyue city
Running around Liyue city
Going to Wanmin Restaurant to eat
```
