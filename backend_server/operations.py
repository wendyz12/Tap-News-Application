import json
import os
import sys

from bson.json_util import dumps

# import utils dir.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client  # pylint: disable=import-error, wrong-import-position


def add(num1, num2):
    """ Test method. """
    return num1 + num2

def get_one_news():
    """ Test method to get one news. """
    res = mongodb_client.get_db()['news'].find_one()
    return json.loads(dumps(res))
