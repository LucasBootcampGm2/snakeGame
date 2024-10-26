import pygame
import sys
import random

class Snake():
    def __init__(self, tamano):
        self.tamano = tamano
        self.reset()

    def reset(self):
        self.serpiente = [(7, 7)]
        self.fruta = (random.randint(0, self.tamano - 1), random.randint(0, self.tamano - 1))
        self.longitud = 1
        self.direccion = (0, 1)  

    def step(self, accion):
        if accion == 1:
            self.direccion = (-self.direccion[1], self.direccion[0]) 
        elif accion == 2:
             self.direccion = (self.direccion[1], -self.direccion[0])  

        nueva_cabeza = (self.serpiente[0][0] + self.direccion[0], self.serpiente[0][1] + self.direccion[1])

        if (nueva_cabeza in self.serpiente) or (nueva_cabeza[0] < 0 or nueva_cabeza[0] >= self.tamano or nueva_cabeza[1] < 0 or nueva_cabeza[1] >= self.tamano):
           return None, -1, True

        self.serpiente = [nueva_cabeza] + self.serpiente[:self.longitud - 1]

        if nueva_cabeza == self.fruta:
            self.longitud += 1
            self.fruta = (random.randint(0, self.tamano - 1), random.randint(0, self.tamano - 1))
            return None, 1, False  

        return None, 0, False  

    def render(self):
        Ventana.venta.fill(Ventana.BACKGROUND_COLOR)
        
        for parte in self.serpiente:
            pygame.draw.rect(Ventana.venta, (0, 255, 0), (parte[0] * Ventana.CELL_SIZE, parte[1] * Ventana.CELL_SIZE, Ventana.CELL_SIZE, Ventana.CELL_SIZE))

        pygame.draw.rect(Ventana.venta, (255, 0, 0), (self.fruta[0] * Ventana.CELL_SIZE, self.fruta[1] * Ventana.CELL_SIZE, Ventana.CELL_SIZE, Ventana.CELL_SIZE))

        pygame.display.update()

class Ventana:
    GRID_SIZE = 16
    CELL_SIZE = 16  
    WIDTH = GRID_SIZE * CELL_SIZE
    HEIGHT = GRID_SIZE * CELL_SIZE
    pygame.init()
    venta = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SnakeGame")
    GRID_COLOR = (200, 200, 200)
    BACKGROUND_COLOR = (0, 0, 0)

