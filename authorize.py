import http.client

conn = http.client.HTTPSConnection("api-sandbox.sebgroup.com")

headers = {'accept': "text/html"}

conn.request("GET", "/mga/sps/oauth/oauth20/authorize?client_id=FhQAyqDMJ2djM3fXAd1q&scope=psd2_accounts psd2_payments&redirect_uri=https://api.sebgroup.com/accounts/v1/&response_type=code", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
