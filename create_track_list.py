# Import the Tkinter module for GUI creation
import tkinter as tk
# Import function to retrieve a track from the track library
from track_library import get_item
# Import font configuration function
from font_manager import configure

playlist = []   # Global list to store the current playlist


# Function to open the "Create Playlist" window
def open_create_track_list():
    # Create a new popup window
    win = tk.Toplevel()
    win.resizable(False, False)  # Disable window resizing
    configure()  # Apply custom font settings
    win.geometry("680x360")  # Set window size
    win.title("Create Playlist")  # Set window title
    win.grid_columnconfigure(0, weight=1)  # Center-align the main column

    # Label to instruct the user to enter a track number
    label = tk.Label(win, text="Enter track number:")
    label.grid(row=0, column=0, columnspan=2, sticky="n", pady=5)

    # Entry widget for entering track number
    entry = tk.Entry(win)
    entry.grid(row=1, column=0, sticky="n", pady=5, padx=10)

    # Text widget to display the playlist
    display = tk.Text(win, width=60, height=10)
    display.grid(row=2, column=0, sticky="n", pady=5, padx=10)

    # Label to show status messages to the user
    message = tk.Label(win, text="")
    message.grid(row=3, column=0, sticky="n", pady=5, padx=10)

    # Frame to hold control buttons
    button_frame = tk.Frame(win)
    button_frame.grid(row=4, column=0, pady=(5, 10))

    # Function to add a track to the playlist
    def add_track():
        try:
            num = int(entry.get())  # Get track number from input
            item = get_item(num)  # Retrieve track from library
            if item:
                if item not in playlist:  # Avoid duplicates
                    playlist.append(item)  # Add to playlist
                    display.delete(1.0, tk.END)  # Clear current display
                    for t in playlist:
                        # Show each track in the playlist
                        display.insert(tk.END, f"{t.get_name()} - {t.get_artist()} "
                                               f"(Play Count: {t.get_play_count()})\n")
                    message.config(text=f"Added: {item.get_name()}")  # Show success message
                else:
                    message.config(text="Track is already in playlist.")  # Duplicate track warning
            else:
                message.config(text="Track does not exist")  # Invalid track number
        except ValueError:
            message.config(text="Please enter a valid number.")  # Input was not a number

    # Function to simulate playing the playlist
    def play_playlist():
        if not playlist:
            message.config(text="Playlist is empty.")  # Cannot play an empty playlist
            return

        display.delete(1.0, tk.END)  # Clear display
        for item in playlist:
            item.increment_play_count()  # Increase play count
            name = item.get_name()
            artist = item.get_artist()
            count = item.get_play_count()
            # Show track with updated play count
            display.insert(tk.END, f"{name} - {artist} (Play Count: {count})\n")
        message.config(text="Playlist played!")  # Success message

    # Function to reset playlist and play counts
    def reset_playlist():
        for item in playlist:
            item.reset_play_count()  # Reset play count to 0
        playlist.clear()  # Clear playlist
        display.delete(1.0, tk.END)  # Clear display
        message.config(text="Playlist reset.")  # Show reset message

    # Add control buttons for the user
    tk.Button(button_frame, text="Add Track", command=add_track).pack(side="left", padx=5)
    tk.Button(button_frame, text="Play Playlist", command=play_playlist).pack(side="left", padx=5)
    tk.Button(button_frame, text="Reset Playlist", command=reset_playlist).pack(side="left", padx=5)
