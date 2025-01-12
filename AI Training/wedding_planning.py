class WeddingPlanner:
    def __init__(self):
        """Membina struktur data untuk menyimpan tetamu dan acara."""
        self.guests = {}  # dictionary yang menyimpan tetamu sebagai kunci (nama) dan nilai (seat number)
        self.schedule = []  # senarai acara dengan struct(time, event)

    def add_guest(self, name, seat_number):
        """Menambah tetamu ke senarai."""
        if name in self.guests:
            print(f"Tetamu '{name}' telah ada dalam senarai. Adakah anda mahu mengemaskini nombor tempat duduk?")
            choice = input("Ya/Tidak: ").strip().lower()
            if choice == 'ya':
                self.guests[name] = seat_number
                print(f"Nombor tempat duduk untuk '{name}' telah dikemaskini kepada {seat_number}.")
            else:
                print(f"Tiada perubahan dibuat untuk '{name}'.")
        else:
            self.guests[name] = seat_number
            print(f"Tetamu '{name}' telah ditambahkan dengan nombor tempat duduk {seat_number}.")

    def remove_guest(self, name):
        """Membuang tetamu dari senarai."""
        if name in self.guests:
            del self.guests[name]
            print(f"Tetamu '{name}' telah dibuang dari senarai.")
        else:
            print(f"Tetamu '{name}' tidak ditemui dalam senarai.")

    def view_guests(self):
        """Melihat senarai tetamu."""
        if not self.guests:
            print("Tiada tetamu dalam senarai.")
        else:
            print("Senarai tetamu:")
            for name, seat_number in self.guests.items():
                print(f"{name}: Nombor tempat duduk {seat_number}")

    def schedule_event(self, time, event):
        """Menjadualkan acara baru."""
        self.schedule.append({"time": time, "event": event})
        print(f"Acara '{event}' telah dijadualkan pada waktu {time}.")

    def view_schedule(self):
        """Melihat jadual acara."""
        if not self.schedule:
            print("Tiada acara dalam jadual.")
        else:
            print("Jadual Acara:")
            for index, item in enumerate(self.schedule, 1):
                print(f"{index}. Waktu: {item['time']}, Acara: {item['event']}")


def main():
    """Menjalankan fungsi pengendali utama program."""
    planner = WeddingPlanner()
    while True:
        print("\nPilihan Perancangan Majlis Perkahwinan:")
        print("1. Menambah Tetamu")
        print("2. Membuang Tetamu")
        print("3. Melihat Senarai Tetamu")
        print("4. Menjadualkan Acara")
        print("5. Melihat Jadual Acara")
        print("6. Keluar")

        choice = input("Pilih pilihan: ").strip()

        if choice == '1':
            name = input("Masukkan nama tetamu: ").strip()
            try:
                seat_number = int(input("Masukkan nombor tempat duduk: ").strip())
                planner.add_guest(name, seat_number)
            except ValueError:
                print("Nombor tempat duduk mesti nombor bulat.")
        elif choice == '2':
            name = input("Masukkan nama tetamu untuk dibuang: ").strip()
            planner.remove_guest(name)
        elif choice == '3':
            planner.view_guests()
        elif choice == '4':
            time = input("Masukkan waktu acara: ").strip()
            event = input("Masukkan nama acara: ").strip()
            planner.schedule_event(time, event)
        elif choice == '5':
            planner.view_schedule()
        elif choice == '6':
            print("Terima kasih menggunakan sistem perancangan majlis perkahwinan. Selamat tinggal!")
            break
        else:
            print("Pilihan tidak sah. Sila cuba lagi.")


if __name__ == "__main__":
    main()
