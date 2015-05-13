import requests

r = requests.post('http://127.0.0.1:8080/upload', files={
    'img': open('test.png', 'rb')
})
print r.text
