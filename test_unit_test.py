import unittest
from library_item import LibraryItem
import view_tracks
from unittest.mock import MagicMock, patch
import tkinter as tk
from track_library import list_all, get_item


# ===== Test for LibraryItem =====
class TestLibraryItem(unittest.TestCase):
    def test_track_creation(self):
        track = LibraryItem(1, "Song A", "Artist X", 4)
        self.assertEqual(track.track_id, 1)
        self.assertEqual(track.get_name(), "Song A")
        self.assertEqual(track.get_artist(), "Artist X")
        self.assertEqual(track.get_rating(), 4)
        self.assertEqual(track.get_play_count(), 0)

    def test_increment_play_count(self):
        track = LibraryItem(2, "Song B", "Artist Y", 5)
        track.increment_play_count()
        track.increment_play_count()
        self.assertEqual(track.get_play_count(), 2)

    def test_reset_play_count(self):
        track = LibraryItem(3, "Song C", "Artist Z", 3)
        track.increment_play_count()
        track.increment_play_count()
        track.reset_play_count()
        self.assertEqual(track.get_play_count(), 0)

    def test_set_rating(self):
        track = LibraryItem(4, "Song D", "Artist W", 2)
        track.set_rating(5)
        self.assertEqual(track.get_rating(), 5)

