import cgi
import cgitb

cgitb.enable()

# Secure data we know about
securedata = __import__('securevars')
headers = {'Content-Type': 'text/plain'}
output = ''


def main():
    global output, headers
    output += securedata.SECURE_MESSAGE + '\n'
    print_headers()
    print_content()


def print_headers():
    for k, v in headers:
        print('{}: {}'.format(k, v))
    print()


def print_content():
    print(output, end='')

if __name__ == '__main__':
    main()
