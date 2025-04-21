import tkinter as tk    # Import the Tkinter module for GUI creation
from font_manager import configure  # Custom function to configure fonts
from track_library import get_item  # Function to retrieve track info by ID


def open_update_tracks():
    # Create a new top-level window (separate from the main window)
    win = tk.Toplevel()
    win.resizable(False, False)  # Disable resizing
    configure()  # Apply custom font settings
    win.geometry("540x250")  # Set window size
    win.title("Update Track Rating")  # Set window title

    # Label and Entry for track number input
    tk.Label(win, text="Track Number", pady=5).pack()
    num_entry = tk.Entry(win)
    num_entry.pack(pady=10)

    # Label and Entry for new rating input
    tk.Label(win, text="New Rating (1-5)", pady=5).pack()
    rating_entry = tk.Entry(win)
    rating_entry.pack(pady=5)

    # Label to display result messages (success or error)
    result = tk.Label(win, text="", fg="blue", font=("Helvetica", 12))
    result.pack(pady=5)

    # Function to update the rating of a track
    def update_rating():
        try:
            # Convert user input to integers
            num = int(num_entry.get())
            new_rating = int(rating_entry.get())

            # Validate that the rating is within 1 to 5
            if new_rating < 1 or new_rating > 5:
                result.config(text=" Rating must be between 1 and 5.", fg="red")
                return

            # Get the track item by number
            item = get_item(num)
            if item:
                # Update rating if track exists
                item.set_rating(new_rating)
                # Show success message
                result.config(
                    text=f"{item.get_name()} updated: "
                         f"Rating = {'*' * item.get_rating()}, "
                         f"Played {item.get_play_count()} times.",
                    fg="green"
                )
            else:
                # Show error if track number is invalid
                result.config(text=" Invalid track number.", fg="red")
        except ValueError:
            # Show error if user input is not valid integers
            result.config(text=" Please enter valid numbers for both fields.", fg="red")

    # Button to trigger rating update
    tk.Button(win, text="Update Rating", command=update_rating).pack(pady=5)
