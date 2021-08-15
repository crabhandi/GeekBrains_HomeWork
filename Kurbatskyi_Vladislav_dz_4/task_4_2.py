from requests import get, utils
import xml.dom.minidom

url = get('http://www.cbr.ru/scripts/XML_daily.asp')
head = utils.get_encoding_from_headers(url.headers)
content = url.content.decode(encoding=head)

dom = xml.dom.minidom.parseString(content)
root = dom.getElementsByTagName('ValCurs')[0]
date = f'Курс на {root.getAttribute("Date")} '
cur = dom.getElementsByTagName('Value')


def currency_rates():
    name = input()
    for rate in cur:
        char = rate.getElementsByTagName('CharCode')
        value = rate.getElementsByTagName('Value')
        result = {char.firstChild.data: value.firstChild.data}
        i = result.get(name)
        if i is not None:
            print(date, ':', i)


if __name__ == '__main__':
    currency_rates()
