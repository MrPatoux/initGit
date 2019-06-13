import os
import subprocess

def initGit():
    try:
        # Change the current working Directory
        os.chdir("/Users/mrpatoux/Documents/Documents - Mac mini de Jérémie/Projets Git/")
    except OSError:
        print("Une erreur est survenue. Veuillez réessayer ultérieurment.")
        exit()

if __name__ == '__main__':
    initGit()





