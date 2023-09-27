# Created By ttv/AmsayNZ
# Fast customisation options
total_hours = int(input("How many hours should we start at: "))
minute_penalty = int(input("What should the penalty be for the banned words (minutes and whole numbers please): "))
inputing = True
bannedwords = []
channel_name = input("What channel should I look at: ")

while inputing:
    input_word = input("What word should be banned (press enter to escape out of loop): ")
    if input_word == '':
        inputing = False
    else:
        bannedwords.append(input_word)


# Main Code
import socket
import random
import time
import threading
import re
import winsound
from flask import Flask, render_template


app = Flask(__name__)
total_minutes = total_hours * 60
total_seconds = total_minutes * 60
pattern = r'\b\s*(' + '|'.join(re.escape(word) for word in bannedwords) + r')\s*\b'
rgx = re.compile(pattern, flags=re.IGNORECASE)


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

            if seconds <= 9:
                true_seconds = f'0{seconds}'
            else:
                true_seconds = seconds

            if minutes <= 9:
                true_minutes = f'0{minutes}'
            else:
                true_minutes = minutes

            output = f'{hours}:{true_minutes}:{true_seconds}'
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
    appended = random.randint(1, 9000)
    user = f'justinfan{appended}'
    # The channel to join
    channel = f'#{channel_name}'

    server = socket.socket()
    server.connect(connection_data)
    server.send(bytes('PASS ' + token + '\r\n', 'utf-8'))
    server.send(bytes('NICK ' + user + '\r\n', 'utf-8'))
    server.send(bytes('JOIN ' + channel + '\r\n', 'utf-8'))

    while True:
        # Connect to twitch and look for word custom.
        message = server.recv(2048)
        messagestr = str(message)

        matches = rgx.findall(messagestr.replace(' ', ''))
        was_match = False

        for match in matches:
            print("Found match!")
            was_match = True

        if was_match:
            total_seconds += minute_penalty * 60

        was_match = False
        matches = []


# Create a thread for the countdown timer and obs
countdown_thread = threading.Thread(target=countdown_timer)
mainp_thread = threading.Thread(target=main_program)

# Start the countdown timer and obs thread
mainp_thread.start()
countdown_thread.start()
obs()


print("Main program completed.")