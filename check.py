#! /usr/bin/env python3
#
# http://docs.python-requests.org/en/latest/user/quickstart/#redirection-and-history
#
import requests

class Site:
    def __init__(self, name, start, end, strings=None):
        self.name = name
        self.start = start
        self.end = end
        if strings is None:
            strings = []
        self.strings = strings

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
}

sites = [
        Site("frp.no", "http://frp.no", "https://www.frp.no/", 
            ["Karl Johans Gate 25", "Streng og ansvarlig innvandringspolitikk"]),
        Site("hoyre.no", "http://hoyre.no", "https://hoyre.no/", 
            ["Stortingsgaten 20", "Å bygge et land."]), 
            # Høyre bruker ikke høyre.no?
        Site("rødt.no", "http://rødt.no", "https://xn--rdt-0na.no/", 
            ["Rødt - Fordi fellesskap fungerer"]),
            # Rødt bruker ikke rodt.no?
        Site("skalfeile.no", "http://vg.no", "https://microsoft.no", 
            ["Alle i NUUG elsker Microsoft"])
        ]

def check_site(site):
    headers = { 'User-Agent': 
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like ' + 
        'Gecko) Chrome/60.0.3112.78 Safari/537.36',
            }
    r = requests.get(site.start, headers=headers)
    result = []
    try:
        r = requests.get(site.start, headers=headers)

        if r.url != site.end:
            result.append(
                "\tExpected {} to redirect to {}, did not happen".format(
                    site.start, site.end)

            )
            result.append("\tWas redirected to {}, status code {}".format(r.url, r.status_code))

        for string in site.strings:
            if string not in r.text:
                result.append("\tDid not find expected string '{}'".format(string))

    except ConnectionError as e:
        print(e.msg)

    if len(result):
        print("Errors when checking {}:".format(site.name))
        print("\n".join(result))
        return False
    return True

for site in sites:
    check_site(site)
