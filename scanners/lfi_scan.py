import requests


def Scan(domain):

    f.write('{:<15} {:<15} {:<30} \n'.format('Domain', 'Payload', 'LFI'))
        f.write('='*66+'\n')

    with open("./payloads/lfi.txt", "r") as f:
        for line in f:
            payload = line.strip()
            url = target_url + payload
            response = requests.get(url)
            if response.status_code != 404:
                with open(f"./scans/LFI/{domain}.txt", "a") as f:
                    f.write("{:<15} {:<15} {:<30} \n".format(domain, payload, "True"))
            else:
                pass
