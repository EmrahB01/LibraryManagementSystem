class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")  
        self.file.seek(0)  

    def __del__(self):
        self.file.close()  

    def add_book(self):  # Library sınıfının bir metodu olarak tanımlanmalı
        # Kullanıcıdan kitap bilgilerini alıyoruz
        book_title = input("Kitap başlığını girin: ")
        book_author = input("Kitap yazarını girin: ")
        release_year = input("İlk yayınlanma yılını girin: ")
        num_pages = input("Sayfa sayısını girin: ")

        # Kitap bilgilerini bir satır halinde birleştiriyoruz
        book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"

        # Bilgileri dosyaya ekliyoruz
        self.file.write(book_info)
        print("Kitap başarıyla eklendi.")

    def list_books(self):
        self.file.seek(0)  # Dosyanın başına dön
        books = self.file.read().splitlines()  # Satırları oku ve liste haline getir
        if not books:
            print("Kütüphane boş.")
            return

        print("Kütüphanedeki Kitaplar:")
        for book in books:
            title, author, *_ = book.split(",")  # Kitap bilgilerini virgüllere göre ayır
            print(f"Başlık: {title}, Yazar: {author}")
    def remove_book(self):
        title_to_remove = input("Silmek istediğiniz kitabın başlığını girin: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("Kütüphane boş.")
            return

        # Kaldırılacak kitabın indexini bul
        index_to_remove = None
        for i, book in enumerate(books):
            if title_to_remove in book:
                index_to_remove = i
                break

        if index_to_remove is None:
            print("Kitap bulunamadı.")
            return
        # Kitabı kaldır
        del books[index_to_remove]

        self.file.seek(0)
        self.file.truncate()

        #Güncel listeyi books.txt dosyasına yaz
        for book in books:
            self.file.write(book + '\n')

        print("Kitap başarıyla silindi.")

    def show_menu(self):
        while True:
            print("\n***Menü***")
            print("--------------------")
            print("1. Kitapları Listele")
            print("2. Kitap Ekle")
            print("3. Kitap Kaldır")
            print("4. Çıkış (q ya basın)")

            secim = input("Lütfen bir seçenek girin: ")

            if secim == "1":
                self.list_books()
            elif secim == "2":
                self.add_book()
            elif secim == "3":
                self.remove_book()
                pass
            elif secim.lower() == "q":
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçenek! Lütfen tekrar deneyin.")

lib = Library()  # Library sınıfından bir nesne oluşturuyoruz
lib.show_menu()  # Menüyü göstermek için bu nesne üzerinden show_menu metodunu çağırın
