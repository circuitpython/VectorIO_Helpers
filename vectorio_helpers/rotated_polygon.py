# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
"""
`outlined_rectangle.py`
================================================================================

A polygon that can be rotated to arbitrary angles


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads


"""
import math

from vectorio import Polygon
from displayio import Group


class RotatedPolygon(Group):
    def __init__(self, pixel_shader, points, x, y, rotation):
        rotated_points = []
        self._original_points = points
        for point in points:
            rotated_points.append(
                (
                    int(point[0] * math.cos(math.radians(rotation)) - point[1] * math.sin(math.radians(rotation))),
                    int(point[1] * math.cos(math.radians(rotation)) + point[0] * math.sin(math.radians(rotation)))
                )
            )
        print(rotated_points)
        _poly = Polygon(pixel_shader=pixel_shader, points=rotated_points, x=x, y=y)
        super().__init__()
        self.append(_poly)
        self._rotation = rotation

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, new_rotation):
        self._rotation = new_rotation
        rotated_points = []
        for point in self._original_points:
            rotated_points.append(
                (
                    int(point[0] * math.cos(math.radians(self._rotation)) - point[1] * math.sin(math.radians(self._rotation))),
                    int(point[1] * math.cos(math.radians(self._rotation)) + point[0] * math.sin(math.radians(self._rotation)))
                )
            )
        self[0].points = rotated_points
