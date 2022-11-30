import requests
import json

import pytest

from documents.models import Document

id = ["ABC123DEF", "DF987SK"]
type = ["Identity Card", "Driver License"]
country = ["Italy", "Italy"]
issue = ["1998-05-03", "1996-08-12"]
expiry = ["2028-05-03", "2026-08-12"]
authority = ["Comune di Tortora", "Comune di Rende"]


def test_add_a_new_document(db):
    data = {
        "id_number" : "ABC123DEF",
        "type" : "Identity Card",
        "country_of_issue" : "Italy",
        "date_of_issue" : "05/03/1998",
        "date_of_expiration" : "05/03/2028",
        "authority_issuing_the_document" : "Comune di Tortora"
            }
    #print(json.dumps(data))
    response = requests.post("http://127.0.0.1:8000/api/documents/add-document-id",json=json.dumps(data))
    #json_response = response.json()
    #print(json_response)
    print(Document.objects.all())
    assert True