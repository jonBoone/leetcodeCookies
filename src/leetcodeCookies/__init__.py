"""Retrieve leetcode cookies from browsers with local keyring"""

import browser_cookie3
import requests
import sys
import urllib.parse
import warnings

VERSION="0.2.0"

supported_browsers = [
    "chrome",
    "chromium",
    "brave",
    "edge", 
    "firefox",
    "safari"
]


def get_cookie_jar_from_browser(browser: str, domain_name:str):
    """
    Create cookie jar from browser filtered on domain_name
    """
    cookie_jar = None
    
    match browser:
        case "chrome":
            cookie_jar = browser_cookie3.chrome(domain_name)
        case "chromium":
            cookie_jar = browser_cookie3.chromium(domain_name)
        case "brave":
            cookie_jar = browser_cookie3.brave(domain_name)
        case "firefox":
            cookie_jar = browser_cookie3.firefox(domain_name)
        case "edge":
            cookie_jar = browser_cookie3.edge(domain_name)
        case "safari":
            cookie_jar = browser_cookie3.safari(domain_name)
        case _:
            error(f'Unsupported browser {browser} requested.')

    return cookie_jar


def get_cookie_jar(domain_name:str):
    """
    Iterate through supported browsers to locate cookies for domain_name
    """
    cookie_jar = None
    
    for browser in supported_browsers:
        print(f'Trying to extract cookie for {domain_name} from {browser}')
        try:
            cookie_jar = get_cookie_jar_from_browser(browser, domain)
            break
        except Exception as e:
            warnings.warn(f'{e}: extracting cookie from {browser} failed')

    print(f'Obtained cookie_jar {cookie_jar} for {domain_name} from {browser}')

    return cookie_jar
    

def main(url="https://leetcode.com"):
    """
    Print cookies.
    """

    url_components = urllib.parse.urlsplit(url)

    print(f'From {url} we have:\n scheme = {url_components.scheme}\n \
    netloc = {url_components.netloc}\n hostname = {url_components.hostname}\n \
    port = {url_components.port}\n path = {url_components.path}\n \
    query = {url_components.query}\n')
    
    cookie_jar = get_cookie_jar(url_components.hostname)

    if cookie_jar is not None:
        r = requests.get(url, cookies=cookie_jar)

    leetcode_cookies = list(
        filter(lambda c: c.name in ("LEETCODE_SESSION", "csrftoken"), cookie_jar)
    )

    if len(leetcode_cookies) < 2:
        print(
            "get cookie failed, make sure you have Chrome, Chromium, Brave, Firefox, Edge or Safari installed and login in LeetCode with one of them at least once."
        )
        return

    for c in leetcode_cookies:
        print(c.name, c.value)

        
if __name__ == "__main__":
    main(sys.args[1])
