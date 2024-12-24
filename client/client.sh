#!/bin/bash

API_URL="http://127.0.0.1:52039/api/recommend"

SONGS='["Mask Off"]'

response=$(curl -s -X POST $API_URL \
  -H "Content-Type: application/json" \
  -d "{\"songs\": $SONGS}")
  
echo "Resposta da API:"
echo $response