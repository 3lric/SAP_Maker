import tkinter.font as tkFont
import tkinter as tk
from tkinter import filedialog, messagebox, Menu
from tkinter import ttk
import os
from PIL import Image, ImageTk
import webbrowser
from sap_headers import get_sap_headers  # Import headers
from sap_files import get_sap_files      # Import files


class SAPConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SAP Maker v0.2b")
        self.root.geometry("408x358")
        self.root.resizable(False, False)

        # Update icon
        self.root.iconbitmap('SM_Icon.ico')

        # Path to background image
        bg_image_path = "logo.png"  # Ensure this path is correct
        self.set_background(bg_image_path)

        # SAP headers
        self.sap_headers = get_sap_headers()  # Fetch headers from external module

        # Dropdown menus
        self.game_dropdown = tk.StringVar(value="Select Game")
        self.category_dropdown = tk.StringVar(value="Select SAP Category")
        self.file_dropdown = tk.StringVar(value="Select SAP File")

        # Create dropdowns with ttk.Combobox
        self.create_dropdown_menus()

        # Buttons
        self.extract_button = tk.Button(
            root, text="Extract WAV from SAP", command=self.extract_wav, bg="#333", fg="#ff8080", font=("Helvetica", 10, "bold")
        )
        self.extract_button.place(x=125, y=40)  # Move to top center

        self.create_button = tk.Button(
            root, text="Create SAP from WAV", command=self.create_sap, bg="#333", fg="#ff8080", font=("Helvetica", 10, "bold"), state="disabled"
        )
        self.create_button.place(x=125, y=203)  # Bottom center, disabled initially

        # Bind event to check if button should be enabled
        self.game_dropdown.trace("w", self.update_ui)
        self.category_dropdown.trace("w", self.update_ui)
        self.file_dropdown.trace("w", self.update_file_selection)

        # Menu
        menubar = Menu(root)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Instructions", command=self.show_instructions)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        root.config(menu=menubar)

    def set_background(self, image_path):
        image = Image.open(image_path)
        image = image.resize((408, 358))
        image = image.convert("RGBA")
        transparency = 0.7
        alpha = image.split()[3]
        alpha = alpha.point(lambda p: p * transparency)
        image.putalpha(alpha)
        self.background_image = ImageTk.PhotoImage(image)

        self.bg_label = tk.Label(self.root, image=self.background_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_dropdown_menus(self):
        # Create dropdowns with ttk.Combobox
        self.game_menu = ttk.Combobox(self.root, textvariable=self.game_dropdown, state="readonly")
        self.game_menu['values'] = ["Resident Evil 2"]
        self.game_menu.place(x=130, y=235)  # Positioned in the center

        self.category_menu = ttk.Combobox(self.root, textvariable=self.category_dropdown, state="readonly")
        self.category_menu['values'] = ["Core", "Door", "Enemy", "Room", "Weapon", "Voice/Music", "Footstep", "Custom"]
        self.category_menu.place(x=130, y=260)

        self.file_menu = ttk.Combobox(self.root, textvariable=self.file_dropdown, state="readonly")
        self.file_menu.place(x=130, y=285)

        # Initially hide category and file dropdowns
        self.category_menu.place_forget()
        self.file_menu.place_forget()

    def update_ui(self, *args):
        game_selected = self.game_dropdown.get() != "Select Game"
        category_selected = self.category_dropdown.get() != "Select SAP Category"
        file_selected = self.file_dropdown.get() != "Select SAP File"

        # Reset file dropdown and disable create button when category changes
        if category_selected:
            self.file_dropdown.set("Select SAP File")
            self.create_button.config(state="disabled")

        if game_selected:
            self.category_menu.place(x=130, y=260)
        else:
            self.category_menu.place_forget()

        if category_selected and self.category_dropdown.get() not in ["Voice/Music", "Footstep", "Custom"]:
            self.file_menu.place(x=130, y=285)
            self.populate_file_menu()
        else:
            self.file_menu.place_forget()

        if self.category_dropdown.get() == "Custom":
            self.show_custom_warning()

    def populate_file_menu(self):
        category = self.category_dropdown.get()
        sap_files = get_sap_files(category)

        # Populate the file_menu dropdown without resetting the previous state
        self.file_menu['values'] = sap_files

    def update_file_selection(self, *args):
        selected_file = self.file_dropdown.get()
        if selected_file and selected_file != "Select SAP File":
            self.create_button.config(state="normal")
        else:
            self.create_button.config(state="disabled")

    def extract_wav(self):
        sap_file_path = filedialog.askopenfilename(title="Select SAP file", filetypes=[("SAP files", "*.sap")])
        if not sap_file_path:
            return

        output_dir = filedialog.askdirectory(title="Select output folder for WAV files")
        if not output_dir:
            return

        with open(sap_file_path, 'rb') as sap_file:
            data = sap_file.read()
            riff_chunks = data.split(b'RIFF')[1:]
            for i, chunk in enumerate(riff_chunks):
                wav_data = b'RIFF' + chunk
                output_path = os.path.join(output_dir, f"extracted_{i+1}.wav")
                with open(output_path, 'wb') as wav_file:
                    wav_file.write(wav_data)
        print(f"Extracted {len(riff_chunks)} WAV files to {output_dir}")
        messagebox.showinfo("Success", "WAV files successfully extracted!", icon='info')

    def create_sap(self):
        wav_files = filedialog.askopenfilenames(title="Select WAV files", filetypes=[("WAV files", "*.wav")])
        if not wav_files:
            return

        sap_file_path = filedialog.asksaveasfilename(defaultextension=".sap", title="Save SAP file as", filetypes=[("SAP files", "*.sap")])
        if not sap_file_path:
            return

        header = self.get_sap_header(self.category_dropdown.get())

        with open(sap_file_path, 'wb') as sap_file:
            sap_file.write(header)
            for wav_file in wav_files:
                with open(wav_file, 'rb') as wf:
                    sap_file.write(wf.read())
        print(f"Created new SAP file at {sap_file_path}")
        messagebox.showinfo("Success", "SAP file successfully created!", icon='info')

    def get_sap_header(self, category):
        if category == "Voice/Music":
            return b'\x01\x00\x00\x00\x00\x00\x00\x00'
        elif category == "Footstep":
            return b'\x07\x00\x00\x00\x00\x00\x00\x00'
        elif category == "Custom":
            return b'\x01\x00\x00\x00\x00\x00\x00\x00'
        else:
            return self.sap_headers.get(self.file_dropdown.get(), b'\x00\x00\x00\x00\x00\x00\x00\x00')

    def show_instructions(self):
        messagebox.showinfo("Instructions", "This is a SAP converter tool for extracting and creating SAP files.\n\n"
                                            "Steps:\n"
                                            "1. Select a game.\n"
                                            "2. Choose the appropriate SAP category.\n"
                                            "3. For most categories, select a specific SAP file.\n"
                                            "4. Use 'Extract WAV from SAP' to extract audio files or 'Create SAP from WAV' to create new SAP files.\n\n"
                                            "Categories like 'Voice/Music', 'Footstep', and 'Custom' automatically generate the SAP header.")

    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About SAP Maker")
        about_window.geometry("350x250")
        about_window.iconbitmap('SM_Icon.ico')

        about_text = tk.Label(about_window, text="SAP Maker v0.2b\nCreated by 3lric", font=("Helvetica", 10, "bold"))
        about_text.pack(pady=10)

        # Hyperlink labels
        github_label = tk.Label(about_window, text="GitHub: 3lric", fg="blue", cursor="hand2", font=("Helvetica", 9, "underline"))
        github_label.pack(pady=5)
        github_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/3lric"))

        crem_wiki_label = tk.Label(about_window, text="CREM Wiki", fg="blue", cursor="hand2", font=("Helvetica", 9, "underline"))
        crem_wiki_label.pack(pady=5)
        crem_wiki_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://classicremodification.com"))

        crem_discord_label = tk.Label(about_window, text="CREM Discord", fg="blue", cursor="hand2", font=("Helvetica", 9, "underline"))
        crem_discord_label.pack(pady=5)
        crem_discord_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://discord.gg/tR29MU5aCS"))

    def show_custom_warning(self):
        warning_window = tk.Toplevel(self.root)
        warning_window.title("Custom SAP Warning")
        warning_window.geometry("300x200")

        # Set custom icon and background
        warning_window.iconbitmap('SM_Icon.ico')
        image = Image.open("warning.png")
        image = image.resize((300, 200))
        self.warning_bg = ImageTk.PhotoImage(image)
        warning_label = tk.Label(warning_window, image=self.warning_bg)
        warning_label.place(x=0, y=0, relwidth=1, relheight=1)

        warning_text = tk.Label(warning_window, text="This option should only be used if you know what you are doing.\n\n"
                                                     "You need to edit the EXE/SLUS or EDT/EDH file accordingly for "
                                                     "it to work properly with more or less sounds or in a different "
                                                     "order than originally intended.\n\n"
                                                     "Custom SAPs will be output with a generic 8-byte header that will "
                                                     "also need to be edited accordingly.", fg="red", bg="black",
                                wraplength=280, font=("Helvetica", 9, "bold"))
        warning_text.place(x=10, y=20)

        close_button = tk.Button(warning_window, text="I Understand", command=warning_window.destroy)
        close_button.place(x=120, y=160)


if __name__ == "__main__":
    root = tk.Tk()
    app = SAPConverterApp(root)
    root.mainloop()
