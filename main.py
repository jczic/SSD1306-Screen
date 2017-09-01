
from ssd1306 import SSD1306

print("---------------------")
print(" Test SSD1306 screen ")
print("---------------------")

screen = SSD1306(2, 3)
screen.DrawScreenText("JC`zic", 10, 10)
