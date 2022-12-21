import json
from websocket import create_connection

f = open("C:/Users/conno/OneDrive/Documents/GitHub/CODE/Python/HomeAssistantControl/authkey.txt", "r")
authkey = f.read()

class BedsideLight():
    def turn_on(self, brightness):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_on","service_data":{"entity_id":"light.philips_ltw012_huelight_2", "brightness_pct":brightness},"id":24}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_off","service_data":{"entity_id":"light.philips_ltw012_huelight_2"},"id":24}))
        ws.close()

class MainLight():
    def turn_on(self, brightness):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_on","service_data":{"entity_id":"light.philips_lct015_huelight", "brightness_pct":brightness},"id":25}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_off","service_data":{"entity_id":"light.philips_lct015_huelight"},"id":25}))
        ws.close()

class LightStrips():
    def turn_on(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"switch","service":"turn_on","service_data":{"entity_id":"switch.connors_led_lights"},"id":25}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"switch","service":"turn_off","service_data":{"entity_id":"switch.connors_led_lights"},"id":25}))
        ws.close()
