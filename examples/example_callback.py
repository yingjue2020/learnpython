# -*- coding: utf-8 -*-

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from examples import send_request

def cb_build_request(sequence:int, track_id:int):
  headers = {
    "Content-Type": "application/json"
  }
  body = {
    "sequence": sequence,
    "track_id": track_id
  }
  return headers, body

if __name__ == "__main__":
  send_request(os.path.basename(__file__), cb_build_request)