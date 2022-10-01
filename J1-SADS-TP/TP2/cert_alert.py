import ssl
import socket
from cryptography import x509

from datetime import datetime
from datetime import date



domains = ["anatares.com"]

for domain in domains:
    context = ssl.create_default_context()

    # override context so that it can get expired cert
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            print("SSL/TLS version:", ssock.version())
            # get cert in DER format
            data = ssock.getpeercert(True)
            # convert cert to PEM format
            pem_data = ssl.DER_cert_to_PEM_cert(data)
            # extract cert info from PEM format
            cert_data = x509.load_pem_x509_certificate(str.encode(pem_data))
            # show cert expiry date
            print("Expiry date:", cert_data.not_valid_after)
            print("Domain "+domain+" epire in "+str((date.today() - (cert_data.not_valid_after).date()))+"days")
