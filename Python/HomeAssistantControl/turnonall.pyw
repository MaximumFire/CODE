import controls

bsLight = controls.BedsideLight()
mnLight = controls.MainLight()
ledStrip = controls.LightStrips()

bsLight.turn_on(100)
mnLight.turn_on(100)
ledStrip.turn_off()