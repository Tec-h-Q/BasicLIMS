import tkinter as tk
from datetime import datetime

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

        LABEL_WIDTH = 15
        INPUT_WIDGET_WIDTH = 20
        BUTTON_WIDTH = 10

        # --- Batch Number Field with Search Button ---
        batch_frame = tk.Frame(master)
        batch_frame.pack(pady=5, fill='x', padx=50)

        self.batch_label = tk.Label(batch_frame, text="Batch Number:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.batch_label.pack(side='left', padx=(0, 10))

        self.batch_entry = tk.Entry(batch_frame, width=INPUT_WIDGET_WIDTH)
        self.batch_entry.pack(side='left', expand=True, fill='x')

        self.batch_search_button = tk.Button(batch_frame, text="Search", command=self.search_batch, width=BUTTON_WIDTH)
        self.batch_search_button.pack(side='left', padx=(10, 0))
        # --- End Batch Number Field with Search Button ---

        # --- Analysis Dropdown List ---
        analysis_frame = tk.Frame(master)
        analysis_frame.pack(pady=5, fill='x', padx=50)

        self.analysis_label = tk.Label(analysis_frame, text="Analysis Type:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.analysis_label.pack(side='left', padx=(0, 10))

        self.analysis_options = ["Volume", "Mass", "Temperature", "Density", "Purity"]
        self.selected_analysis = tk.StringVar(master)
        self.selected_analysis.set(self.analysis_options[0])

        self.analysis_dropdown = tk.OptionMenu(analysis_frame, self.selected_analysis, *self.analysis_options)
        self.analysis_dropdown.pack(side='right', expand=True, fill='x')
        self.analysis_dropdown.config(width=INPUT_WIDGET_WIDTH)
        # --- End Analysis Dropdown List ---

        # --- Measurement Field (New) with Import Button ---
        measurement_frame = tk.Frame(master)
        measurement_frame.pack(pady=5, fill='x', padx=50)

        self.measurement_label = tk.Label(measurement_frame, text="Measurement:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.measurement_label.pack(side='left', padx=(0, 10))

        self.measurement_entry = tk.Entry(measurement_frame, width=INPUT_WIDGET_WIDTH)
        self.measurement_entry.pack(side='left', expand=True, fill='x') # Changed to side='left'

        # Moved the Import Measurement button here
        self.import_button = tk.Button(measurement_frame, text="Import", command=self.import_measurement, width=BUTTON_WIDTH) # Smaller text and width
        self.import_button.pack(side='left', padx=(10, 0)) # Packed to the left of the entry, with padding
        # --- End Measurement Field with Import Button ---

        # --- Equipment Dropdown List ---
        equipment_frame = tk.Frame(master)
        equipment_frame.pack(pady=5, fill='x', padx=50)

        self.equipment_label = tk.Label(equipment_frame, text="Equipment Type:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.equipment_label.pack(side='left', padx=(0, 10))

        self.equipment_options = ["Volume", "Mass", "Temperature", "Density", "Purity"]
        self.selected_equipment = tk.StringVar(master)
        self.selected_equipment.set(self.equipment_options[0])

        self.equipment_dropdown = tk.OptionMenu(equipment_frame, self.selected_equipment, *self.equipment_options)
        self.equipment_dropdown.pack(side='right', expand=True, fill='x')
        self.equipment_dropdown.config(width=INPUT_WIDGET_WIDTH)
        # --- End equipment Dropdown List ---

        # --- Last Calibration Field (New) ---
        calibration_frame = tk.Frame(master)
        calibration_frame.pack(pady=5, fill='x', padx=50)

        self.calibration_label = tk.Label(calibration_frame, text="Last Calibration:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.calibration_label.pack(side='left', padx=(0, 10))

        self.calibration_display_label = tk.Label(calibration_frame, text="N/A", font=("Arial", 12), width=INPUT_WIDGET_WIDTH, anchor='w', relief="groove")
        self.calibration_display_label.pack(side='right', expand=True, fill='x')
        # --- End Last Calibration Field ---

        # --- Buttons (Remaining) ---
        # The 'action_buttons_frame' now only contains the Publish button
        button_frame = tk.Frame(master)
        button_frame.pack(side='bottom', pady=20, fill='x', padx=20)

        action_buttons_frame = tk.Frame(button_frame)
        action_buttons_frame.pack(side='left', expand=True, fill='x', padx=(0, 10))

        # Only Publish button remains here
        self.publish_button = tk.Button(action_buttons_frame, text="Publish Analysis", command=self.publish_analysis, width=20, height=2, font=("Arial", 10, "bold"))
        self.publish_button.pack(side='left', padx=5) # No expand=True here if you want it compact within its frame

        self.back_button = tk.Button(button_frame, text="Back", command=self.go_back, width=20, height=2, font=("Arial", 10))
        self.back_button.pack(side='right', padx=10)
        # --- End Buttons ---

        self.master.protocol("WM_DELETE_WINDOW", self.go_back)

    def go_back(self):
        self.master.destroy()
        if self.main_window_root:
            self.main_window_root.deiconify()

    def search_batch(self):
        batch_number = self.batch_entry.get()
        if batch_number:
            print(f"Searching for Batch Number: {batch_number}")
            # Placeholder for your actual batch search logic
            if batch_number == "BATCH123":
                self.selected_analysis.set("Mass")
                self.measurement_entry.delete(0, tk.END)
                self.measurement_entry.insert(0, "500 kg")
                self.selected_equipment.set("Mass")
                self.calibration_display_label.config(text="2025-01-15")
                print("Batch found!")
            else:
                self.selected_analysis.set("Volume")
                self.measurement_entry.delete(0, tk.END)
                self.measurement_entry.insert(0, "")
                self.selected_equipment.set(self.equipment_options[0])
                self.calibration_display_label.config(text="N/A")
                print("Batch not found or no data.")
        else:
            print("Please enter a batch number to search.")

    def import_measurement(self):
        # Placeholder for importing measurement (e.g., from a sensor, a file)
        print("Import Measurement button clicked!")
        # For demonstration, let's just put a random value or a placeholder
        import random
        random_measurement = round(random.uniform(10.0, 100.0), 2)
        self.measurement_entry.delete(0, tk.END)
        self.measurement_entry.insert(0, str(random_measurement))


    def publish_analysis(self):
        print("Publish Analysis button clicked!")
        batch_num = self.batch_entry.get()
        analysis_type = self.selected_analysis.get()
        measurement = self.measurement_entry.get()
        equipment_type = self.selected_equipment.get()
        last_calibration = self.calibration_display_label.cget("text")

        print(f"Batch: {batch_num}, Analysis: {analysis_type}, Measurement: {measurement}, Equipment: {equipment_type}, Calibration: {last_calibration}")



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

        self.back_button = tk.Button(master, text="Back", command=self.go_back, width=15, height=1)
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