import json
import falcon


class Birds(object):
    BIRD_ARRAY = []
    ID_COUNTER = 1

    @classmethod
    def on_get(cls, req, resp):
        """Handles GET requests"""
        # Create Response
        doc = {
            'birds': cls.BIRD_ARRAY
        }
        # Make Response Object
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    @classmethod
    def on_post(cls, req, resp):
        """Handles POST requests"""
        try:
            # Read Body Of Request
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)
        try:
            # Load Data To Json
            result_json = json.loads(raw_json)
            # Give Each Object created an ID
            result_json["id"] = cls.ID_COUNTER
            # Append Object to Array
            cls.BIRD_ARRAY.append(result_json)
            # Create a response
            doc = {
                "status": "created",
                "id": cls.ID_COUNTER
            }
            # Increment ID counter
            cls.ID_COUNTER = cls.ID_COUNTER + 1
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect.')
        # Make Response Object
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(doc)
