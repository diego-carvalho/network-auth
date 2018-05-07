import urllib.request
import urllib.parse
import time

def send_connection(serial_magic):
    # Posting Data
    data = urllib.parse.urlencode({
        '4Tredir': 'http://www.python.org',
        'magic': serial_magic,
        'username': login,
        'password': password
        }).encode("utf-8")

    req = urllib.request.Request('https://captive.ufsj.edu.br:1003/fgtauth?' + serial_magic, data=data)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    req.add_header('Referer', 'https://captive.ufsj.edu.br:1003/fgtauth?' + serial_magic)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Connection', 'keep-alive')
    resp = urllib.request.urlopen(req).read().decode('utf8', 'ignore')


def connection():
    # Get Magic
    fp = urllib.request.urlopen("http://www.python.org")
    mybytes = fp.read()

    mystr  = mybytes.decode("utf8")
    fp.close()

    magic = ""

    if 'name=\"magic\" value=\"' in mystr:

        substring = mystr.split('name=\"magic\" value=\"')[1]
        magic = substring.split('\">')[0]
        print(magic)
        send_connection(magic)
        return False
    else:
        return True
 

# Run program
filein = open('network-config.txt', 'r')
login = filein.readline().rstrip()
password = filein.readline().rstrip()
filein.close()

serial_magic = connection()
while True:
    try:
        time.sleep( 15 * 60 )
        serial_magic = True
        while(serial_magic):
            time.sleep( 30 )
            serial_magic = connection()
    except KeyboardInterrupt:
        break

exit()

