songs = []
#-------------GIAO DIEN CHINH---------------------
def show_menu():
    print("\n===== MENU QUẢN LÝ PLAYLIST =====")
    print("1. Thêm bài hát")
    print("2. Xóa bài hát")
    print("3. Hiển thị danh sách")
    print("0. Thoát")
    print("=================================")
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
add_song("Lạc Trôi", "Sơn Tùng MTP", 240)
add_song("Nắng Ấm Xa Dần", "Sơn Tùng MTP", 230)

print("\nDanh sách bài hát hiện có:")
print(songs)