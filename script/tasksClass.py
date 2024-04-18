import pygame
from script.constants import *


class Task:
    task_no = 1

    def __init__(self, description: str = "complete this task") -> None:
        self.num = self.task_no
        Task.task_no += 1
        self.description = description
        self.status = PENDIGN
        self.precentage = 0

        self.display = pygame.Surface(
            (100, 40),
        )
        # self.display.

    def complete(self):
        self.status = COMPLETED

    def display_task(self, screen: pygame.Surface):
        screen.blit(self.display)
