import os

# os.listdir(b'C:\Users\Saluc\AppData\Local')
chemin = 'C:/Users/'+os.getcwd().split('\\')[2]+'/AppData/Local/'

if os.path.exists(chemin+'virus.py') :
    