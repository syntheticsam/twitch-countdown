# Twitch Countdown

If a word is detected on a twitch channel chat some time to a timer will be added. It defults to the word custom. 

# How to run!
Minimal Edition (min.py):
1. Download python and min.py and run
2. Enter your values

For Main Edition (main.py & templates folder):
1. Download python (personaly I use 3.11.5): https://www.python.org/downloads/
2. Open a new terminal and enter the command `pyhton -m pip install flask`
3. After that finishes you should now be able to go and run main.py (by default it will be set up to connect to the birnooce channel)
3b. If you wish to change the start times etc. open the file in a text editor RightClk > Open With > Notepad
4. To add the countdown to obs add a new browser source with the url: `127.0.0.1:8080`

# When the countdown ends a tone will play for 10 seconds
# TODO
1. Make it more user friendly (better customisation etc.)
2. Change the font
3. Add easy support for multiple words
