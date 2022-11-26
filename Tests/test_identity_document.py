import pytest
from documents.models import Document

@pytest.mark.django_db
def test_insert_document_in_the_database():
    assert True