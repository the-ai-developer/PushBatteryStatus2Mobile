from pushbullet import Pushbullet
pb = Pushbullet('<YOUR_PUSHBULLET_API>')
title = "Alert From Laptop!"
def PushNotification(message):
    pb.push_note(title, message)
    print("Sent Successfully!")