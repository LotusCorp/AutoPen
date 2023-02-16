import requests
from time import sleep

def Scan(domain):

    with open(f"./scans/DIRECTORIES/{domain}.txt", "a") as f:
        f.write("{:<15} {:<15} {:<15} \n".format("Domain", "Directory", "Response Code"))
        f.write("="*45+"\n")

    with open("./wordlists/dir_list.txt", "r") as f:
        dirs = f.read().splitlines()

    for directory in dirs:
        try:
            url = f"https://{domain}/{dirs}"
            response = requests.get(url)
            if response.status_code != 404:
                with open(f"./scans/DIRECTORIES/{domain}.txt", "a") as f:
                    f.write("{:<15} {:<15} {:<15} \n".format(domain, directory, str(response.status_code)))
        except requests.exceptions.ConnectionError as e:
            continue
