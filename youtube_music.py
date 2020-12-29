# importing module 
import youtube_dl 
import vlc

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


def play_file(url):
	media = Instance.media_new(url)
	media.get_mrl()
	player.set_media(media)
	player.play()

def dwl_vid(): 
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    # extarcting informations 
		meta_data = ydl.extract_info(zxt,download=False)
		# print(meta_data['url'])	
		play_file(meta_data['url'])

		
		
#play the wav file just downloaded
# def play_musix():
    


channel = 1
while (channel == int(1)): 
	link_of_the_video = input("Get me the source ") 
	zxt = link_of_the_video.strip() 

	dwl_vid() 
	channel = int(input("press 0 to stop"))
	# channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done ")) 

