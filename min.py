# Created By ttv/AmsayNZ

import socket
import time
import threading
from re import search
import winsound

connection_data = ('irc.chat.twitch.tv', 6667)
# This can be anything
token = 'arealpassword!'
# JustinfanXXXX (anom username)
user = 'justinfan2222'
# The channel to join
channel = '#birnooce'

# Starts at 200 mins
total_seconds = 12000


def countdown_timer():
    global total_seconds
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        print(f"Time left: {minutes} minutes {seconds} seconds")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up! Its Custom Time!")
    winsound.Beep(250, 10000)


def main_program():
    global total_seconds

    server = socket.socket()
    server.connect(connection_data)
    server.send(bytes('PASS ' + token + '\r\n', 'utf-8'))
    server.send(bytes('NICK ' + user + '\r\n', 'utf-8'))
    server.send(bytes('JOIN ' + channel + '\r\n', 'utf-8'))

    while True:
        # Connect to twitch and look for word custom.
        message = server.recv(2048)
        messagestr = str(message)
        bannedword = 'custom'

        # Uses rx theoreticly could add or statements to extend functionality
        if search(bannedword, messagestr):
            print("Found!")
            minutes_to_add = 20
            total_seconds += minutes_to_add * 60
        else:
            print("Not found!")


# Create a thread for the countdown timer
countdown_thread = threading.Thread(target=countdown_timer)

# Start the countdown timer thread
countdown_thread.start()

# Start your main program
main_program()

# Wait for the countdown timer thread to finish (optional)
countdown_thread.join()

print("Main program completed.")