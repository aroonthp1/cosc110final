import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CleanlinessRaterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cleanliness Rater")
        
        self.ratings = []

        # Create a ttk style for the buttons
        self.button_style = ttk.Style()
        self.button_style.configure(
            "Rounded.TButton",  # Style name
            padding=2,          # Padding within the button
            borderwidth=10,      # Border width
            relief="groove",    # Border style (rounded edges)
            background="white",
            foreground="black"
        )

        # Create an outer frame with padding
        outer_frame = ttk.Frame(root, padding=5)
        outer_frame.grid(row=0, column=0)
        
        # Centered label for rating prompt
        self.label = ttk.Label(outer_frame, text="Rate the cleanliness of this bus:", justify="center", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, columnspan=5, pady=3)
        
        # Buttons for ratings 1 to 5, displayed on the same line
        for rating in range(1, 6):
            rating_button = ttk.Button(outer_frame, text=str(rating), command=lambda r=rating: self.submit_rating(r), style="Rounded.TButton")
            rating_button.grid(row=1, column=rating-1, padx=0)
        
        # Centered label for displaying the average rating on the next line
        self.average_label = ttk.Label(outer_frame, text="", justify="center", font=("Helvetica", 12))
        self.average_label.grid(row=2, column=0, columnspan=5, pady=2)
        
    def submit_rating(self, rating):
        self.ratings.append(rating)
        self.update_average()
        
    def update_average(self):
        if self.ratings:
            average = sum(self.ratings) / len(self.ratings)
            self.average_label.config(text=f"This bus has an average cleanliness rating of {average:.2f}")
        else:
            self.average_label.config(text="This bus has an average cleanliness rating of N/A")

if __name__ == "__main__":
    root = tk.Tk()
    app = CleanlinessRaterApp(root)
    root.mainloop()
