import webbrowser

class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False
    def open(self):
        webbrowser.open(self.link)
        self.seen = True

class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

def read_video():
    title = input("Enter title: ") + "\n"
    link = input("Enter link: ") + "\n"
    return Video(title, link)
def print_video(video):
    print("Video title:", video.title, end="")
    print("Video link:",video.link, end="")

def read_videos():
    videos = []
    total = int(input("\nEnter how many videos: "))
    print()
    for i in range(total):
        print("==> Enter video", i+1)
        videos.append(read_video())
    return videos
def print_videos(videos):
    print("\n============ Display videos ============")
    for i in range(len(videos)):
        print("===> Video "+str(i+1)+":")
        print_video(videos[i])

def write_video_to_txt(video, file):
    title = file.write(video.title)
    link = file.write(video.link)
def write_videos_to_txt(videos, file):
    file.write(str(len(videos)) + "\n")
    for i in range(len(videos)):
        write_video_to_txt(videos[i], file)

def read_video_from_txt(file):
    title = file.readline()
    link = file.readline()
    return Video(title, link)
def read_videos_from_txt(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        videos.append(read_video_from_txt(file))
    return videos

def read_playlist():
    name = input("\nEnter playlist name: ") + "\n"
    description = input("Enter description: ") + "\n"
    rating = input("Enter playlist rating (1-5): ") + "\n"
    videos = read_videos()
    return Playlist(name, description, rating, videos)

def write_playlist_to_txt(playlist):
    with open("data.txt","w") as file:
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(playlist.rating)
        write_videos_to_txt(playlist.videos, file)

def read_playlist_from_txt():
    with open("data.txt", "r") as file:
        name = file.readline()
        description = file.readline()
        rating = file.readline()
        videos = read_videos_from_txt(file)
    return Playlist(name, description, rating, videos)

def print_playlist(playlist):
    print("\n============ Display playlist ============")
    print("Playlist name:", playlist.name, end="")
    print("Playlist description:", playlist.description, end="")
    print("Playlist rating:", playlist.rating, end="")
    print_videos(playlist.videos)

def show_menu():
    print("\n=========== Menu ===========")    
    print("|  Option 1: Create playlist |")
    print("|  Option 2: Show playlist   |")
    print("|  Option 3: Play a video    |")
    print("|  Option 4: Add a video     |")
    print("|  Option 5: Update playlist |")
    print("|  Option 6: Remove a video  |")
    print("|  Option 7: Save and Exit   |")
    print("==============================") 

def select_digit_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice)<min or int(choice)>max:
        choice = input(prompt)
    return int(choice)

def play_video(playlist):
    print_videos(playlist.videos)
    total_videos = len(playlist.videos)
    choice = select_digit_in_range("Select a video (1,"+str(total_videos)+"): ", 1, total_videos)
    print("Open video:"+playlist.videos[choice-1].title+"- link: "+playlist.videos[choice-1].link)
    playlist.videos[choice-1].open()

def add_video(playlist):
    print("Enter new video information !!!")
    new_title = input("Enter new video title: ") + "\n"
    new_link = input("Enter new video link: ") + "\n"
    new_video = Video(new_title, new_link)
    return playlist.videos.append(Video(new_title,new_link))

def update_playlist(playlist):
    print("===> Update playlist information ?")
    print("1. name")
    print("2. Description")
    print("3. Rating")
    choice = select_digit_in_range("Enter what you wanna update(1-3): ",1,3)
    if choice == 1:
        new_name = input("Enter new name for playlist: ") +"\n"
        playlist.name = new_name
        print("Update successfully !!!")
        return playlist
    elif choice == 2:
        new_description = input("Enter new description for playlist: ") + "\n"
        playlist.description = new_description
        print("Updated successfully !!!")
        return playlist
    else:
        new_rating = input("Enter new rating for playlist: ") + "\n"
        playlist.rating = new_rating
        print("Updated successfully !!!")
        return playlist
    
def remove_video(playlist):
    print_videos(playlist.videos)
    choice = select_digit_in_range("Enter video you wanna delete (1,"+str(len(playlist.videos))+"): ", 1, len(playlist.videos))
    # del playlist.videos[choice-1]  #Way 1
    new_video_list = []          #Way 2
    for i in range(len(playlist.videos)):
        if i == choice-1:
            continue
        new_video_list.append(playlist.videos[i])
    playlist.videos = new_video_list
    print("===> Delete successfully !!!")
    return playlist


if __name__ == "__main__":
    try:
        playlist = read_playlist_from_txt()
        print("\n===>Loaded data successfully !!!")
    except:
        print("Welcome first user !!!")
    
    while True:
        show_menu()
        choice = select_digit_in_range("Select an option (1-7): ", 1, 7)
        if choice == 1:
            playlist = read_playlist()
            input("\n===> Press to continue !!!")
        elif choice == 2:
            print_playlist(playlist)
            input("\n===> Press to continue !!!")
        elif choice == 3:
            play_video(playlist)
            input("\n===> Press to continue !!!")
        elif choice == 4:
            playlist = add_video(playlist)
            input("\nPress enter to continue !!!")
        elif choice == 5:
            playlist = update_playlist(playlist)
            input("\n===> Press to continue !!!")
        elif choice == 6:
            playlist = remove_video(playlist)
            input("\n===> Press enter to continue !!!")
        elif choice == 7:
            write_playlist_to_txt(playlist)
            input("\n===> Press to continue !!!")
            break
