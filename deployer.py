import cgi
import cgitb

cgitb.enable()

# Secure data we know about
securedata = __import__('securevars')
headers = {'Content-Type': 'text/plain'}
output = ''


def main():
    println(securedata.SECURE_MESSAGE)
    print_headers()
    print_content()


def add_header(k, v):
    global headers
    headers[k] = v


def println(*args, sep=' ', end='\n'):
    global output
    output += sep.join(args) + end

def print_headers():
    for k, v in headers:
        print('{}: {}'.format(k, v))
    print()


def print_content():
    print(output, end='')

if __name__ == '__main__':
    main()
