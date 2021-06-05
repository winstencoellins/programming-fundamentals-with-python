# Week 2 Programming Fundamentals Assignment
Catatan Week 2 terdapat pada file `Week2_Prog_Fund.pdf`.

# Control Flow
## Soal 1: FizzBuzz
Tuliskan sebuah function di Python yang mengiterasi sebuah integer dari 0 hingga n. Untuk bilangan kelipatan tiga, print / output "Fizz" sebagai ganti integer, dan untuk bilangan kelipatan lima, print / output "buzz". Untuk bilangan kelipatan tiga dan lima, print / output "fizzbuzz" ke console.

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/assgn_control_flow1.png)

Output:


![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/fizzbuzz_output.png)

## Soal 2: Mengkalikan tanpa Menggunakan Simbol *
Tuliskan function di Python yang mengkalikan dua nilai tanpa menggunakan simbol `*`. Gunakan tambah dan while loop untuk menulis function tersebut.

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/assgn_control_flow2.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/multiply_output.png)

# List
## Soal 1: Generate list of numbers
Tuliskan function di Python yang menghasilkan sebuah list yang dimulai dari `start` dan berhenti sebelum `end` dan mengalami kenaikan sebanyak `step`

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/assgn_list1.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/generate_list_output.png)

## Soal 2: Reverse the list
Tuliskan function di Python yang membalikkan nilai di dalam sebuah list

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/assgn_list2.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/reverse_list_output.png)

###### Note: Jika kamu terpikir untuk menggunakan `list.reverse()`, itu merupakan hal yang sangat bagus untukmu karena kamu bisa mengerti dokumentasi yang diberikan. Tetapi cobalah mengimplementasinya dengan menggunakan `while loop`.

# Loops
## Soal 1: Is number in list?
Tuliskan sebuah function di Python yang memeriksa apakah angka tersebut (`n`) berada di dalam sebuah list (`lst`).

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/loops_1.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/is_in_list.png)

## Soal 2: Intersection of lists
Tuliskan sebuah function di Python yang membandingkan 2 lists dan melihat apakah masing - masing mempunyai angka yang sama di dalam list tersebut. Contohnya, `[1, 2, 3]` dan `[2, 4, 6]` akan menghasilkan sebuah list baru `[2]` karena masing - masing list memiliki 1 angka yang sama yaitu 2. List bisa mengandung angka duplikat, tetapi tidak boleh memasukkan angka duplikat tersebut ke dalam list. Contohnya, `[2, 3, 2, 4]` dan `[2, 2, 4]` akan mengoutput `[2, 4]`.

#### Note: Disini kita akan mempelajari syntax `if else` baru yaitu `not in`. `Not in` berguna sebagai pembantu untuk memeriksa apakah nilai tersebut ada di dalam sebuah list. Cara penulisannya adalah `if [nilai] not in [list]`. Misalkan kita memiliki sebuah list `a = [1, 2, 3, 4]`. Kita ingin memeriksa apakah nilai 4 tersebut ada di dalam list. Kita bisa menuliskan kode ini sebagai berikut:

`if 4 not in a: print("False") else: print("True")` gunakan syntax yang baik dan benar ketika mencoba kode tersebut. Setelah mencoba kode tersebut dan mengerti bagaimana kode tersebut bekerja, implimentasikan kode ini untuk mempermudah pekerjaan kalian. (Good luck in exploring the code!)

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/loops_2.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/intersection.png)

###### Addition: Soal yang ini sengaja dibuat sedemikian sulit karena ini akan membantu mengasah kemampuan problem solving kalian ketika kalian terjun ke masyarakat. Skill untuk memahami dan mengerti segala sesuatu sendiri sangatlah dibutuhkan. Orang yang gagal untuk menguasai skill tersebut akan tertinggal sangat jauh di belakang (speaking from experience). Jika kalian berhasil menyelesaikan soal ini, bagus sekali. Jika kalian tidak berhasil menyelesaikan soal ini, kita akan membahasnya bersama.

## Soal 3: Output a Square
Tuliskan sebuah function di Python yang mengoutput sebuah persegi. Jika input `n` bernilai 1, maka "Not able / unable to form a square" akan di print ke console.

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/loops_3.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/square.png)

# List of List
## Soal 1: Output Matriks

Tuliskan sebuah function yang mengoutput list of list menjadi sebuah matriks

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/print_matrix.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/output_print_matrix.png)

## Soal 2: Penjumlahan Matriks

Tuliskan sebuah function yang mengoutput hasil jumlah kedua matriks

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/matrix_addition.png)

Output:

![alt text](https://github.com/winstencoellins/programming-fundamentals-with-python/blob/main/Week2/images/output_matrix_addition.png)
