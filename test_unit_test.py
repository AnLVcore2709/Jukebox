import unittest
from library_item import LibraryItem


# ===== Test for LibraryItem =====
class TestLibraryItem(unittest.TestCase):
    def test_track(self):
        track = LibraryItem(3, "Highway to Hell", "AC/DC", 2)
        self.assertEqual(track.track_id, 3)
        self.assertEqual(track.get_name(), "Highway to Hell")
        self.assertEqual(track.get_artist(), "AC/DC")
        self.assertEqual(track.get_rating(), 2)
        self.assertEqual(track.get_play_count(), 0)

    def test_increment_play_count(self):
        track = LibraryItem(2, "Stayin' Alive", "Bee Gees", 5)
        track.increment_play_count()
        track.increment_play_count()
        self.assertEqual(track.get_play_count(), 2)

    def test_reset_play_count(self):
        track = LibraryItem(2, "Stayin' Alive", "Bee Gees", 5)
        track.increment_play_count()
        track.increment_play_count()
        track.reset_play_count()
        self.assertEqual(track.get_play_count(), 0)

    def test_set_rating(self):
        track = LibraryItem(4, "Shape of You", "Ed Sheeran", 1)
        track.set_rating(5)
        self.assertEqual(track.get_rating(), 5)
