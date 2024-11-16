import random
import time

def main():
    print("Selamat datang di permainan Teka-Teki Matematika!")
    player_name = input("Masukkan nama Anda: ")
    print(f"Halo, {player_name}!")

    # Memilih level kesulitan
    print("\nPilih level kesulitan:")
    print("1. Mudah (angka 1-10, penjumlahan dan pengurangan)")
    print("2. Menengah (angka 1-50, tambah operasi perkalian)")
    print("3. Sulit (angka 1-100, termasuk pembagian)")
    level = input("Masukkan nomor level (1/2/3): ")

    # Menentukan batas angka dan jenis operasi berdasarkan level
    if level == '1':
        max_number = 10
        operators = ['+', '-']
    elif level == '2':
        max_number = 50
        operators = ['+', '-', '*']
    elif level == '3':
        max_number = 100
        operators = ['+', '-', '*', '/']
    else:
        print("Level tidak valid. Mulai dari level Mudah.")
        max_number = 10
        operators = ['+', '-']

    score = 0
    questions = 5  # Jumlah soal

    for i in range(questions):
        num1 = random.randint(1, max_number)
        num2 = random.randint(1, max_number)
        operator = random.choice(operators)

        # Menghitung jawaban yang benar
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2
        else:  # Pembagian
            # Membulatkan pembagian ke bilangan bulat
            num1 = num1 * num2  # Pastikan num1 bisa dibagi dengan num2 tanpa desimal
            correct_answer = num1 // num2

        # Menampilkan soal kepada pemain
        print(f"\nSoal {i+1}: Berapa hasil dari {num1} {operator} {num2}?")
        
        # Menghitung waktu mulai untuk batas waktu 5 detik
        start_time = time.time()
        try:
            answer = int(input("Jawaban Anda: "))
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Memeriksa batas waktu dan jawaban
            if elapsed_time > 5:
                print("Terlambat! Anda kehabisan waktu.")
            elif answer == correct_answer:
                print("Benar!")
                score += 10
            else:
                print(f"Salah! Jawaban yang benar adalah {correct_answer}.")
        except ValueError:
            print("Harap masukkan angka yang valid.")

    print(f"\nSkor Akhir Anda: {score}")
    print("Terima kasih telah bermain!")

if __name__ == "_main_":
    main() 