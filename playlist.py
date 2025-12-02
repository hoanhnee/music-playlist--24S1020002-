songs = []
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
#-----------Xoa bai hat --------------
def remove_song():
    if not songs:
        print("❌ Playlist trống!")
        return

    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song}")

    try:
        index = int(input("Nhập số thứ tự bài hát muốn xóa: "))
        index -= 1  # vì danh sách bắt đầu từ 0

        if 0 <= index < len(songs):
            removed = songs.pop(index)
            print(f"✔ Đã xóa bài hát: {removed}")
        else:
            print("❌ Số thứ tự không hợp lệ!")

    except ValueError:
        print("❌ Vui lòng nhập số!")

def search_by_artist():
    """Hàm tìm kiếm bài hát theo tên ca sĩ"""
    artist_name = input("\nNhập tên ca sĩ muốn tìm: ").lower()
    
    # Lọc danh sách bài hát, tìm kiếm không phân biệt chữ hoa/thường
    found_songs = [s for s in songs if artist_name in s['artist'].lower()]
    
    if found_songs:
        print(f"\nTìm thấy {len(found_songs)} bài hát của nghệ sĩ '{artist_name}':")
        for s in found_songs:
            # Dùng định dạng tương tự view_playlist
            print(f"- {s['title']} ({s['duration']}s)")
    else:
        print(f"❌ Không tìm thấy bài hát nào của ca sĩ '{artist_name}'.")