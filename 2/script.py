import http.client
import json

conn = http.client.HTTPConnection("localhost", 8081)
payload = json.dumps({
  "ime": "Andrej",
  "prezime": "Arsic",
  "username": "aarsic",
  "predmeti": [
    {
      "ime": "OIT",
      "espb": 6
    },
    {
      "ime": "RISO",
      "espb": 6
    }
  ],
  "smer": "IT"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))