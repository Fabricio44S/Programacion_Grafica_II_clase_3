# from tkinter import Canvas
# from pygame import *
# import asyncio

# import pygame, sys
from vpython import *
import asyncio
import random
## Crear de forma recursiva otro objeto(cubo) en 3D de abajo hacia arriba, de forma asincrona o paralela 
# crear otros dos objetos que se esten moviendo hacia las esquinas de la patalla 
# Poner 5 colores en una lista y crear un metodo asincrono que al azar cambie de color, se pude llamar o ejecutar cada 5 segundo y lo debemos ejecutar de forma asincrona 
# pygame.init()
scene = canvas(title="Combinacion de figuras 3D", width=800, height=600,)

scene.ortho = True
# scene.camera.pos = vector(0,0,20)
# scene.camera.axis = vector(0,0,-1)


def crear_figura(position, lon1,lon2,lon3, n):
    if n == 0:
        return
    cubo = box(pos=position, length=lon1, height=lon2, width=lon3 , color = color.cyan)
    crear_figura(position + vector(0, 0.8 * lon2,0), lon1 * 0.8, lon2 *0.8, lon3 *0.8,  n - 1 )

crear_figura(vector(0,-5,0), 2,2,2, 5)

async def mover_objeto(objeto, eje):
    while True:
        objeto.pos += eje * 0.1
        if objeto.pos.x > 4 or objeto.pos.y > 4 or objeto.pos.z > 4:
            objeto.pos = vector(-2, -2, 0)
        await asyncio.sleep(0.1)

piramide = pyramid(pos=vector(-2,0,0), size=vector(1,2,3), color = color.green) 
elipse = ellipsoid(pos=vector(-2,0,0), size=vector(2,1,3), color = color.white)   

async def cambiar_color():

    color_lista = [color.red, color.green, color.blue, color.yellow, color.orange]
    while True:
        piramide.color = random.choice(color_lista)
        elipse.color = random.choice(color_lista)
        for _ in range(50):
            rate(60)
        await asyncio.sleep(5)


async def main():
    
    task1 = asyncio.create_task(mover_objeto(piramide, vector(1, 1, 0)))
    task2 = asyncio.create_task(mover_objeto(elipse, vector(1, -1, 0)))
    task3 = asyncio.create_task(cambiar_color())
    
    await asyncio.gather(task1, task2, task3)
   
asyncio.run(main())




