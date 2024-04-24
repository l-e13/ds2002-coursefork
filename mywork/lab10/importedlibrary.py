#!/usr/bin/env python3

import json

# valid JSON data
data = '{"valid_json_key": "value"}'

try:
  # Attempt to load the JSON data
  parse = json.loads(data)
  print(parse)
except json.JSONDecodeError as e:
  # Print the JSON import error
  print(f"JSON import error: {e}")

