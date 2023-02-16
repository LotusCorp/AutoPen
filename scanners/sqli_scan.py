import requests


def Scan(domain):

    param = input("[LOTUS] SQLi Parameter: ")
    with open(f'./scans/SQLI/{domain}.txt', 'w') as f:
        f.write('{:<15} {:<45} {:<15} \n'.format('Domain', 'Payload', 'SQLI'))
        f.write('='*66+'\n')

    with open("./payloads/sqli.txt", "r") as f:
        try:
            for line in f:
                payload = line.strip()
                response = requests.get(f"https://{domain}{param}{payload}")
                if response.status_code != 404:
                    with open(f"./scans/SQLI/{domain}.txt", "a") as f:
                        f.write("{:<15} {:<45} {:<15} \n".format(domain, payload, "True"))
                else:
                    pass
        except requests.exceptions.ConnectionError as e:
            pass
