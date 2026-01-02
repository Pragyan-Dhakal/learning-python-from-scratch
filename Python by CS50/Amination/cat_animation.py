import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Create the main window
root = tk.Tk()
root.title("Cat Animation")

# Load the GIF using PIL
gif_path = "cat.gif"  # Replace this with the path to the cat GIF you want to use
img = Image.open(gif_path)

# Create a label to display the animation
lbl = tk.Label(root)
lbl.pack()

# Function to update the frame of the GIF
def update_frame(ind):
    frame = ImageTk.PhotoImage(img.copy().seek(ind))
    lbl.config(image=frame)
    lbl.image = frame
    root.after(100, update_frame, (ind + 1) % img.n_frames)

# Start the animation
root.after(0, update_frame, 0)

# Start the Tkinter event loop
root.mainloop()
