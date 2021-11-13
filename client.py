import requests
from requests.structures import CaseInsensitiveDict

url = "http://127.0.0.1:8000/o/token/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

headers["Authorization"] = "Basic SWxVMGp3TVZjRzRlY0ZZTENYNlVublJqS0dqZG1hSmhEVlBPNWdEazpSU1NybWQzSFNlWE80YkpOMEJGUlAxSllBWGQyYU03aHRmcnU3aDhheTE4dER1RW9rUTI0dGtUNnFJc2ZSMnRrdHNaWENvOXU5RVB6d1ZjbTZ0VnFVazFZcUFPUlNrT3VnaFlJa3Vvbkpjdm1FN2IwWm15UWpaeGR0WkNDdlk0RA=="

data = "grant_type=password&username=danilo&password=Danilo*1997"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

