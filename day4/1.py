import urllib.parse

string = "这是一个测试"
encoded_string = urllib.parse.quote(string.encode('utf-8'))

print(encoded_string)
# Output: '%D5%C5%CA%A1%B8%B4%B2%BB%B2%BB'

decoded_string = urllib.parse.unquote(encoded_string, encoding='utf-8')

print(decoded_string)
# Output: '这是一个测试'
