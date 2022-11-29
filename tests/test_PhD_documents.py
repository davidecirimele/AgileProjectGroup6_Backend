import pytest

from documents.models import Doctorate
from documents.views import DoctorateViewSet


def test_add_a_new_PhD_document(db):
    DoctorateViewSet.addIdentityDocument()
    DoctorateViewSet.addIdentityDocument()
    assert Doctorate.objects.filter()