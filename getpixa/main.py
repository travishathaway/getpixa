import requests
import sys
import configparser
import os
import json


PIXA_SEARCH_URL = 'https://pixabay.com/api/'


def get_pixa_config():
    """
    Search for a pixa config file. Returns information from the file or
    None if nothing returned.

    :return: Dictionary or None
    """
    config = configparser.ConfigParser()

    if os.path.isfile('pixa.conf'):
        config.read('pixa.conf')
    elif os.path.isfile('~/.pixa_conf'):
        config.read('~/.pixa_conf')
    else:
        return None

    return config


def getpixa(search_query, api_key=None, page=1, per_page=20):
    """
    Returns a result search provided a search_query string. You may optionally
    provide an api key.

    :param search_query: String
    :param api_key: String

    :return: Dictionary
    """
    results = {}

    if api_key is None:
        config = get_pixa_config()
        error_msg = None

        if config is not None:
            try:
                api_key = config['pixa_api']['api_key']
            except KeyError:
                error_msg = 'Improper configuration. Please define "api_key" in section "pixa_api"'
        else:
            error_msg = "No config detected and no api key passed as argument"

        if error_msg is not None:
            sys.stderr.write('{}\n'.format(error_msg))
            sys.exit(1)

    params = {
        'key': api_key,
        'q': search_query,
        'page': page,
        'per_page': per_page
    }

    resp = requests.get(PIXA_SEARCH_URL, params=params)

    if resp.status_code != 200:
        sys.stdout.write(resp.text)
        sys.exit(1)

    data = json.loads(resp.text)

    if data.get('total', 0) > 0:
        results['total'] = data.get('total')
        results['results'] = []
        for row in data['hits']:
            results['results'].append(row.get('webformatURL'))

    return results

