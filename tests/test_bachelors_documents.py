import pytest

from documents.models import BachelorsDegree
from documents.views import BachelorsDegreeViewSet


def test_add_a_new_bachelors_degree_document(db):
    BachelorsDegreeViewSet.addIdentityDocument()
    BachelorsDegreeViewSet.addIdentityDocument()
    assert BachelorsDegree.objects.filter()