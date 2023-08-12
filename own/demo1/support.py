##!/usr/bin/python3
# Filename: support.py
import requests

url = "http://123.129.175.157:9000/msj-customer-bucket/2023-08-03/test1.txt"

response = requests.get(url)
content = response.content.decode("utf-8")

print(content)
