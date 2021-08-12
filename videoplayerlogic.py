import VideoplayerUi
import vlc
import pafy

class VideoPlayerLogic:
    def __init__(self):
        
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        url = "https://www.youtube.com/watch?v=G0OqIkgZqlA"                                                                                         
        video = pafy.new(url)                                                                                                                       
        best = video.getbestvideo()                                                                                                                 
        playurl = best.url                                                                                                                          
        player = vlc.MediaPlayer(playurl)  
        player.video_set_scale(0.6)                                                                                                      
        player.play()
        while True:
            pass
        

        
  