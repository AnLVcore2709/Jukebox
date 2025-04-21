# Import the Tkinter module for GUI creation
import tkinter as tk
# Import custom font configuration function
from font_manager import configure
# Function to open the "Create Track List" window
from create_track_list import open_create_track_list
# Function to open the "Update Tracks" window
from update_tracks import open_update_tracks
# Function to open the "View Tracks" window
from view_tracks import open_view_tracks


# Main function that sets up the main JukeBox window
def main():
    # Create the main application window
    win = tk.Tk()
    # Disable resizing to maintain consistent layout
    win.resizable(False, False)
    configure()  # Apply custom font settings from the font_manager
    win.geometry("680x250")  # Set the size of the main window
    win.title("JukeBox")  # Set the window title
    win.configure(bg="gray")  # Set background color for the window

    # Add an instructional label at the top of the window
    tk.Label(
        win,
        text="Select an option by clicking one of the buttons below",  # Instruction text
        bg="white",  # Background color of the label
        fg="black",  # Text color
        font=("Helvetica", 20)  # Font style and size
    ).pack(pady=15, padx=20)  # Add spacing around the label

    # Create a horizontal frame to hold the option buttons
    frame = tk.Frame(win, bg="gray")
    frame.pack(padx=20, pady=50)

    # Button to open the "View Tracks" window
    tk.Button(
        frame,
        text="View Tracks",
        width=15,
        command=open_view_tracks  # Calls function when clicked
    ).pack(side=tk.LEFT, padx=15)

    # Button to open the "Create Track List" window
    tk.Button(
        frame,
        text="Create Track List",
        width=15,
        command=open_create_track_list
    ).pack(side=tk.LEFT, padx=15)

    # Button to open the "Update Tracks" window
    tk.Button(
        frame,
        text="Update Tracks",
        width=15,
        command=open_update_tracks
    ).pack(side=tk.LEFT, padx=15)

    # Start the Tkinter event loop to keep the window open and responsive
    win.mainloop()


# Entry point of the program
if __name__ == "__main__":
    main()
