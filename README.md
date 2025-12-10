
# <p align = "center">Infinite Canvas</p>
This is a project aimed at understanding the working and implementation of canvases with endless canvas size.

## How does such a canvas work
Talking about an infinite canvas, it is not something where it actually has infinite canvas size and storage for it. 
It is rather a smart implementation using global coordinates and local coordinates from a point to our advantage, Something similar to what many games with infinite scroll area implement under the hood.
### Core Idea
The canvas can be considered similar to cameras in games, where the things, whose even a small part is visible, are drawn to the screen. A more technical phrasing of the same sentence is "Objects that overlap with the canvas/camera area are drawn to the screen".
This statement provides a more clear picture of what should  be done.

The key idea here is not to move the objects but the canvas, using x and y offset values. These Offset values can then be used to calculate relative distance between canvas and the object. This relative distance can be used to check whether it overlaps with the canvas or not, and hence should it be drawn or not.
Therefore, we don't really move any object but just use the offset to draw objects relative to the canvas position. This can be abstractly understood as "moving the canvas".

The mathematical implementation of this logic can be understood from the code.

### advantages of this approach
1. We don't have to perform complex calculations, simple collision checks  can be used, making the implementation easier.
2. We can check which objects need not be drawn, which saves resources and time.

# Constraints considered while Development
1. The project should not support zooming functionality.
2. An object once created cannot be modified or moved, it can just be deleted.
3. Allow creation of only two kinds of objects, rectangle and circle.
4. Any changes to the canvas should not be persistent.

These constraints were considered to allow us to focus more on the logic behind it and build a working prototype in minimal time.

# How to Use
To start using the canvas, run the "app/main.py" file.
The canvas has 5 options:
1. move: move around the canvas
2. select: select any object/shape already drawn to the screen.
3. rect: to draw a new rectangle to the canvas.
4. circle: to draw a new circle to the canvas.
5. delete: press the delete key to delete the selected object from the canvas.

# Future scope of Development
1. Add zooming functionality.
2. Allow the user to draw more kinds of objects, and also allow image imports.
3. Transform it into a mutli-user whiteboard to sketch out ideas with your friends/team, etc.
