import pygame
from UI.textRenderer import TextRenderer

class Button:
    def __init__(self, text: str, x : int, y : int, w : int, h : int):
        self.hovered : bool = False
        self.selected : bool = False
        self.hover_color : str
        self.select_color : str
        self.setGeometry(x, y, w, h)

        self.text : str = text
        self.text_renderer = TextRenderer(self.text, 20, "black")

    def setGeometry(self, x : int, y : int, w : int, h : int) -> None:
        self.x, self.y, self.w, self.h = x, y, w, h

    def setColors(self, hover_color : str, select_color : str) -> None:
        self.hover_color = hover_color
        self.select_color = select_color

    def setHover(self, hover: bool) -> None:
        self.hovered = hover

    def setSelected(self, selected: bool) -> 'Button':
        self.selected = selected
        return self
    
    def getText(self) -> str:
        return self.text

    def getRect(self, border: int = 0) -> pygame.rect.Rect:
        return pygame.rect.Rect(self.x+border, self.y+border, self.w-border, self.h-border)

    def draw(self, screen : pygame.Surface) -> None:
        width = 3
        if self.selected:
            pygame.draw.rect(screen, self.select_color, self.getRect(width-1), border_radius=self.w//5)
        elif self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.getRect(width-1), border_radius=self.w//5)

        pygame.draw.rect(screen, "black", self.getRect(), border_radius=self.w//5, width=width)

        rect = self.text_renderer.getRect()
        text_x, text_y = (self.x + (self.w - rect.w)//2), (self.y + (self.h - rect.h)//2)

        self.text_renderer.draw(screen, text_x, text_y)