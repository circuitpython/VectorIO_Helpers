# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
"""
Draw a circle pattern of rotated polygons in rainbow colors
"""
import math
import board
import displayio
import rainbowio
from vectorio_helpers import rotated_polygon

display = board.DISPLAY

# Change these variables to see different patterns
count = 18
circle_r = 54
polygon_points = [(-30, 0), (50, 0), (0, 20)]

# Make the display context
main_group = displayio.Group()
board.DISPLAY.show(main_group)

# create a rainbowy palette from given size
def make_rainbow_palette(size):
    colors = displayio.Palette(size)
    for i in range(size):
        colors[i] = rainbowio.colorwheel(i * (255//size))
    return colors


rainbow = make_rainbow_palette(count)

for i in range(count):
    angle = i * (360//count)
    #print(angle)

    # find point along a circle
    _x = int(circle_r * math.cos(math.radians(angle)) + display.width//2)
    _y = int(circle_r * math.sin(math.radians(angle)) + display.height//2)

    # make a rotated polygon
    cur_poly = rotated_polygon.RotatedPolygon(pixel_shader=rainbow, points=polygon_points, x=_x, y=_y, rotation=angle, color_index=i)

    # show it on the display
    main_group.append(cur_poly)

while True:
    pass