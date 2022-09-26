from bs4 import BeautifulSoup as bs
import sys

def replace_figure_with_script(soup, figure):
    href = figure.find_all('a')[0]['href']
    scriptTag = soup.new_tag('script', src='%s%s' % (href, '.js'))
    figure.replace_with(scriptTag)

def scrape(input, output):
    with open(input, 'r') as fin:
        soup = bs(fin, 'html.parser')

    soup_out = soup.find_all('div', {'class': 'page-body'})[0]

    figures = soup.find_all('figure')
    for figure in figures:
        replace_figure_with_script(soup, figure)

    with open(output, 'wb') as fout:
        fout.write(soup_out.prettify('utf-8'))

if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    scrape(input, output)