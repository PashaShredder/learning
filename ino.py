import pygame


class Ino(pygame.sprite.Sprite):
    """класс пришельца"""

    def __init__(self, screen):
        """иниц. и задаем начальнуб позю"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("image/green.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод нло на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение нло в новое место"""
        self.y += 0.1
        self.rect.y = self.y
