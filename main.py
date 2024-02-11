from datetime import datetime, timedelta
import tkinter as tk
from datetime import datetime

class Plant:
    def __init__(self, name, last_watered):
        self.name = name
        self.last_watered = last_watered

    def water(self):
        self.last_watered = datetime.now()

    def needs_watering(self, days_interval):
        return (datetime.now() - self.last_watered).days >= days_interval

# Example usage:
plants = {
    'Rose': Plant('Rose', datetime.now() - timedelta(days=1)),
    'Fern': Plant('Fern', datetime.now() - timedelta(days=3))
}

preset_interval =  2  # Preset interval for watering in days

for plant_name, plant in plants.items():
    if plant.needs_watering(preset_interval):
        print(f"{plant_name} needs watering.")

class PlantApp:
    def __init__(self, root):
        self.root = root
        self.plants = {}
        self.create_widgets()

    def create_widgets(self):
        self.plant_label = tk.Label(self.root, text="Select a plant to water:")
        self.plant_label.pack()

        self.plant_listbox = tk.Listbox(self.root)
        self.plant_listbox.pack()

        self.water_button = tk.Button(self.root, text="Water", command=self.water_selected_plant)
        self.water_button.pack()

    def water_selected_plant(self):
        selected_plant = self.plant_listbox.get(tk.ACTIVE)
        if selected_plant in self.plants:
            self.plants[selected_plant].water()
            print(f"{selected_plant} has been watered.")

    def add_plant(self, plant_name):
        self.plant_listbox.insert(tk.END, plant_name)
        self.plants[plant_name] = Plant(plant_name, datetime.now())

if __name__ == "__main__":
    root = tk.Tk()
    app = PlantApp(root)
    app.add_plant("Rose")
    app.add_plant("Fern")
    root.mainloop()
