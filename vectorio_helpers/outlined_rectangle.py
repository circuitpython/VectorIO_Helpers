# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
"""
`outlined_rectangle.py`
================================================================================

A rectangle with optional border line.


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
from vectorio_helpers.line import Line


class OutlinedRectangle(displayio.Group):
    """
    A rectangle with optional border line.

    """

    def __init__(
        self,
        pixel_shader,
        width,
        height,
        x,
        y,
        outline_color_index=None,
        outline_thickness=1,
    ):
        _rectangle = vectorio.Rectangle(
            pixel_shader=pixel_shader,
            width=width,
            height=height,
            x=0,
            y=0,
            color_index=2,
        )
        super().__init__(x=x, y=y, scale=1)
        self.append(_rectangle)

        if outline_color_index is not None:
            _left_border = Line(
                ((0, 0), (0, height)), pixel_shader, stroke=outline_thickness
            )
            _left_border.x = 0
            _left_border.y = 0
            self.append(_left_border)

            _top_border = Line(
                ((0, 0), (width + outline_thickness, 0)),
                pixel_shader,
                stroke=outline_thickness,
            )
            _top_border.x = 0 - outline_thickness // 2
            _top_border.y = 0
            self.append(_top_border)

            _right_border = Line(
                ((width, 0), (width, height)), pixel_shader, stroke=outline_thickness
            )
            _right_border.x = 0
            _right_border.y = 0
            self.append(_right_border)

            _bottom_border = Line(
                ((0, height), (width + outline_thickness, height)),
                pixel_shader,
                stroke=outline_thickness,
            )
            _bottom_border.x = 0 - outline_thickness // 2
            _bottom_border.y = 0
            self.append(_bottom_border)
