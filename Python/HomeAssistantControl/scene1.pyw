import controls

bsLight = controls.BedsideLight()
mnLight = controls.MainLight()
ledStrip = controls.LightStrips()

bsLight.turn_on(50)
mnLight.turn_off()
ledStrip.turn_off()