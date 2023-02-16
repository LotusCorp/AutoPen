import ssl
import socket

def Dump(domain):

    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as sslsock:
            cert = sslsock.getpeercert(True)

    with open(f'./scans/CERTIFICATES/{domain}.txt', 'w') as f:
        f.write(str(cert))
