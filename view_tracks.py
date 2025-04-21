# Import the Tkinter module for GUI creation
import tkinter as tk
# Import helper functions from the music library module
from track_library import list_all, get_item


# Function to open the "View Tracks" GUI window
def open_view_tracks():
    # Create a new top-level window separate from the main window
    win = tk.Toplevel()
    win.resizable(False, False)  # Disable window resizing
    win.title("View Tracks")  # Set the window title

    # Label prompting the user to enter a track number
    tk.Label(win, text="Enter Track Number").grid(row=0, column=1)
    # Entry widget where user inputs the track number
    entry = tk.Entry(win, width=5)
    entry.grid(row=0, column=2)

    # Text widget to display all tracks from the library
    listbox = tk.Text(win, width=45, height=10)
    listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Text widget to display detailed information of a specific track
    detail = tk.Text(win, width=25, height=10)
    detail.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

    # Label to show status messages to users
    status = tk.Label(win, text="", anchor="w")
    status.grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=20)

    # Function to list all tracks in the listbox area
    def list_tracks():
        listbox.delete(1.0, tk.END)  # Clear previous content
        for track_id, item in list_all():  # Loop through all tracks
            stars = '*' * item.get_rating()  # Convert rating to star format
            # Format the line: ID, name, artist, rating stars
            line = f"{track_id:02d} {item.get_name()} - {item.get_artist()} {stars}\n"
            listbox.insert(tk.END, line)  # Insert into listbox
        status.config(text="List Tracks button was clicked!")  # Update status message

    # Function to display details of a specific track based on the entered number
    def view_track():
        try:
            num = int(entry.get())  # Try converting input to an integer
            item = get_item(num)  # Retrieve track data from the library
            if item:
                detail.delete(1.0, tk.END)  # Clear previous details
                # Insert track name, artist, rating, and play count
                detail.insert(tk.END, f"{item.get_name()}\n{item.get_artist()}\n")
                detail.insert(tk.END, f"rating: {'*' * item.get_rating()}\n"
                                      f"plays: {item.get_play_count()}")
                status.config(text="View Track button was clicked!")  # Update status
            else:
                detail.delete(1.0, tk.END)
                detail.insert(tk.END, "Track number does not exist.")  # Handle invalid track
                status.config(text="View Track button was clicked!")
        except ValueError:
            detail.delete(1.0, tk.END)
            detail.insert(tk.END, "Please enter a valid number.")  # Handle non-integer input
            status.config(text="View Track button was clicked!")

    # Button to trigger listing all tracks
    tk.Button(win, text="List All Tracks", command=list_tracks).grid(row=0, column=0)

    # Button to trigger viewing a specific track by number
    tk.Button(win, text="View Track", command=view_track).grid(row=0, column=3)
