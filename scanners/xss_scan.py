import requests


def Scan(domain):
    param = input("[LOTUS] XSS Parameter: ") # ?page= for example
    with open(f"./scans/XSS/{domain}.txt", "w") as f:
        f.write('{:<15} {:<45} {:<15} \n'.format('Domain', 'Payload', 'LFI'))
        f.write('='*66+'\n')

    with open("./payloads/xss.txt", "r") as f:
        for line in f:
            payload = line.strip()
            response = requests.get(f"https://{domain}{param}{payload}")
            if payload in response.content.decode():
                with open(f"./scans/XSS/{domain}.txt", "a") as f:
                    f.write("{:<15} {:<45} {:<15} \n".format(domain, payload, "True"))
            else:
                pass
