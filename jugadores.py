import random
import pickle
import pygame
import sys

class Random():
    def __init__(self, juego):
        self.juego = juego

    # Juega al juego de manera aleatoria hasta que termine
    def jugar(self):
        reloj = pygame.time.Clock()  # Para controlar la velocidad del juego
        while True:
            # Manejo de eventos de Pygame
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            accion = random.choice([0, 1, 2])  # Elige una acción aleatoria
            estado, recompensa, terminado = self.juego.step(accion)

            # Mostrar en consola las acciones, estado y recompensas
            print(f"Accion: {accion}, Estado: {estado}, Recompensa: {recompensa}")

            if terminado:
                print("El juego ha terminado.")
                break

            # Renderiza el juego después de cada movimiento
            self.juego.render()

            # Controlar el frame rate (velocidad del juego)
            reloj.tick(10)  # Limita el juego a 10 frames por segundo


class IA():
    def __init__(self, juego):
        self.juego = juego
        self.path = None
        self.Q = {}

    def set_path(self, path):
        self.path = path

    # Juega al juego hasta que termine, eligiendo la mejor acción según la tabla Q
    def jugar(self):
        raise NotImplementedError  # Completar si fuera necesario

    # Entrena el agente actualizando la tabla Q
    def entrenar(self):
        raise NotImplementedError  # Completar si fuera necesario

    def save(self):
        if self.path is not None:
            with open(self.path, 'wb') as f:
                pickle.dump(self.Q, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):
        if self.path is not None:
            with open(self.path, 'rb') as f:
                self.Q = pickle.load(f)
