import requests
import re

def FindUrl(url):
    res = requests.get(url)
    pattern = r'<a\S*\s*href="*\'*\S*:*/*(\S+\.\w+)"*\'*\S*\s*>'
    result = re.findall(pattern,res.text)
    result.sort()
    return result

input_url = input()

print(FindUrl(input_url))


