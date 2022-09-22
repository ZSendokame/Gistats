from datetime import date

import requests

from .util import sep

class Login:
    def __init__(self, token, gist_id, filename='gistats.ini'):
        self.token = token
        self.gist_id = gist_id
        self.filename = filename

    def update(self, statistics, separator='.', until=15):
        content = sep(statistics, separator, until)

        response = requests.patch(
            url=f'https://api.github.com/gists/' + self.gist_id,
            json={
                'description': 'Updated on ' + str(date.today()),
                'files': {
                    self.filename: {'content': content}
                }
            },
            auth=('ZSendokme', self.token)
        )

        return response.status_code
