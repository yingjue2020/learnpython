# -*- coding: utf-8 -*-

def send_request(device_filename:str, cb_build_request:callable):
  sequence = 100
  track_id = 10
  headers, body = cb_build_request(sequence, track_id)
  print(f"device filename: {device_filename}")
  print(f"headers: {headers}")
  print(f"body: {body}")