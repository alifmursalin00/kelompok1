import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.score = {'1': 0, '2': 0, '3': 0}  # Skor berdasarkan level

    def update_score(self, level, score):
        self.score[level] = max(self.score[level], score)  # Memperbarui skor untuk level tertentu

class MathGame:
    def __init__(self):
        self.players = {}  # Dictionary untuk menyimpan objek pemain
        self.current_player = None
        self.questions = 5
        self.max_number = 10
        self.operators = ['+', '-']

    def create_player(self, player_name):
        if player_name in self.players:
            print(f"Pemain {player_name} sudah ada.")
        else:
            self.players[player_name] = Player(player_name)  # Membuat objek Player baru
            print(f"Pemain {player_name} berhasil ditambahkan.")

    def read_players(self):
        if self.players:
            print("\nDaftar Pemain:")
            for player in self.players.values():
                print(f"- {player.name}")
        else:
            print("Belum ada pemain yang terdaftar.")

    def update_player(self, player_name, new_name):
        if player_name in self.players:
            self.players[new_name] = self.players.pop(player_name)  # Ubah nama pemain
            self.players[new_name].name = new_name
            print(f"Nama pemain {player_name} berhasil diubah menjadi {new_name}.")
        else:
            print(f"Pemain {player_name} tidak ditemukan.")

    def delete_player(self, player_name):
        if player_name in self.players:
            del self.players[player_name]
            print(f"Pemain {player_name} berhasil dihapus.")
        else:
            print(f"Pemain {player_name} tidak ditemukan.")

    def display_top_scores(self):
        if self.players:
            print("\nTop Skor Berdasarkan Level:")
            for level in ['1', '2', '3']:
                print(f"\nLevel {level}:")
                sorted_players = sorted(
                    self.players.items(),
                    key=lambda x: x[1].score[level],
                    reverse=True
                )
                for rank, (player, data) in enumerate(sorted_players, start=1):
                    print(f"{rank}. {data.name}: {data.score[level]} poin")
        else:
            print("Belum ada pemain dengan skor.")

    def set_level(self, level):
        if level == '1':
            self.max_number = 10
            self.operators = ['+', '-']
        elif level == '2':
            self.max_number = 50
            self.operators = ['+', '-', '*']
        elif level == '3':
            self.max_number = 100
            self.operators = ['+', '-', '*', '/']
        else:
            print("Level tidak valid. Mulai dari level Mudah.")
            self.max_number = 10
            self.operators = ['+', '-']

        if self.current_player:
            self.players[self.current_player].score.setdefault(level, 0)  # Inisialisasi skor level jika belum ada

    def generate_question(self):
        num1 = random.randint(1, self.max_number)
        num2 = random.randint(1, self.max_number)
        operator = random.choice(self.operators)

        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2
        else:  # Pembagian
            num1 = num1 * num2  # Pastikan num1 bisa dibagi dengan num2 tanpa desimal
            correct_answer = num1 // num2

        return num1, operator, num2, correct_answer

    def play(self):
        # Reset skor untuk level yang dipilih setiap kali permainan dimulai
        self.score = 0
        
        for i in range(self.questions):
            num1, operator, num2, correct_answer = self.generate_question()

            print(f"\nSoal {i+1}: Berapa hasil dari {num1} {operator} {num2}?")

            start_time = time.time()
            try:
                answer = int(input("Jawaban Anda: "))
                end_time = time.time()
                elapsed_time = end_time - start_time

                if elapsed_time > 15:
                    print("Terlambat! Anda kehabisan waktu.")
                elif answer == correct_answer:
                    print("Benar!")
                    self.score += 10
                else:
                    print(f"Salah! Jawaban yang benar adalah {correct_answer}.")
            except ValueError:
                print("Harap masukkan angka yang valid.")

        # Skor yang dicapai di level ini
        print(f"\nSkor Akhir Anda untuk Level {self.current_level}: {self.score}")

        # Update skor hanya untuk level yang dimainkan
        self.players[self.current_player].update_score(self.current_level, self.score)
        print("Terima kasih telah bermain!")

def main():
    game = MathGame()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Pemain")
        print("2. Lihat Pemain")
        print("3. Ubah Nama Pemain")
        print("4. Hapus Pemain")
        print("5. Main Game")
        print("6. Top Skor")
        print("7. Keluar")

        choice = input("Pilih menu (1-7): ")

        if choice == '1':
            player_name = input("Masukkan nama pemain baru: ")
            game.create_player(player_name)
        elif choice == '2':
            game.read_players()
        elif choice == '3':
            player_name = input("Masukkan nama pemain yang ingin diubah: ")
            new_name = input("Masukkan nama baru: ")
            game.update_player(player_name, new_name)
        elif choice == '4':
            player_name = input("Masukkan nama pemain yang ingin dihapus: ")
            game.delete_player(player_name)
        elif choice == '5':
            player_name = input("Masukkan nama pemain: ")
            if player_name in game.players:
                game.current_player = player_name
                print("\nPilih level kesulitan:")
                print("1. Mudah (angka 1-10, penjumlahan dan pengurangan)")
                print("2. Menengah (angka 1-50, tambah operasi perkalian)")
                print("3. Sulit (angka 1-100, termasuk pembagian)")
                level = input("Masukkan nomor level (1/2/3): ")
                game.set_level(level)
                game.current_level = level  # Menyimpan level yang dipilih
                game.play()
            else:
                print(f"Pemain {player_name} tidak ditemukan.")
        elif choice == '6':
            game.display_top_scores()
        elif choice == '7':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
