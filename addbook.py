import customtkinter
from tkinter import filedialog
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class CreateNewWorkApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Create/Add New Bork")
        self.geometry("1200x800")  # Full window size
        self.minsize(800, 600)  # Minimum window size

        # Create a frame for the content
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

        # Configuring layout for the frame
        self.grid_rowconfigure(0, weight=1)  # Allow resizing of content area
        self.grid_columnconfigure(0, weight=1)

        # Title for the form
        self.form_title_label = customtkinter.CTkLabel(self.main_frame, text="Create/Add New Book", font=("Arial", 24, "bold"))
        self.form_title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

        # Title field
        self.title_field_label = customtkinter.CTkLabel(self.main_frame, text="Title", font=("Arial", 14))
        self.title_field_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")

        self.title_textbox = customtkinter.CTkTextbox(self.main_frame, height=30, width=400)
        self.title_textbox.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="ew")

        # Description field
        self.description_label = customtkinter.CTkLabel(self.main_frame, text="Description", font=("Arial", 14))
        self.description_label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")

        self.description_textbox = customtkinter.CTkTextbox(self.main_frame, height=100, width=400)
        self.description_textbox.grid(row=2, column=1, padx=(5, 10), pady=5, sticky="ew")

        # Genre field (Checkboxes displayed horizontally)
        self.genre_label = customtkinter.CTkLabel(self.main_frame, text="Genre", font=("Arial", 14))
        self.genre_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")

        # Genres list
        self.genres = ["Mystery", "Thriller", "Horror", "Sci-Fi", "Fantasy", "Romance", "Adventure", "Historical", "Drama"]
        self.genre_checkboxes = {}
        self.genre_frame = customtkinter.CTkFrame(self.main_frame)
        self.genre_frame.grid(row=3, column=1, padx=(5, 10), pady=5, sticky="ew")

        # Add checkboxes for each genre in a horizontal layout
        for idx, genre in enumerate(self.genres):
            self.genre_checkboxes[genre] = customtkinter.StringVar(value="0")
            checkbox = customtkinter.CTkCheckBox(self.genre_frame, text=genre, variable=self.genre_checkboxes[genre], onvalue="1", offvalue="0")
            checkbox.grid(row=0, column=idx, padx=5, pady=5, sticky="w")

        # Cover Image Display (resize box to a book cover size)
        self.cover_image_label = customtkinter.CTkLabel(self.main_frame, text="No image selected", width=150, height=250, fg_color="gray")
        self.cover_image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Bind the label click to the upload_image function
        self.cover_image_label.bind("<Button-1>", self.upload_image)

        # Action Buttons (Save and Cancel) - Move buttons to the right
        self.action_buttons_frame = customtkinter.CTkFrame(self.main_frame)
        self.action_buttons_frame.grid(row=5, column=1, padx=10, pady=10, sticky="e")  # Align to the right

        self.save_button = customtkinter.CTkButton(self.action_buttons_frame, text="Save", command=self.save_work)
        self.save_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.cancel_button = customtkinter.CTkButton(self.action_buttons_frame, text="Cancel", command=self.cancel_creation)
        self.cancel_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Adjusting layout to fill the window
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(5, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=3)

    def upload_image(self, event=None):
        """Open file dialog to upload an image for the cover."""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path).resize((150, 250))  # Resize image to book cover size
            self.cover_image = ImageTk.PhotoImage(image)
            self.cover_image_label.configure(image=self.cover_image, text="")  # Show selected image

    def save_work(self):
        """Handle the save action for the new work."""
        title = self.title_textbox.get("1.0", "end").strip()
        description = self.description_textbox.get("1.0", "end").strip()

        # Collect selected genres
        selected_genres = [genre for genre, var in self.genre_checkboxes.items() if var.get() == "1"]

        # Validation check for empty fields
        if not title or not description or not selected_genres:
            customtkinter.CTkMessagebox(title="Error", message="Please fill in all fields and upload a cover image.")
            return

        # Simulating save action (this could be saving to a database or file)
        print(f"Saving New Work: Title: {title}, Description: {description}, Genres: {', '.join(selected_genres)}")

        # Success message
        customtkinter.CTkMessagebox(title="Success", message="Your work has been saved successfully!")
        self.clear_form()

    def cancel_creation(self):
        """Cancel the creation process and clear form."""
        self.clear_form()

    def clear_form(self):
        """Clear all fields in the form."""
        self.title_textbox.delete("1.0", "end")
        self.description_textbox.delete("1.0", "end")
        for genre_var in self.genre_checkboxes.values():
            genre_var.set("0")
        self.cover_image_label.configure(image=None, text="No cover selected")

if __name__ == "__main__":
    app = CreateNewWorkApp()
    app.mainloop()
