class Music:
    firmware_version = 0.0

    def __init__(self):
        self.__tracks = ["Spirit in the sky", "Starman", "Escape"]
        self.current_track = None

    def play(self):
        self.current_track = self.__tracks[0]
    
    def list_tracks(self):
        return self.__tracks
    
    @classmethod
    def update_firmware(cls, new_version):
        if new_version > cls.firmware_version:
            cls.firmware_version = new_version

player = Music()
print("Tracks currently on device:", player.list_tracks())
Music.update_firmware(2.0)
print("Updated player firmware version to", player.firmware_version)
player.play()
print("currently playing", player.current_track)
        
