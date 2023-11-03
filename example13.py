"""Script to get list of FTP servers from Shodan.io"""

from ftplib import FTP, Error as FTPError
from multiprocessing import Pool
from threading import Lock
from shodan import Shodan, APIError

# Shodan API key (https://account.shodan.io/)
SHODAN_API_KEY = '<INSERT_YOUR_API_KEY>'

output_lock = Lock()

def list_ftp_files(server):
    """List FTP server root directory"""
    ftp = FTP(server)
    try:
        ftp.login()
        conts = ftp.nlst()
        ftp.quit()

        with output_lock:
            print(f"Root directory listing in server {server}:")
            if len(conts) == 0:
                print("<empty>")
            else:
                for cont in conts:
                    print(cont)
    except FTPError as ftp_e:
        print(f"Failed to list root directory in server {server}: {ftp_e}")

if __name__ == '__main__':
    servers = []

    if SHODAN_API_KEY == '<INSERT_YOUR_API_KEY>':
        print('Using demo data')
        servers = ['47.89.16.40', '192.134.134.6', '24.52.30.187', '194.78.237.234',
                '109.196.254.1', '177.69.254.51', '133.18.128.248', '80.232.190.69',
                '128.171.90.95', '103.51.112.153', '176.97.143.174', '155.37.255.46',
                '94.152.35.172', '94.152.35.248', '138.99.200.36', '128.171.90.152',
                '185.237.18.28', '208.72.23.64', '93.63.78.1', '66.207.3.31']
    else:
        api = Shodan(SHODAN_API_KEY)

        try:
            results = api.search('"230 login successful" port:"21"', limit=20)
            for result in results['matches']:
                #hostname = result['ip_str']
                #if 'hostnames' in result and len(result['hostnames']) > 0:
                #    hostname = result['hostnames'][0]
                servers.append(result['ip_str'])
        except APIError as e:
            print(f"Error: {e}")

    with Pool(4) as p:
        p.map(list_ftp_files, servers)
