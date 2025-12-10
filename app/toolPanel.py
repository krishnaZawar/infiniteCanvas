import pygame
from UI.button import Button
from collider import pointToRectCollider

class ToolPanel:
    def __init__(self, tools : list[str], x : int, y : int, w : int, h : int):
        self.setGeometry(x, y, w, h)
        self.tool_dict : dict = {}
        self.tool_hover_color : str = "light grey"
        self.tool_select_color : str = "dark grey"
        self.tools = tools

        self.initTools()

        self.active = self.tool_dict[tools[0]]
        self.active.setSelected(True)

    def setGeometry(self, x : int, y : int, w : int, h : int) -> None:
        self.x, self.y, self.w, self.h = x, y, w, h

    def initTools(self) -> None:
        def initTool(text : str, x : int, y : int, w : int, h : int) -> None:
            self.tool_dict[text] = Button(text, x, y, w, h)
            self.tool_dict[text].setColors(self.tool_hover_color, self.tool_select_color)

        n = len(self.tools)
        x_dist, y_dist = 20, 20     # dist between buttons and borders
        button_width, button_height = (self.w - (n+1)*x_dist)//n, (self.h - 2*y_dist)

        cur_x, cur_y = self.x + x_dist, self.y + y_dist

        for tool in self.tools:
            initTool(tool, cur_x, cur_y, button_width, button_height)
            cur_x += x_dist + button_width

    def getRect(self) -> pygame.rect.Rect:
        return pygame.rect.Rect(self.x, self.y, self.w, self.h)

    def draw(self, screen : pygame.Surface) -> None:
        for tool in self.tool_dict:
            self.tool_dict[tool].draw(screen)

    def update(self, mouse_pos : tuple[int, int], update_event: str) -> None:
        if update_event == "hover":
            for tool in self.tool_dict:
                self.tool_dict[tool].setHover(False)
                if pointToRectCollider(self.tool_dict[tool].getRect(), mouse_pos):
                    if self.active != self.tool_dict[tool]:
                        self.tool_dict[tool].setHover(True)

        if update_event == "left mouse button":
            for tool in self.tool_dict:
                if pointToRectCollider(self.tool_dict[tool].getRect(), mouse_pos):
                    if self.active:
                        self.active.setSelected(False)
                    self.active = self.tool_dict[tool].setSelected(True)