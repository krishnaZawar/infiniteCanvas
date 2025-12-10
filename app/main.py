import pygame
from canvas import Canvas
from toolPanel import ToolPanel

from collider import pointToRectCollider

from objects.rectangle import Rectangle
from objects.circle import Circle

pygame.init()

def main():
    screen : pygame.Surface = pygame.display.set_mode((1000, 600))

    tools = [
        'move', 'select', 'rect', 'circle'
    ]

    canvas : Canvas = Canvas(1000, 600)
    tool_panel : ToolPanel = ToolPanel(tools, 300, 500, 400, 100)

    windowActive : bool = True
    drag : bool = False
    newObject : Rectangle | None= None

    drag_start, drag_end = [0, 0], [0, 0]
    last_mouse_pos = pygame.mouse.get_pos()

    while windowActive == True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                windowActive = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    canvas.deleteSelection()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pointToRectCollider(tool_panel.getRect(), mouse_pos):
                    tool_panel.update(mouse_pos, "left mouse button")
                    canvas.resetSelection()
                else:
                    drag = True
                    drag_start = mouse_pos
                    if tool_panel.active.getText() == 'select':
                        canvas.updateSelection(mouse_pos)
                    elif tool_panel.active.getText() == 'rect':
                        newObject = Rectangle(mouse_pos[0], mouse_pos[1], 0, 0) 
                    elif tool_panel.active.getText() == 'circle':
                        newObject = Circle(mouse_pos[0], mouse_pos[1], 0, 0)
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drag = False
                if newObject:
                    canvas.addObject(newObject)

                drag = False
                newObject = None

        if pointToRectCollider(tool_panel.getRect(), mouse_pos):
            tool_panel.update(mouse_pos, 'hover')

        if drag:
            if newObject:
                drag_end = mouse_pos
                newObject.setSize(drag_end[0]-drag_start[0], drag_end[1] - drag_start[1])
            if tool_panel.active.getText() == 'move':
                dx = mouse_pos[0] - last_mouse_pos[0]
                dy = mouse_pos[1] - last_mouse_pos[1]
                canvas.movePage(dx, dy)

        screen.fill((255, 255, 255))
        canvas.draw(screen)
        if newObject:
            newObject.draw(screen)
        tool_panel.draw(screen)

        last_mouse_pos = mouse_pos

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()