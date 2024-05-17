from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

def updateImage(*args):
    selection_index = display_names.index(varGraph.get())
    imagePath = f'{graph_names[selection_index]}.png'
    image = Image.open(imagePath)
    defaultPhoto = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=defaultPhoto)
    canvas.image = defaultPhoto 

# image
graph_names = ['surfaceTemperatureofPlanetsinSolorSystem',
               'mainCompositionofPlantsAtmosphereinSolorSystem',
               'boroughPerTypeofCuisine',
               'averageScoresClass']

# menu name
display_names = ['Average temperature of planets in solor system',
                 'Average composition of plants atmosphere in solor system',
                 'Borough per type of cuisine',
                 'Average score per evaluation type']
root.title("Lab4")

varGraph = tk.StringVar(root)
varGraph.set('Average temperature of planets in solor system')

dropdown = OptionMenu(root, varGraph, *display_names, command=updateImage)
dropdown.pack()

defaultImagePath = f'{graph_names[0]}.png'
defaultImage = Image.open(defaultImagePath)
defaultPhoto = ImageTk.PhotoImage(defaultImage)

canvas = Canvas(root, width=defaultImage.width, height=defaultImage.height)
canvas.create_image(0, 0, anchor=NW, image=defaultPhoto)
canvas.pack()

root.mainloop()
