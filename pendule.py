from math import *
import csv
import os

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

l = 1  # longueur du fil en m   
t = 0  # temps initialisation en s
dt = 0.01  # le pas
theta = pi/4  # initialisation de l'angle
dtheta = 0  # vitesse angulaire
g = 9.8  # accélération de la pesanteur m/s**2


newDirectory = ""


os.chdir(newDirectory)

def writtefile(theta, t):
    with open('data.csv', 'a', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([round(theta,3), round(t,3)])

def angularacceleration(g, l, theta):
    result = (-g / l) * sin(theta)
    return result

def calculfunction(l, t, dt, theta, g, dtheta):
    print(theta, t)
    positions = []  # Liste pour stocker les positions du point
    for i in range(1000):
        t = t + dt
        dtheta = dtheta + angularacceleration(g, l, theta) * dt
        theta = theta + dtheta * dt
        writtefile(theta, t)
        positions.append((t, theta))  
        print(theta, t)

    return positions 

def main():
    with open('data.csv', 'w', newline='') as fichier:  
        writer = csv.writer(fichier)

    positions = calculfunction(l, t, dt, theta, g, dtheta)

    # Extraire les coordonnées des positions
    temps, angles = zip(*positions)

    # Initialiser la figure et l'axe pour le graphique
    fig, ax = plt.subplots()
    point, = ax.plot([], [], 'ro', linestyle='-', linewidth=1) 

    # limites du graphique
    ax.set_xlim(min(temps), max(temps))
    ax.set_ylim(min(angles), max(angles))

    # Titres et noms des axes
    ax.set_title("simulation d'un pendule simple au cours du temps")
    ax.set_xlabel("Temps en s")
    ax.set_ylabel("Angle en rad")

    # Fonction d'initialisation de l'animation
    def init():
        point.set_data([], [])
        return point,

    # Fonction d'animation qui met à jour le point sur le graphique
    def animate(i):
        x = temps[:i+1]
        y = angles[:i+1]
        point.set_data(x, y)
        return point,

    # Créer l'animation
    ani = FuncAnimation(fig, animate, frames=len(temps), init_func=init, interval=10, blit=True)

    # Affichage
    plt.show()

if __name__ == "__main__":
    main()
