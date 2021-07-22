import http.client

conn = http.client.HTTPSConnection("api-sandbox.sebgroup.com")

payload = "client_id=MHuQ6MLqCH2Oj3ipZqCq&client_secret=OA6qvVUYN6qTwkIjmdyl&code=................................&redirect_uri=https://example.com&grant_type=authorization_code"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
}

conn.request("POST", "/mga/sps/oauth/oauth20/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
