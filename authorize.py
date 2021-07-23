import requests
# , "PSU-Corporate-Id": "9311219639"
headers = {"accept": "text/html"}
seb = requests.get("https://api-sandbox.sebgroup.com/mga/sps/oauth/oauth20/authorize?client_id=MHuQ6MLqCH2Oj3ipZqCq&scope=psd2_accounts psd2_payments&redirect_uri=https://example.com&response_type=code", headers=headers,)

print(seb.status_code)

if seb.history:
    print("Request was redirected")
    for resp in seb.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(seb.status_code, seb.url)
