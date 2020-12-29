import youtube_dl
import vlc

flag = 1

# ydl configs
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }]
}

# setting up the vlc player
Instance = vlc.Instance()
player = Instance.media_player_new()

# setting up youtube_dl
ydl = youtube_dl.YoutubeDL(ydl_opts)

def play_file(url):
    print("starting the player")
    media = Instance.media_new(url)
    media.get_mrl()
    player.set_media(media)
    player.play()

key = input("Enter the search key: ")

info = ydl.extract_info('ytsearch1:'+key, download=False,ie_key="YoutubeSearch")
url = info['entries'][0]['url']

while(flag == 1):
    play_file(url)
    flag = int(input("Press 0 to stop 1 to start again "))


