from lib.constants import *
import os.path
import requests


def download(year, day, path):
    with open(SESSION_FILE, 'r') as file:
        session = file.read().strip()
    cookies = {'session': session}

    headers = requests.utils.default_headers()
    headers.update(HTTP_HEADER)

    r = requests.get(DATA_URL.format(year, day), cookies=cookies)
    with open(path, 'wb') as file:
        file.write(r.content)


def load(year, day, split_lines=False, test=None):
    if test:
        data = {'test': True, 'raw': test}
    else:
        filepath = DATA_PATH.format(year, day)
        if not os.path.isfile(filepath):
            download(year, day, filepath)
        data = {'test': False, 'raw': open(filepath, 'r').read()}

    if split_lines:
        data['split'] = data['raw'].split('\n')[:-1]

    return data
