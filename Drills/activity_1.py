# Part 1
# What does the following code do? Add a comment to each line of code
import requests
import json

base_url = "https://api.chucknorris.io/jokes"
endpoint = 'categories'
response = requests.get(f'{base_url}/{endpoint}')
print(f'status Code: {response.status_code}')
print(f'Response Body: {response.text}')

endpoint = 'random'
params = 'music'

response = requests.get(f'{base_url}/{endpoint}?category={params}')
print(f'status Code: {response.status_code}')
print(f'Response Body: {response.text}')