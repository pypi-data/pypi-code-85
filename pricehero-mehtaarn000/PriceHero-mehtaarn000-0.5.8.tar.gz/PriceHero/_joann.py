from requests import get
from selectorlib import Extractor


def _joann(joann_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: 'div.pdp-main__section h1.pdp__name'
        xpath: null
        type: Text
    price:
        css: 'div.pdp-main__section span.price__item.price__sales span.value'
        xpath: null
        type: Text
    originalprice:
        css: 'div.pdp-main__section span.price__item.price__original span.value'
        xpath: null
        type: Text
    """)
    headers = {
        'authority': 'www.joann.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

    website = get(joann_url, headers=headers)
    productdata = extractor.extract(website.text)
    return productdata
