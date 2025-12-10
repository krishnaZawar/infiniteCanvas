import pygame

class TextRenderer:
    def __init__(self, text : str, fontSize : int, color : str):
        self.font : pygame.font.Font = pygame.font.SysFont("Arial", fontSize)
        self.text = text
        self.color = color

        self.text_surface : pygame.Surface = self.font.render(self.text, True, color)
    
    def getRect(self) -> pygame.rect.Rect:
        return self.text_surface.get_rect()
    
    def draw(self, surface : pygame.Surface, x : int, y : int) -> None:
        surface.blit(self.text_surface, self.text_surface.get_rect(topleft=(x, y)))