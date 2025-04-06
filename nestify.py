import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def fade_in(widget, alpha=0.0):
    """Fade-in animation for the window."""
    alpha += 0.05
    if alpha <= 0.9:
        widget.attributes("-alpha", alpha)
        widget.after(50, fade_in, widget, alpha)

def set_path():
    """Open a file dialog to choose a folder path."""
    folder_path = filedialog.askdirectory(title="Select Folder Path")
    if folder_path:
        messagebox.showinfo("Path Selected", f"Selected path: {folder_path}")
    return folder_path

def get_user_input(prompt):
    """Get input from user via a dialog."""
    return simpledialog.askstring("Input", prompt)

def create_folders():
    """Create folders based on user input."""
    try:
        folder_path = set_path() or get_user_input("Enter folder path:")
        if not folder_path:
            return
        
        folder_name = get_user_input("Enter folder name:")
        if not folder_name or folder_name.upper() == "Q":
            return
        
        folder_quantity = simpledialog.askinteger("Input", "Enter quantity:")
        if folder_quantity is None:
            return

        for x in range(1, folder_quantity + 1):
            os.makedirs(os.path.join(folder_path, f"{folder_name}{x}"), exist_ok=True)
        messagebox.showinfo("Success", f"Created {folder_quantity} folders successfully!")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for quantity.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The specified path does not exist.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied to create folders.")
    except OSError as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def create_files():
    """Create files based on user input with optional file type."""
    try:
        folder_path = set_path() or get_user_input("Enter folder path:")
        if not folder_path:
            return
        
        file_name = get_user_input("Enter file name:")  # Fixed: Removed incorrect MainFrame reference
        if not file_name or file_name.upper() == "Q":
            return
        
        file_quantity = simpledialog.askinteger("Input", "Enter quantity:")
        if file_quantity is None:
            return
        
        file_type = get_user_input("Enter file type (e.g., .txt, .doc) or leave blank for .txt:")
        if not file_type:
            file_type = ".txt"
        elif not file_type.startswith("."):
            file_type = f".{file_type}"

        os.makedirs(folder_path, exist_ok=True)
        for x in range(1, file_quantity + 1):
            full_path = os.path.join(folder_path, f"{file_name}{x}{file_type}")
            with open(full_path, 'w') as file:
                file.write(f"This is file number {x}")
        messagebox.showinfo("Success", f"Created {file_quantity} files with type {file_type} successfully!")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for quantity.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The specified path does not exist.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied to create files.")
    except OSError as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def create_both():
    """Create folders and files inside them with optional file type."""
    try:
        folder_path = set_path() or get_user_input("Enter folder path:")
        if not folder_path:
            return
        
        folder_name = get_user_input("Enter folder name:")
        if not folder_name or folder_name.upper() == "Q":
            return
        
        folder_quantity = simpledialog.askinteger("Input", "Enter folder quantity:")
        if folder_quantity is None:
            return
        
        file_name = get_user_input("Enter file name:")
        if not file_name or file_name.upper() == "Q":
            return
        
        file_quantity = simpledialog.askinteger("Input", "Enter file quantity per folder:")
        if file_quantity is None:
            return
        
        file_type = get_user_input("Enter file type (e.g., .txt, .doc) or leave blank for .txt:")
        if not file_type:
            file_type = ".txt"
        elif not file_type.startswith("."):
            file_type = f".{file_type}"

        for x in range(1, folder_quantity + 1):
            folder_full_path = os.path.join(folder_path, f"{folder_name}{x}")
            os.makedirs(folder_full_path, exist_ok=True)
            for y in range(1, file_quantity + 1):
                file_full_path = os.path.join(folder_full_path, f"{file_name}{y}{file_type}")
                with open(file_full_path, 'w') as file:
                    file.write(f"This is file number {y} in folder {folder_name}{x}")
        messagebox.showinfo("Success", f"Created {folder_quantity} folders, each with {file_quantity} {file_type} files!")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for quantities.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The specified path does not exist.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied.")
    except OSError as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def show_help():
    """Display help information."""
    help_text = (
        "Nestify by Naeem Mahmud\n\n"
        "This tool helps you create folders and files easily:\n"
        "- Browse Path: Select a directory to work in.\n"
        "- Create Folders: Make multiple folders with a custom name and quantity.\n"
        "- Create Files: Generate files with a custom name, quantity, and file type.\n"
        "- Create Both: Create folders and populate them with files.\n\n"
    )
    messagebox.showinfo("Help", help_text)

def on_enter(e):
    """Hover effect: Change button color on mouse enter."""
    e.widget['background'] = '#4a6fa5'

def on_leave(e):
    """Hover effect: Revert button color on mouse leave."""
    e.widget['background'] = '#2a4066'

# Set up the GUI
root = tk.Tk()
root.title("Nestify")
root.geometry("600x300")  # Default window size
root.configure(bg="#1a2a44")  # Space-like dark blue
root.attributes("-alpha", 0.0)  # Start fully transparent for fade-in

# Fade-in animation
fade_in(root)

# Main frame to hold all elements
main_frame = tk.Frame(root, bg="#1a2a44")
main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Label
title_label = tk.Label(main_frame, text="Nestify", bg="#1a2a44", fg="white", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=10)

# Define button style for uniformity
button_font = ("Arial", 10)
button_width = 12
button_height = 2
button_padx = 10
button_pady = 5

# Buttons with rounded borders, uniform size, and space theme
browse_btn = tk.Button(main_frame, text="just for show",  bg="#2a4066", fg="white", 
                      activebackground="#4a6fa5", relief="flat", borderwidth=0, 
                      font=button_font, width=button_width, height=button_height, padx=button_padx, pady=button_pady)
browse_btn.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
browse_btn.bind("<Enter>", on_enter)
browse_btn.bind("<Leave>", on_leave)
browse_btn.configure(highlightthickness=10, highlightbackground="#2a4066")

folder_btn = tk.Button(main_frame, text="Create Folders", command=create_folders, bg="#2a4066", fg="white", 
                      activebackground="#4a6fa5", relief="flat", borderwidth=0, 
                      font=button_font, width=button_width, height=button_height, padx=button_padx, pady=button_pady)
folder_btn.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
folder_btn.bind("<Enter>", on_enter)
folder_btn.bind("<Leave>", on_leave)
folder_btn.configure(highlightthickness=10, highlightbackground="#2a4066")

file_btn = tk.Button(main_frame, text="Create Files", command=create_files, bg="#2a4066", fg="white", 
                    activebackground="#4a6fa5", relief="flat", borderwidth=0, 
                    font=button_font, width=button_width, height=button_height, padx=button_padx, pady=button_pady)
file_btn.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
file_btn.bind("<Enter>", on_enter)
file_btn.bind("<Leave>", on_leave)
file_btn.configure(highlightthickness=10, highlightbackground="#2a4066")

both_btn = tk.Button(main_frame, text="Create Both", command=create_both, bg="#2a4066", fg="white", 
                    activebackground="#4a6fa5", relief="flat", borderwidth=0, 
                    font=button_font, width=button_width, height=button_height, padx=button_padx, pady=button_pady)
both_btn.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
both_btn.bind("<Enter>", on_enter)
both_btn.bind("<Leave>", on_leave)
both_btn.configure(highlightthickness=10, highlightbackground="#2a4066")

# Help button
help_btn = tk.Button(main_frame, text="Help", command=show_help, bg="#2a4066", fg="white", 
                    activebackground="#4a6fa5", relief="flat", borderwidth=0, 
                    font=button_font, width=button_width, height=button_height, padx=button_padx, pady=button_pady)
help_btn.grid(row=2, column=1, columnspan=2, pady=10, sticky="nsew")
help_btn.bind("<Enter>", on_enter)
help_btn.bind("<Leave>", on_leave)
help_btn.configure(highlightthickness=10, highlightbackground="#2a4066")

# Configure grid weights to make the layout responsive
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1, uniform="btn")
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)

# Run the GUI
if __name__ == "__main__":
    root.mainloop()