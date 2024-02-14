import controls as c

m = c.MainLight()
d = c.DeskLight()
s = c.StripLights()

m.turn_off()
d.turn_off()
s.turn_on(100, 215, 151, 255)