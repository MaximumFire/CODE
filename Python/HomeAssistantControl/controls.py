import json
from websocket import create_connection

class BedsideLight():
    def turn_on(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYWZhY2M2NGQ4OTY0ODYxYTNhNDA2YWE3MGJjZjI2ZSIsImlhdCI6MTY1ODg3MzkzNywiZXhwIjoxOTc0MjMzOTM3fQ.gHwnBiqGwc2-5KlHNTWHvTU7mluk8mC-KjVVINVtqVc"}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_on","service_data":{"entity_id":"light.connors_bedside_light"},"id":24}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYWZhY2M2NGQ4OTY0ODYxYTNhNDA2YWE3MGJjZjI2ZSIsImlhdCI6MTY1ODg3MzkzNywiZXhwIjoxOTc0MjMzOTM3fQ.gHwnBiqGwc2-5KlHNTWHvTU7mluk8mC-KjVVINVtqVc"}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_off","service_data":{"entity_id":"light.connors_bedside_light"},"id":24}))
        ws.close()

class MainLight():
    def turn_on(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYWZhY2M2NGQ4OTY0ODYxYTNhNDA2YWE3MGJjZjI2ZSIsImlhdCI6MTY1ODg3MzkzNywiZXhwIjoxOTc0MjMzOTM3fQ.gHwnBiqGwc2-5KlHNTWHvTU7mluk8mC-KjVVINVtqVc"}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_on","service_data":{"entity_id":"light.connors_main_light"},"id":25}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYWZhY2M2NGQ4OTY0ODYxYTNhNDA2YWE3MGJjZjI2ZSIsImlhdCI6MTY1ODg3MzkzNywiZXhwIjoxOTc0MjMzOTM3fQ.gHwnBiqGwc2-5KlHNTWHvTU7mluk8mC-KjVVINVtqVc"}))
        ws.send(json.dumps({"type":"call_service","domain":"light","service":"turn_off","service_data":{"entity_id":"light.connors_main_light"},"id":25}))
        ws.close()

class LightStrips():
    def turn_on(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYWZhY2M2NGQ4OTY0ODYxYTNhNDA2YWE3MGJjZjI2ZSIsImlhdCI6MTY1ODg3MzkzNywiZXhwIjoxOTc0MjMzOTM3fQ.gHwnBiqGwc2-5KlHNTWHvTU7mluk8mC-KjVVINVtqVc"}))
        ws.send(json.dumps({"type":"call_service","domain":"switch","service":"turn_on","service_data":{"entity_id":"switch.connors_led_lights"},"id":25}))
        ws.close()
    
    def turn_off(self):
        ws = create_connection("ws://192.168.1.202:8123/api/websocket")
        ws.send(json.dumps({"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYWZhY2M2NGQ4OTY0ODYxYTNhNDA2YWE3MGJjZjI2ZSIsImlhdCI6MTY1ODg3MzkzNywiZXhwIjoxOTc0MjMzOTM3fQ.gHwnBiqGwc2-5KlHNTWHvTU7mluk8mC-KjVVINVtqVc"}))
        ws.send(json.dumps({"type":"call_service","domain":"switch","service":"turn_off","service_data":{"entity_id":"switch.connors_led_lights"},"id":25}))
        ws.close()