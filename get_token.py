import http.client

conn = http.client.HTTPSConnection("api-sandbox.sebgroup.com")

payload = "client_id=FhQAyqDMJ2djM3fXAd1q&client_secret=7AHTfwmDjSD9FBSwolzG&code=.............&redirect_uri=https://oauth.pstmn.io/v1/browser-callback&grant_type=refresh_token"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
}

conn.request("POST", "/mga/sps/oauth/oauth20/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
