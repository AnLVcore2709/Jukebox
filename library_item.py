# Define the LibraryItem class, representing a track in the music library
class LibraryItem:
    def __init__(self, track_id, name, artist, rating):
        # Unique ID for the track
        self.track_id = track_id
        # Name of the track
        self.name = name
        # Artist of the track
        self.artist = artist
        # Rating of the track (1 to 5)
        self.rating = rating
        # Number of times the track has been played ;initialized to 0
        self.play_count = 0

    # Returns the name of the track
    def get_name(self):
        return self.name

    # Returns the artist's name
    def get_artist(self):
        return self.artist

    # Returns the current rating of the track
    def get_rating(self):
        return self.rating

    # Sets a new rating for the track
    def set_rating(self, rating):
        self.rating = rating

    # Returns the current play count of the track
    def get_play_count(self):
        return self.play_count

    # Increments the play count by 1
    def increment_play_count(self):
        self.play_count += 1

    # Resets the play count to 0
    def reset_play_count(self):
        self.play_count = 0
