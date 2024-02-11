import tkinter as tk
from datetime import datetime, timedelta

class PlantTracker:
    def __init__(self):
        self.plants = {}  # Dictionary to store plant information

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Plant Watering Tracker")

        # Plant selection dropdown
        self.plant_label = tk.Label(self.root, text="Select Plant:")
        self.plant_label.pack()

        self.plant_var = tk.StringVar()
        self.plant_dropdown = tk.OptionMenu(self.root, self.plant_var, *self.plants.keys())
        self.plant_dropdown.pack()

        # Last watered entry
        self.last_watered_label = tk.Label(self.root, text="Last Watered:")
        self.last_watered_label.pack()

        self.last_watered_var = tk.StringVar()
        self.last_watered_entry = tk.Entry(self.root, textvariable=self.last_watered_var)
        self.last_watered_entry.pack()

        # Button to record watering
        self.water_button = tk.Button(self.root, text="Water Plant", command=self.water_plant)
        self.water_button.pack()

        # Check plants button
        self.check_button = tk.Button(self.root, text="Check Plants", command=self.check_plants)
        self.check_button.pack()

    def water_plant(self):
        plant_name = self.plant_var.get()
        last_watered = self.last_watered_var.get()

        # Convert last watered to datetime object
        last_watered_date = datetime.strptime(last_watered, "%Y-%m-%d")

        # Update or add plant entry
        self.plants[plant_name] = last_watered_date

        # Clear the entry fields
        self.plant_var.set('')
        self.last_watered_var.set('')

    def check_plants(self):
        current_date = datetime.now()

        # Preset time for each specific plant (you can adjust these values)
        preset_time = {
            'Plant1': 7,   # 7 days
            'Plant2': 5,   # 5 days
            'Plant3': 10   # 10 days
            # Add more plants as needed
        }

        for plant, last_watered_date in self.plants.items():
            days_since_last_watered = (current_date - last_watered_date).days

            if plant in preset_time and days_since_last_watered > preset_time[plant]:
                print(f"{plant} needs to be watered!")

if __name__ == "__main__":
    tracker = PlantTracker()
    tracker.root.mainloop()
