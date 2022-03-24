
import time
import board
import displayio
from vectorio_helpers import rotated_polygon

display = board.DISPLAY

# Make the display context
main_group = displayio.Group()
board.DISPLAY.show(main_group)

colors = displayio.Palette(3)
colors[0] = 0x002299
colors[1] = 0x22aa00
colors[2] = 0xaa0022

test_poly = rotated_polygon.RotatedPolygon(pixel_shader=colors, points=[(-80,-40), (80, -40), (0, 40)], x=120, y=120, rotation=0)

main_group.append(test_poly)

while True:
    print(test_poly.rotation)
    test_poly.rotation += 1
    time.sleep(0.01)
