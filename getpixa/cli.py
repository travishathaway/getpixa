"""
Usage:
    getpixa <search_query> [options]

Options:
    -p PAGE      The page to print if paginated result set
    -r PER_PAGE  The number of rows to return per page
"""
from docopt import docopt
from getpixa.main import getpixa
import sys


def main():
    args = docopt(__doc__, version=' 0.1')

    search_query = args.get('<search_query>')
    page = args.get('-p', 1)
    per_page = args.get('-r', 20)

    results = getpixa(search_query, page=page, per_page=per_page)

    sys.stdout.write('{}\n'.format(results.get('total')))

    for row in results.get('results', []):
        sys.stdout.write('{}\n'.format(row))
