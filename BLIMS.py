import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Main Menu")
        master.geometry("400x300") # Set a default size for the main window

        self.label = tk.Label(master, text="Welcome to the Main Menu!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button1 = tk.Button(master, text="Quality Analysis", command=self.open_subwindow1, width=20, height=2)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(master, text="Open Subwindow 2", command=self.open_subwindow2, width=20, height=2)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(master, text="Open Subwindow 3", command=self.open_subwindow3, width=20, height=2)
        self.button3.pack(pady=10)

    def open_subwindow1(self):
        self.master.withdraw()  # Hide the main window
        subwindow = tk.Toplevel(self.master)
        Subwindow1(subwindow, self.master)

    def open_subwindow2(self):
        self.master.withdraw()  # Hide the main window
        subwindow = tk.Toplevel(self.master)
        Subwindow2(subwindow, self.master)

    def open_subwindow3(self):
        self.master.withdraw()  # Hide the main window
        subwindow = tk.Toplevel(self.master)
        Subwindow3(subwindow, self.master)

class Subwindow1:
    def __init__(self, master, main_window_root):
        self.master = master
        self.main_window_root = main_window_root # Reference to the main window's root
        master.title("Quality Analysis")
        master.geometry("800x200")

        self.label = tk.Label(master, text="Quality Analysis", font=("Arial", 14))
        self.label.pack(pady=20)
        # --- Batch Number Field for Subwindow1 ---
        self.batch_label = tk.Label(master, text="Batch Number:", font=("Arial", 12))
        self.batch_label.pack(pady=5)

        self.batch_entry = tk.Entry(master, width=30)
        self.batch_entry.pack(pady=5)
        # --- End Batch Number Field ---

        self.back_button = tk.Button(master, text="Back to Main Menu", command=self.go_back, width=15, height=1)
        self.back_button.pack(pady=20)

        # Handle window close button (X) directly to go back
        self.master.protocol("WM_DELETE_WINDOW", self.go_back)

    def go_back(self):
        self.master.destroy()  # Close the current subwindow
        self.main_window_root.deiconify() # Show the main window again

class Subwindow2:
    def __init__(self, master, main_window_root):
        self.master = master
        self.main_window_root = main_window_root
        master.title("Subwindow 2")
        master.geometry("300x200")

        self.label = tk.Label(master, text="This is Subwindow 2", font=("Arial", 14))
        self.label.pack(pady=20)

        self.back_button = tk.Button(master, text="Back to Main Menu", command=self.go_back, width=15, height=1)
        self.back_button.pack(pady=20)

        self.master.protocol("WM_DELETE_WINDOW", self.go_back)

    def go_back(self):
        self.master.destroy()
        self.main_window_root.deiconify()

class Subwindow3:
    def __init__(self, master, main_window_root):
        self.master = master
        self.main_window_root = main_window_root
        master.title("Subwindow 3")
        master.geometry("300x200")

        self.label = tk.Label(master, text="This is Subwindow 3", font=("Arial", 14))
        self.label.pack(pady=20)

        self.back_button = tk.Button(master, text="Back to Main Menu", command=self.go_back, width=15, height=1)
        self.back_button.pack(pady=20)

        self.master.protocol("WM_DELETE_WINDOW", self.go_back)

    def go_back(self):
        self.master.destroy()
        self.main_window_root.deiconify()

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()