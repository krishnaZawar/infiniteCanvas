import pygame

class Rectangle:
    __type__ = 'rectangle'
    def __init__(self, global_x: int, global_y: int, w: int, h: int):
       self.setGeometry(global_x, global_y, w, h)
       self.updateLocalPos(0, 0)
       self.selected = False

    def setGeometry(self, x: int, y: int, w: int, h: int) -> None:
        self.global_x, self.global_y = x, y
        self.setSize(w, h)

    def setSize(self, w: int, h: int) -> None:
        self.w, self.h = max(0, w), max(0, h)

    def getRect(self, border: int = 0) -> pygame.rect.Rect:
        return pygame.rect.Rect(self.local_x+border, self.local_y+border, self.w-border, self.h-border)
    
    def setSelected(self, selected: bool) -> 'Rectangle':
        self.selected = selected
        return self
    
    def updateLocalPos(self, x_offset: int, y_offset: int) -> None:
        self.local_x = self.global_x - x_offset
        self.local_y = self.global_y - y_offset
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.selected:
            pygame.draw.rect(screen, "light grey", self.getRect(1), border_radius=self.w//20)

        pygame.draw.rect(screen, "black", self.getRect(), border_radius=self.w//20, width=2)