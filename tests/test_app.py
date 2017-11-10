import falcon
import json
import pytest
from birds.app import api
from falcon import testing


@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_birds(client):
    response_object = {"birds": []}
    response = client.simulate_get('/birds')
    result_doc = json.loads(response.content)
    assert result_doc == response_object
    assert response.status == falcon.HTTP_OK


def test_create_birds(client):
    response_object = {
        "id": 1,
        "status": "created"
    }
    request_object = {
        'species': "Falcon"
    }
    response = client.simulate_request(method='POST', path='/birds',
                                       body=json.dumps(request_object))
    result_doc = json.loads(response.content)
    assert result_doc == response_object
    assert response.status == falcon.HTTP_202
