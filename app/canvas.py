import pygame

from objects.rectangle import Rectangle
from objects.circle import Circle

from collider import pointToRectCollider, pointToCircleCollider, rectToRectCollider

class Canvas:
    def __init__(self, w: int, h: int):
        self.x_offset : int = 0
        self.y_offset : int = 0
        self.w, self.h = w, h

        self.objects : list = []
        self.selected_object = None

    def addObject(self, obj) -> None:
        if not obj.w or not obj.h:
            return
        obj.setGeometry(obj.local_x + self.x_offset, obj.local_y + self.y_offset, obj.w, obj.h)
        self.objects.append(obj)

    def draw(self, screen: pygame.Surface) -> None:
        for obj in self.objects:
            if rectToRectCollider(self.getRect(), obj.getRect()):
                obj.draw(screen)

    def getRect(self) -> pygame.rect.Rect:
        return pygame.rect.Rect(0, 0, self.w, self.h)

    def resetSelection(self) -> None:
        if self.selected_object:
            self.selected_object.setSelected(False)
        self.selected_object = None

    def deleteSelection(self) -> None:
        if self.selected_object:
            self.objects.remove(self.selected_object)
        self.selected_object = None

    def updateSelection(self, mouse_pos : tuple[int, int]) -> None:
        self.resetSelection()

        for obj in self.objects[::-1]:
            if obj.__type__ == 'rectangle':
                if pointToRectCollider(obj.getRect(), mouse_pos):
                    self.selected_object = obj.setSelected(True)
                    break
            if obj.__type__ == 'circle':
                if pointToCircleCollider(obj.getRect(), mouse_pos):
                    self.selected_object = obj.setSelected(True)
                    break

    def movePage(self, dx: int, dy: int) -> None:
        self.x_offset -= dx
        self.y_offset -= dy

        self.updateObjectPositions()

    def updateObjectPositions(self) -> None:
        for obj in self.objects:
            obj.updateLocalPos(self.x_offset, self.y_offset)    