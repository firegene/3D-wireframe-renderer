import dataclasses
from math import pi

import pygame
import pygame_gui
from projection import xprojected, yprojected
from rotation import rotX, rotY, rotZ
from shapes import shapes

width = 700
height = 700
w = width / 2
h = height / 2
focal = 600
angle = 2.5
theta = angle * pi / 180

show_vertices = False
do_rotX = False
do_rotY = False
do_rotZ = False

to_draw = "cube"

shape = shapes[to_draw]  # type: ignore

pygame.init()
pygame.display.set_caption("3D Wireframe Renderer")
screen = pygame.display.set_mode((width, height))
manager = pygame_gui.UIManager((width, height))
clock = pygame.time.Clock()


vertices_toggle = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((3, 3), (90, 25)), text="vertices", manager=manager
)
xtoggle = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((3, height - 78), (70, 25)), text="rot x", manager=manager
)
ytoggle = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((3, height - 53), (70, 25)), text="rot y", manager=manager
)
ztoggle = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((3, height - 28), (70, 25)), text="rot z", manager=manager
)

while True:
    time_delta = clock.tick(60) / 1000.0

    if show_vertices:
        for p in shape.vertex.values():
            pygame.draw.circle(
                screen,
                (0, 0, 0),
                (xprojected(p, focal) + w, yprojected(p, focal) + h),
                3,
            )

    for e in shape.edge:
        start = (
            xprojected(shape.vertex[e[0]], focal) + w,
            yprojected(shape.vertex[e[0]], focal) + h,
        )
        end = (
            xprojected(shape.vertex[e[1]], focal) + w,
            yprojected(shape.vertex[e[1]], focal) + h,
        )
        pygame.draw.aaline(screen, (0, 0, 0), start, end)

    if do_rotX:
        for key, xyz in shape.vertex.items():
            shape.vertex[key] = rotX(xyz, theta)
    if do_rotY:
        for key, xyz in shape.vertex.items():
            shape.vertex[key] = rotY(xyz, theta)
    if do_rotZ:
        for key, xyz in shape.vertex.items():
            shape.vertex[key] = rotZ(xyz, theta)

    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == xtoggle:
                do_rotX = not do_rotX
            if event.ui_element == ytoggle:
                do_rotY = not do_rotY
            if event.ui_element == ztoggle:
                do_rotZ = not do_rotZ
            if event.ui_element == vertices_toggle:
                show_vertices = not show_vertices
        manager.process_events(event)

    manager.update(time_delta)
    screen.fill((255, 255, 255))
    manager.draw_ui(screen)
