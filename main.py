# Created By ttv/AmsayNZ
# Fast customisation options
total_hours = 2
minute_penalty = 20
bannedword = 'custom'


# Main Code
import socket
import time
import threading
from re import search
import winsound
from flask import Flask, render_template


app = Flask(__name__)
total_minutes = total_hours * 60
total_seconds = total_minutes * 60


def countdown_timer():
    global total_seconds

    while total_seconds > 0:
        time.sleep(1)
        total_seconds -= 1

    print("Time's up! Its Custom Time!")
    winsound.Beep(250, 10000)


def obs():

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/value')
    def get_value():
        if total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            output = f'{hours}:{minutes}:{seconds}'
        else:
            output = 'Time for a custom!'
        return output

    if __name__ == '__main__':
        app.run(debug=False, port=8080)


def main_program():
    global total_seconds, minute_penalty
    connection_data = ('irc.chat.twitch.tv', 6667)
    # This can be anything
    token = 'arealpassword!'
    # JustinfanXXXX (anom username)
    user = 'justinfan2222'
    # The channel to join
    channel = '#birnooce'

    server = socket.socket()
    server.connect(connection_data)
    server.send(bytes('PASS ' + token + '\r\n', 'utf-8'))
    server.send(bytes('NICK ' + user + '\r\n', 'utf-8'))
    server.send(bytes('JOIN ' + channel + '\r\n', 'utf-8'))

    while True:
        # Connect to twitch and look for word custom.
        message = server.recv(2048)
        messagestr = str(message)


        # Uses rx, theoreticly could add "or" statements to extend the word search :)
        if search(bannedword, messagestr):
            print("Word was said!")
            total_seconds += minute_penalty * 60


# Create a thread for the countdown timer and obs
countdown_thread = threading.Thread(target=countdown_timer)
mainp_thread = threading.Thread(target=main_program)

# Start the countdown timer and obs thread
mainp_thread.start()
countdown_thread.start()
obs()


print("Main program completed.")