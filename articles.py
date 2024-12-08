import tkinter
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class WattpadApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Easy-Library")
        self.geometry("1200x700")

        # Top frame for search bar, profile icon, menu, and buttons
        self.top_frame = customtkinter.CTkFrame(self, height=50)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.top_frame.grid_columnconfigure(0, weight=1)  # Menu column, smaller space
        self.top_frame.grid_columnconfigure(1, weight=3)  # Search bar takes more space
        self.top_frame.grid_columnconfigure(2, weight=1)  # Profile icon column
        self.top_frame.grid_columnconfigure(3, weight=5)  # ComboBox section takes most space
        self.top_frame.grid_rowconfigure(0, weight=1)

        # ComboBox menu
        self.menu_combobox = customtkinter.CTkComboBox(
            self.top_frame,
            values=["Home", "Popular Articles", "New Releases", "Genres", "Settings"],
            command=self.menu_option_selected,
        )
        self.menu_combobox.set("Menu")  # Set default value
        self.menu_combobox.grid(row=0, column=0, padx=10, pady=(10, 0))

        # Middle section: search bar and button
        self.search_entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="Search articles...")
        self.search_entry.grid(row=0, column=1, padx=10, pady=1, ipadx=200, ipady=3)

        # Adjusted search button width
        self.search_button = customtkinter.CTkButton(self.top_frame, text="Search", command=self.search_articles)
        self.search_button.grid(row=0, column=2, padx=10, pady=1, ipadx=2, ipady=2)  # Increased ipadx for wider button

        # ComboBox section (Browse, Articles, Write)
        self.combo_box_frame = customtkinter.CTkFrame(self.top_frame, fg_color="transparent")
        self.combo_box_frame.grid(row=0, column=3, sticky="e", padx=10, pady=(10, 0))

        # Browse ComboBox
        self.browse_combobox = customtkinter.CTkComboBox(
            self.combo_box_frame,
            values=["Browse Genres"],
            command=self.browse_option_selected,
        )

        # Genres list (to be revealed when Browse option is selected)
        self.genres = [
            "Mystery", "Thriller", "Horror", "Sci-Fi", "Fantasy", "Romance", "Adventure", "Historical", "Drama"
        ]

        self.browse_combobox.set("Browse")
        self.browse_combobox.grid(row=0, column=0, padx=5)

        # Articles ComboBox
        self.articles_combobox = customtkinter.CTkComboBox(
            self.combo_box_frame,
            values=["Book Section"],
            command=self.articles_option_selected,
        )
        self.articles_combobox.set("Books")
        self.articles_combobox.grid(row=0, column=1, padx=5)

        # Write ComboBox
        self.write_combobox = customtkinter.CTkComboBox(
            self.combo_box_frame,
            values=["Write/Add Article"],
            command=self.write_option_selected,
        )
        self.write_combobox.set("Write")
        self.write_combobox.grid(row=0, column=2, padx=5)

        # Profile icon
        self.profile_image = Image.open(r"D:\CustomTkinter-master\examples\test_images\home_dark.png").resize((40, 40))
        self.profile_image = ImageTk.PhotoImage(self.profile_image)
        self.profile_button = customtkinter.CTkButton(
            self.top_frame, text="", image=self.profile_image, width=40, height=40, fg_color="transparent",
            command=self.open_profile
        )
        self.profile_button.grid(row=0, column=4, padx=10, pady=10)

        # Main content area
        self.main_frame = customtkinter.CTkScrollableFrame(self, label_text="Articles")
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self.grid_columnconfigure(0, weight=1)  # Allow resizing
        self.grid_rowconfigure(1, weight=1)  # Allow resizing

        # Example article data with view and favorite counts, and author names
        self.all_articles = [
            {"title": "The Hidden Truth", "view_count": 1500, "favorite_count": 500, "author": "Alice Green", "image": None, "genre": "Mystery"},
            {"title": "The Last Secret", "view_count": 1200, "favorite_count": 800, "author": "Bob White", "image": None, "genre": "Thriller"},
            {"title": "Dark Shadows", "view_count": 900, "favorite_count": 600, "author": "Charlie Brown", "image": None, "genre": "Horror"},
            {"title": "Whispers in the Night", "view_count": 2100, "favorite_count": 1500, "author": "David Gray", "image": None, "genre": "Thriller"},
            {"title": "The Invisible Enemy", "view_count": 2500, "favorite_count": 1800, "author": "Eva Black", "image": None, "genre": "Sci-Fi"},
        ]

        # Initially show all articles
        self.populate_cards(self.all_articles)

    def populate_cards(self, articles):
        # Clear previous cards
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        row = 0
        col = 0
        for article in articles:
            card = customtkinter.CTkFrame(self.main_frame, corner_radius=15, height=150, width=380)  # Adjust width for 3 in a row
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            card.grid_columnconfigure(1, weight=1)

            # Add image placeholder
            image_label = customtkinter.CTkLabel(card, text="Image", width=100, height=100, fg_color="gray")
            image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

            # Add title
            title_label = customtkinter.CTkLabel(card, text=article["title"], font=("Arial", 18, "bold"))
            title_label.grid(row=0, column=1, sticky="w", padx=10)

            # Add author name
            author_label = customtkinter.CTkLabel(card, text=f"By {article['author']}", font=("Arial", 10, "italic"))
            author_label.grid(row=1, column=1, sticky="w", padx=10)

            # Add view and favorite counts (horizontal layout)
            counts_frame = customtkinter.CTkFrame(card, fg_color="transparent")
            counts_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")

            # View count label
            view_count_label = customtkinter.CTkLabel(counts_frame, text=f"Views: {article['view_count']}", font=("Arial", 10))
            view_count_label.grid(row=0, column=0, padx=10)

            # Favorite count label
            favorite_count_label = customtkinter.CTkLabel(counts_frame, text=f"Favorites: {article['favorite_count']}", font=("Arial", 10))
            favorite_count_label.grid(row=0, column=1, padx=10)

            # Arrange 3 cards per row
            col += 1
            if col >= 3:  # Reset column to 0 after 3 cards
                col = 0
                row += 1

    def menu_option_selected(self, choice):
        print(f"Menu option selected: {choice}")
        # Implement logic for menu options
        if choice == "Home":
            self.populate_cards(self.all_articles)  # Example action for Home

    def browse_option_selected(self, option):
        if option == "Browse Genres":
            # Set the browse ComboBox to genres
            self.browse_combobox.configure(values=self.genres)  # Now showing genre options
            self.browse_combobox.set("Select Genre")  # Reset the ComboBox to show "Select Genre"

        elif option == "Browse All Articles":
            self.populate_cards(self.all_articles)

    def articles_option_selected(self, option):
        if option == "View Articles":
            print("View Articles selected")
        elif option == "Popular Articles":
            print("Popular Articles selected")

    def write_option_selected(self, option):
        if option == "Write New Article":
            print("Write New Article selected")
        elif option == "Drafts":
            print("Drafts selected")

    def search_articles(self):
        # Get search term
        search_term = self.search_entry.get().strip().lower()
        filtered_articles = [
            article for article in self.all_articles if search_term in article["title"].lower()
        ]

        if filtered_articles:
            self.populate_cards(filtered_articles)
        else:
            # Clear main frame and show no results message
            for widget in self.main_frame.winfo_children():
                widget.destroy()
            empty_message = customtkinter.CTkLabel(self.main_frame, text="No articles found.", font=("Arial", 18, "italic"))
            empty_message.pack(padx=20, pady=20)

    def open_profile(self):
        print("Profile icon clicked")

if __name__ == "__main__":
    app = WattpadApp()
    app.mainloop()
