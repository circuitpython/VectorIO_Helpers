# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
"""
`line.py`
================================================================================

A line drawn between two points with a specified thickness


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads


"""
import math
import displayio
import vectorio


class Line(displayio.Group):
    """
    A line between two points with specified stroke size.

    :param Union[tuple, list] points: Two points to draw the line between.

    """

    def __init__(self, points, palette, stroke=1):
        super().__init__()
        _x1, _y1 = points[0]
        _x2, _y2 = points[1]
        if (_x2 - _x1) == 0:
            xdiff1 = round(stroke / 2)
            xdiff2 = -round(stroke - xdiff1)
            ydiff1 = 0
            ydiff2 = 0

        elif (_y2 - _y1) == 0:
            xdiff1 = 0
            xdiff2 = 0
            ydiff1 = round(stroke / 2)
            ydiff2 = -round(stroke - ydiff1)

        else:
            _c = math.sqrt((_x2 - _x1) ** 2 + (_y2 - _y1) ** 2)

            xdiff = stroke * (_y2 - _y1) / _c
            xdiff1 = round(xdiff / 2)
            xdiff2 = -round(xdiff - xdiff1)

            ydiff = stroke * (_x2 - _x1) / _c
            ydiff1 = round(ydiff / 2)
            ydiff2 = -round(ydiff - ydiff1)

        _line_polygon = vectorio.Polygon(
            points=[
                (_x1 + xdiff1, _y1 + ydiff2),
                (_x1 + xdiff2, _y1 + ydiff1),
                (_x2 + xdiff2, _y2 + ydiff1),
                (_x2 + xdiff1, _y2 + ydiff2),
            ],
            pixel_shader=palette,
        )
        self.append(_line_polygon)
