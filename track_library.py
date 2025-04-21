# Import the LibraryItem class to represent individual music tracks
from library_item import LibraryItem

# Simple in-memory database of music tracks using a dictionary
# The keys are track numbers (integers), and the values are LibraryItem objects
library = {
    # Track 1: "Another Brick in the Wall" by Pink Floyd, rated 4 stars
    1: LibraryItem(1, "Another Brick in the Wall", "Pink Floyd", 4),
    # Track 2: "Stayin' Alive" by Bee Gees, rated 5 stars
    2: LibraryItem(2, "Stayin' Alive", "Bee Gees", 5),
    # Track 3: "Highway to Hell" by AC/DC, rated 2 stars
    3: LibraryItem(3, "Highway to Hell", "AC/DC", 2),
    # Track 4: "Shape of You" by Ed Sheeran, rated 1 stars
    4: LibraryItem(4, "Shape of You", "Ed Sheeran", 1),
    # Track 5: "Someone Like You" by Adele, rated 3 stars
    5: LibraryItem(5, "Someone Like You", "Adele", 3)
}


# Returns a list of all (track_number, LibraryItem) pairs in the library
# Used to view all available tracks with their details
def list_all():
    return list(library.items())


# Retrieves a LibraryItem by its track number, or returns None if the track does not exist
# Helps in accessing a specific track from the library
def get_item(track_number):
    return library.get(track_number, None)
