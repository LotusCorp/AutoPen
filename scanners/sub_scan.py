import requests
from time import sleep

def Scan(domain):

    with open(f"./scans/SUBDOMAINS/{domain}.txt", "a") as f:
        f.write("{:<15} {:<15} {:<15} \n".format("Domain", "Subdomain", "Response Code"))
        f.write("="*45+"\n")

    with open("./wordlists/sub_list.txt", "r") as f:
        subdomains = f.read().splitlines()

    for subdomain in subdomains:
        try:
            url = f"https://{subdomain}.{domain}"
            response = requests.get(url)
            if response.status_code != 404:
                with open(f"./scans/SUBDOMAINS/{domain}.txt", "a") as f:
                    f.write("{:<15} {:<15} {:<15} \n".format(domain, subdomain, str(response.status_code)))
        except requests.exceptions.ConnectionError as e:
            continue