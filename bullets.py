import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создание пуль согласно положения пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 7)
        self.color = 26, 35, 126
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули п оси у"""
        self.y -= self.speed
        self.rect.y = self.y

    def bullet_draw(self):
        """отрисовка пули"""
        pygame.draw.rect(self.screen, self.color, self.rect)
