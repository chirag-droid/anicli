video_player = "mpv"
mirror = "https://gogoanime.pe"

class Anime:
    def __init__(self, title, id) -> None:
        self.title = title
        self.id = id
    
    def __str__(self) -> str:
        return f"{self.title}"
