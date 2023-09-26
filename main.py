# Created By ttv/AmsayNZ

import socket
import time
import threading
from re import search
import winsound
from flask import Flask, render_template

app = Flask(__name__)

# Global variable to store the value to display
value_to_display = "Initial Value"

connection_data = ('irc.chat.twitch.tv', 6667)
# This can be anything
token = 'arealpassword!'
# JustinfanXXXX (anom username)
user = 'justinfan2222'
# The channel to join
channel = '#amsaynz'

# Starts at 2 hours
total_hours = 2
total_minutes = total_hours * 60
total_seconds = total_minutes * 60


def countdown_timer():
    global total_seconds, value_to_display

    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        print(f"Time left: {minutes} minutes {seconds} seconds")
        value_to_display = total_seconds
        time.sleep(1)
        total_seconds -= 1

    print("Time's up! Its Custom Time!")
    winsound.Beep(250, 10000)


def obs():
    global value_to_display

    @app.route('/')
    def home():
        return render_template('index.html', value=value_to_display)

    @app.route('/value')
    def get_value():
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        output = f'{hours}:{minutes}:{seconds}'
        return output

    if __name__ == '__main__':
        app.run(debug=True, port=8080)


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

        # Uses rx, theoreticly could add "or" statements to extend the word search :)
        if search(bannedword, messagestr):
            print("Custom was said!")
            minutes_to_add = 20
            total_seconds += minutes_to_add * 60


# Create a thread for the countdown timer and obs
countdown_thread = threading.Thread(target=countdown_timer)
main_thread = threading.Thread(target=main_program)

# Start the countdown timer and obs thread
countdown_thread.start()
main_thread.start()

obs()


# Wait for the countdown timer thread to finish (optional)
countdown_thread.join()

print("Main program completed.")
