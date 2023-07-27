import psutil

def check():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if plugged==True and percent>=90:
        return f"Your Laptop's Battery Is {percent}% Full...UnPlug From Charger!!"
    elif plugged==False and percent<30:
        return f"Your Laptop's Battery Is Only {percent}% Left...PlugIn Charger!!"
    else:
        return 'None'