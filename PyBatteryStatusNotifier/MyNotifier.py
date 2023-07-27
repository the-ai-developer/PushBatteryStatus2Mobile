import BatteryStatus as bs
import PushNotification as Push
import time,pyfiglet
color = "\033[1;32m"
ascii_banner = pyfiglet.figlet_format("PyBatteryStatusNotifier")
colored_banner = f"{color}{ascii_banner}\033[0m"  # Reset color after printing
print(colored_banner)

print("[*]Process Started....")
while True:
    Result=bs.check()
    if Result != 'None':
        Push.PushNotification(Result)
    try:
        time.sleep(300)
    except KeyboardInterrupt:
        print("[*]Quitting....")
        break
