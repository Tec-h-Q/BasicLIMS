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

        # Define consistent widths for labels and input fields
        LABEL_WIDTH = 15
        INPUT_WIDGET_WIDTH = 20

        # --- Batch Number Field ---
        batch_frame = tk.Frame(master)
        batch_frame.pack(pady=5, fill='x', padx=50)

        self.batch_label = tk.Label(batch_frame, text="Batch Number:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.batch_label.pack(side='left', padx=(0, 10))

        self.batch_entry = tk.Entry(batch_frame, width=INPUT_WIDGET_WIDTH)
        self.batch_entry.pack(side='right', expand=True, fill='x')
        # --- End Batch Number Field ---

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

        # --- Measurement Field (New) ---
        measurement_frame = tk.Frame(master)
        measurement_frame.pack(pady=5, fill='x', padx=50)

        self.measurement_label = tk.Label(measurement_frame, text="Measurement:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.measurement_label.pack(side='left', padx=(0, 10))

        self.measurement_entry = tk.Entry(measurement_frame, width=INPUT_WIDGET_WIDTH)
        self.measurement_entry.pack(side='right', expand=True, fill='x')
        # --- End Measurement Field ---

        # --- Equipment Dropdown List ---
        equipment_frame = tk.Frame(master)
        equipment_frame.pack(pady=5, fill='x', padx=50)

        self.equipment_label = tk.Label(equipment_frame, text="Equipment Type:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.equipment_label.pack(side='left', padx=(0, 10))

        self.equipment_options = ["Volume", "Mass", "Temperature", "Density", "Purity"]
        self.selected_equipment = tk.StringVar(master)
        self.selected_equipment.set(self.analysis_options[0])

        self.equipment_dropdown = tk.OptionMenu(equipment_frame, self.selected_equipment, *self.equipment_options)
        self.equipment_dropdown.pack(side='right', expand=True, fill='x')
        self.equipment_dropdown.config(width=INPUT_WIDGET_WIDTH)
        # --- End equipment Dropdown List ---

        # --- Last Calibration Field (New) ---
        calibration_frame = tk.Frame(master)
        calibration_frame.pack(pady=5, fill='x', padx=50)

        self.calibration_label = tk.Label(calibration_frame, text="Last Calibration:", font=("Arial", 12), width=LABEL_WIDTH, anchor='w')
        self.calibration_label.pack(side='left', padx=(0, 10))

        self.calibration_entry = tk.Label(calibration_frame,text="10" ,width=INPUT_WIDGET_WIDTH)
        self.calibration_entry.pack(side='right', expand=True, fill='x')
        
        # --- End Last Calibration Field ---

        # --- Buttons ---
        button_frame = tk.Frame(master)
        button_frame.pack(side='bottom', pady=20, fill='x', padx=20)

        # Create a sub-frame for the "action" buttons
        action_buttons_frame = tk.Frame(button_frame)
        action_buttons_frame.pack(side='left', expand=True, fill='x', padx=(0, 10)) # Add some space between action and back button

        self.import_button = tk.Button(action_buttons_frame, text="Import Measurement", command=self.import_measurement, width=20, height=2, font=("Arial", 10, "bold"))
        self.import_button.pack(side='left', padx=5, expand=True) # Use smaller padx within this frame

        self.publish_button = tk.Button(action_buttons_frame, text="Publish Analysis", command=self.publish_analysis, width=20, height=2, font=("Arial", 10, "bold"))
        self.publish_button.pack(side='left', padx=5, expand=True)

        # Back button stays on the right
        self.back_button = tk.Button(button_frame, text="Back", command=self.go_back, width=20, height=2, font=("Arial", 10))
        self.back_button.pack(side='right', padx=10) # No expand here if you want it fixed width on the right
        # --- End Buttons ---

        self.master.protocol("WM_DELETE_WINDOW", self.go_back)

    def go_back(self):
        self.master.destroy()
        if self.main_window_root:
            self.main_window_root.deiconify()

    def import_measurement(self):
        self.measurement_entry.delete(0, tk.END)
        self.measurement_entry.insert(0, "10")

    def publish_analysis(self):
        # Placeholder for your publish analysis logic
        print("Publish Analysis button clicked!")
        # You would typically gather data from the fields here
        batch_num = self.batch_entry.get()
        analysis_type = self.selected_analysis.get()
        measurement = self.measurement_entry.get()
        equipment_type = self.selected_equipment.get()
        last_calibration = self.calibration_entry.get()
        
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