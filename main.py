import os
import sys
import argparse
import threading

import scanners.dns_scan
import scanners.port_scan
import scanners.sub_scan
import scanners.dir_scan
import scanners.cert_dig
import scanners.head_scan
import scanners.whois_scan
import scanners.lfi_scan
import scanners.slqli_scan
import scanners.tech_detect

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', 
    '--domain',
    help='Specify the target domain'
)
args = parser.parse_args()

class Variables:

    global __creators__, __version__, __github__

    __creators__ = 'LotusCorp'
    __version__  = '1.0.1'
    __github__   = 'github.com/LotusCorp'

class Modules:

    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def detect():
        if os.name == 'nt':
            return 'Windows'
        else:
            return 'Linux'

    def banner():

        __system__ = Modules.detect()

        print(f'''
                .?B5^ 
               !B@@@&J.  
             :5@@@@@@@B~ 
            ^B@@@@@@@@@&7  
  7J7~:    .5@@@@@@@@@@@B^    .^7??.
  P@@@&GY!.  ^JB@@@@@#5~  .~JG#@@@#:
  Y@@@@@@@#5~   !G@#?:  ^JB@@@@@@@B.
  !@@@@@@@@@@G7.  ~:  ~P&@@@@@@@@@Y                 Developers..: {__creators__}
  .G@@@@@@@@@@@B!   ~P@@@@@@@@@@@&^                 Version.....: {__version__}
   !&@@@@@@@@@@@@P~Y&@@@@@@@@@@@@J                  Github......: {__github__}
    7&@@@@@@@@@@@@@@@@@@@@@@@@@@J                   System......: {__system__}
     ~B@@@@@@@@@@@@@@@@@@@@@@@#7 
      .?B@@@@@@@@@@@@@@@@@@@#J: 
        .~JG#@@@@@@@@@@@&BY!. 
        ''')

class Main():

    def main(domain):
        Modules.clear()
        Modules.banner()

        try:
            scanners.head_scan.WebService(domain)
            scanners.tech_detect.Detect(domain)

            print('\n[LOTUS] Dumping DNS Records')
            scanners.dns_scan.Dump(domain)

            print('[LOTUS] Dumping Digital Certificates')
            # scanners.cert_dig.Dump(domain)

            print('[LOTUS] Dumping Domain Headers')
            scanners.head_scan.Dump(domain)

            print('[LOTUS] Dumping Domain Information')
            scanners.whois_scan.Dump(domain)

            print('[LOTUS] Scanning for Open Ports and their Services')
            scanners.port_scan.Scan(domain)

            print('[LOTUS] Bruteforcing Subdomains')
            print('[LOTUS] Scanning for Subdomain Takeover')
            scanners.sub_scan.Scan(domain)

            print('[LOTUS] Bruteforcing Directories')
            scanners.dir_scan.Scan(domain)

            print('[LOTUS] Scanning for LFI')
            scanners.lfi_scan.Scan(domain)

            print("[LOTUS] Scanning for SQLi")
            scanners.slqli_scan.Scan(domain)

        except KeyboardInterrupt:
            print("\n[LOTUS] Exiting...")
            sys.exit()

        if os.name == 'nt':
            os.system('explorer .\scans')
        else:
            pass
        
if __name__ == '__main__':
    if args.domain:
        Main.main(args.domain)
    else:
        Modules.clear()
        Modules.banner()
        print('Syntax:  python main.py <domain>')
        print('Example: python main.py domain.com')
