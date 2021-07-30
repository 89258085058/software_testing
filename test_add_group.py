# -*- coding: utf-8 -*-

from group import Group
from aplication import Aplication
import pytest


@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login( username="admin", password="secret")
    app.create_group( Group(name="12345", header="12345", footer="12345"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()



