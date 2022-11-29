import pytest
from documents.views import DocumentViewSet
from documents.models import Document

id = ["ABC123DEF", "DF987SK"]
type = ["Identity Card", "Driver License"]
country = ["Italy", "Italy"]
issue = ["1998-05-03", "1996-08-12"]
expiry = ["2028-05-03", "2026-08-12"]
authority = ["Comune di Tortora", "Comune di Rende"]

def test_add_a_new_document(db):
    DocumentViewSet.addIdentityDocument(id[0],type[0],country[0],issue[0],expiry[0], authority[0])
    DocumentViewSet.addIdentityDocument(id[1], type[1], country[1], issue[1], expiry[1], authority[1])
    assert Document.objects.filter(id_number=id[1])

def test_get_document_by_id_number(db):
    DocumentViewSet.addIdentityDocument(id[0], type[0], country[0], issue[0], expiry[0], authority[0])
    DocumentViewSet.addIdentityDocument(id[1], type[1], country[1], issue[1], expiry[1], authority[1])
    res = DocumentViewSet.getDocumentById(id[0])
    assert res.id_number == id[0]