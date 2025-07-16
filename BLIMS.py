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
        self.main_window_root = main_window_root
        master.title("Quality Analysis")
        master.geometry("500x500")

        self.label = tk.Label(master, text="Quality Analysis", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)

        # --- Batch Number Field ---
        batch_frame = tk.Frame(master)
        batch_frame.pack(pady=10, fill='x', padx=50)

        self.batch_label = tk.Label(batch_frame, text="Batch Number:", font=("Arial", 12))
        self.batch_label.pack(side='left', padx=(0, 10))

        self.batch_entry = tk.Entry(batch_frame, width=30)
        self.batch_entry.pack(side='right', expand=True, fill='x')
        # --- End Batch Number Field ---

        # --- Analysis Dropdown List ---
        analysis_frame = tk.Frame(master)
        analysis_frame.pack(pady=10, fill='x', padx=50)

        self.analysis_label = tk.Label(analysis_frame, text="Analysis Type:", font=("Arial", 12))
        self.analysis_label.pack(side='left', padx=(0, 10))

        self.analysis_options = ["Volume", "Mass", "Temperature", "Density", "Purity"]
        self.selected_analysis = tk.StringVar(master)
        self.selected_analysis.set(self.analysis_options[0])

        self.analysis_dropdown = tk.OptionMenu(analysis_frame, self.selected_analysis, *self.analysis_options)
        self.analysis_dropdown.pack(side='right', expand=True, fill='x')
        self.analysis_dropdown.config(width=25)
        # --- End Analysis Dropdown List ---

        # --- Measurement Field (New) ---
        measurement_frame = tk.Frame(master)
        measurement_frame.pack(pady=10, fill='x', padx=50)

        self.measurement_label = tk.Label(measurement_frame, text="Measurement:", font=("Arial", 12))
        self.measurement_label.pack(side='left', padx=(0, 10))

        self.measurement_entry = tk.Entry(measurement_frame, width=30)
        self.measurement_entry.pack(side='right', expand=True, fill='x')
        # --- End Measurement Field ---

        # --- Buttons ---
        button_frame = tk.Frame(master)
        button_frame.pack(side='bottom', pady=20, fill='x', padx=20)

        self.import_button = tk.Button(button_frame, text="Import Measurement", command=self.import_measurement, width=20, height=2, font=("Arial", 10, "bold"))
        self.import_button.pack(side='left', padx=10, expand=True)

        self.back_button = tk.Button(button_frame, text="Back to Main Menu", command=self.go_back, width=20, height=2, font=("Arial", 10))
        self.back_button.pack(side='right', padx=10, expand=True)
        # --- End Buttons ---

        self.master.protocol("WM_DELETE_WINDOW", self.go_back)

    def go_back(self):
        self.master.destroy()
        self.main_window_root.deiconify()
    def import_measurement(self):
        # Fill the Measurement field with '10'
        self.measurement_entry.delete(0, tk.END)  # Clear any existing text
        self.measurement_entry.insert(0, "10")   # Insert the value '10'

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