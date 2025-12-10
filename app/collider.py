import pygame

def pointToRectCollider(rect : pygame.rect.Rect, point : tuple[int, int]) -> bool:
    return (rect.x <= point[0] and point[0] <= rect.x+rect.w) and (rect.y <= point[1] and point[1] <= rect.y+rect.h)

def pointToCircleCollider(circle: pygame.rect.Rect, point : tuple[int, int]) -> bool:
    xc, yc, r = circle.x+circle.w//2, circle.y+circle.h//2, circle.w//2
    return (xc-point[0])**2 + (yc-point[1])**2 <= r**2

def rectToRectCollider(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect) -> bool:
    xOverLap = max(0, rect1.x+rect1.w - rect2.x) if rect1.x < rect2.x else max(0, rect2.x+rect2.w - rect1.x)
    yOverLap = max(0, rect1.y+rect1.h - rect2.y) if rect1.y < rect2.y else max(0, rect2.y+rect2.h - rect1.y)

    return xOverLap and yOverLap