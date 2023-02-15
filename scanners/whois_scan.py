import whois


def Dump(domain):

    whois_info = whois.whois(domain)
    with open(f'./scans/WHOIS/{domain}', 'w') as f:
        f.write(str(whois_info))
