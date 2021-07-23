import http.client

conn = http.client.HTTPSConnection("api-sandbox.sebgroup.com")
headers = {
    'X-Request-ID': "6MmRlJEbXci0aquKL4SiFhJdtkIz1tfN",
    'Authorization': "Bearer MC9fOSimQz2LKO8rkrUx",
    'accept': "application/json"
}

conn.request(
    "GET", "/ais/v7/identified2/accounts?withBalance=true", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
