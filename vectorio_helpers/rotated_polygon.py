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
    def __init__(self, pixel_shader, points, x, y, rotation=0, color_index=0):
        rotated_points = []
        self._original_points = points
        for point in points:
            rotated_points.append(
                (
                    int(point[0] * math.cos(math.radians(rotation)) - point[1] * math.sin(math.radians(rotation))),
                    int(point[1] * math.cos(math.radians(rotation)) + point[0] * math.sin(math.radians(rotation)))
                )
            )
        _poly = Polygon(pixel_shader=pixel_shader, points=rotated_points, x=x, y=y, color_index=color_index)
        super().__init__()
        self.append(_poly)
        self._rotation = rotation

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, new_rotation):
        self._rotation = new_rotation % 360
        rotated_points = []
        _rotation_radians = math.radians(self._rotation)

        _cos_val = math.cos(_rotation_radians)
        _sin_val = math.sin(_rotation_radians)

        for point in self._original_points:
            rotated_points.append(
                (
                    int(point[0] * _cos_val - point[1] * _sin_val),
                    int(point[1] * _cos_val + point[0] * _sin_val)
                )
            )
        self[0].points = rotated_points
