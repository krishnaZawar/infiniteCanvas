import pygame

class Circle:
    __type__ = 'circle'
    def __init__(self, global_x: int, global_y: int, w: int, h: int):
       self.setGeometry(global_x, global_y, w, h)
       self.updateLocalPos(0, 0)
       self.selected = False

    def setGeometry(self, x: int, y: int, w: int, h: int) -> None:
        self.global_x, self.global_y = x, y
        self.setSize(w, h)

    def setSize(self, w: int, h: int) -> None:
        self.w, self.h = max(0, w), max(0, h)

    def getRect(self) -> pygame.rect.Rect:
        return pygame.rect.Rect(self.local_x, self.local_y, self.w, self.h)
    
    def getLocalCenter(self) -> tuple[int, int]:
        return (self.local_x + self.w//2, self.local_y + self.h//2)
    
    def setSelected(self, selected: bool) -> 'Circle':
        self.selected = selected
        return self
    
    def updateLocalPos(self, x_offset: int, y_offset: int) -> None:
        self.local_x = self.global_x - x_offset
        self.local_y = self.global_y - y_offset
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.selected:
            pygame.draw.circle(screen, "light grey", self.getLocalCenter(), self.w//2-1)

        pygame.draw.circle(screen, "black", self.getLocalCenter(), self.w//2, width=2)