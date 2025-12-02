songs = []
#-------------GIAO DIEN CHINH---------------------
def main():
    while True: 
        print("\n--- MUSIC PLAYLIST MANAGER ---") 
        print("1. Thêm bài hát") 
        print("2. Xem danh sách phát") 
        print("3. Tìm bài hát theo ca sĩ") 
        print("4. Thoát") 
         
        choice = input("Chọn chức năng: ") 
         
        if choice == '1': 
            add_song() 
        elif choice == '2': 
            view_playlist() 
        elif choice == '3': 
            search_by_artist() 
        elif choice == '4': 
            print("Kết thúc chương trình.") 
            break 
        else: 
            print("Lựa chọn không hợp lệ.")
#---------------THEM BAI HAT----------------------
def add_song(title, artist, duration):
    """
    Hàm thêm bài hát vào danh sách songs.
    title: tên bài hát (string)
    artist: tên ca sĩ (string)
    duration: thời lượng (giây) - int
    """
    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }

    songs.append(song)
    print("✔ Đã thêm bài hát thành công!")
    print(song)


# ========================
# Ví dụ chạy thử hàm
# ========================
add_song("Lạc Trôi", "Sơn Tùng MTP", 240)
add_song("Nắng Ấm Xa Dần", "Sơn Tùng MTP", 230)

print("\nDanh sách bài hát hiện có:")

print(songs)
