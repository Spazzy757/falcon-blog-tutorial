import json
import falcon


class Birds(object):

    @classmethod
    def on_get(cls, req, resp):
        doc = {
            'birds': [
                {
                    'species': 'falcons',
                    'status': 'endangered'
                },
                {
                    'species': 'hawks',
                    'status': 'okay'
                }
            ]
        }

        resp.body = json.dumps(doc, ensure_ascii=False)
        print(str(req))
        resp.status = falcon.HTTP_200
