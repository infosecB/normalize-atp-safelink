from argparse import ArgumentParser
import urllib


def normalize_atpsafelink(safelink_url):
    safelink_url = safelink_url.split("=")[1]
    safelink_url = urllib.unquote(safelink_url).decode('utf8')
    safelink_url = safelink_url.replace('&data', '')
    return safelink_url


def main(url):
    print normalize_atpsafelink(url)


if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument('-u', '--url', help="Enter the URL.", dest='url')
    args = args.parse_args()
    
    main(args.url)
