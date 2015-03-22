import cgi
import cgitb

cgitb.enable()

headers = {'Content-Type': 'text/plain'}
output = ''


def main():
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
