import pytest

from documents.models import MastersDegree
from documents.views import MastersDegreeViewSet


def test_add_a_new_masters_degree_document(db):
    MastersDegreeViewSet.addIdentityDocument()
    MastersDegreeViewSet.addIdentityDocument()
    assert MastersDegree.objects.filter()