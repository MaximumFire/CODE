import json
from websocket import create_connection
from time import sleep as s

f = open("C:/Users/conno/OneDrive/Documents/GitHub/CODE/Python/HomeAssistantControl/authkey.txt", "r")
authkey = f.read()

transition_time = 0.5

class MainLight():
    def turn_on(self, brightness):
        ws = create_connection("ws://192.168.1.210:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_on","service_data":{"entity_id":"light.connors_main_light", "brightness_pct":brightness, "transition": transition_time}, "id": 5}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.210:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_off","service_data":{"entity_id":"light.connors_main_light"}, "id": 5}))
        ws.close()

class DeskLight():
    def turn_on(self, brightness):
        ws = create_connection("ws://192.168.1.210:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_on","service_data":{"entity_id":"light.connors_desk_light", "brightness_pct":brightness, "transition": transition_time}, "id": 5}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.210:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_off","service_data":{"entity_id":"light.connors_desk_light"}, "id": 5}))
        ws.close()

class StripLights():
    def turn_on(self, brightness, r, g, b):
        ws = create_connection("ws://192.168.1.210:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_on","service_data":{"entity_id":"light.connor_s_led_controller_light", "brightness_pct":brightness, "transition": transition_time, "rgb_color": [r, g, b]}, "id": 5}))
        ws.close()

    def turn_off(self):
        ws = create_connection("ws://192.168.1.210:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": authkey}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_off","service_data":{"entity_id":"light.connor_s_led_controller_light"}, "id": 5}))
        ws.close()    

if __name__ == "__main__":
    l = StripLights()
    l.turn_on(100, 215, 151, 255)
    s(2)
    l.turn_off()
