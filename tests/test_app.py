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
    response = client.simulate_get('/birds')
    result_doc = json.loads(response.content)
    assert result_doc == doc
    assert response.status == falcon.HTTP_OK