from http import client
import pytest
from library.clients.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, last_name",
    [
        ("Pedro", "Picapiedra"),
        ("Juan", "Perez"),
        ("Benito", "Juarez"),
        ("Jaime", "Kiroz")
    ]
)
def test_nom_clients(name,last_name):
    client = Client.objects.create(name=name, last_name=last_name)
    print(client)
    assert len(client.name) < 128
    assert len(client.last_name) < 128

@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, last_name",
    [
        ("Pedro", "Picapiedra"),
        ("Juan", "Perez"),
        ("Benito", "Juarez"),
        ("Jaime", "Kiroz")
    ]
)
def test_mayus_clients(name,last_name):
    client = Client.objects.create(name=name, last_name=last_name)
    print(client)
    assert client.name[0].isupper()
    assert client.last_name[0].isupper()

@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, last_name",
    [
        ("Pedro", "Picapiedra"),
        ("Juan", "Perez"),
        ("Benito", "Juarez"),
        ("Jaime", "Kiroz")
    ]
)
def test_null_clients(name,last_name):
    client = Client.objects.create(name=name, last_name=last_name)
    print(client)
    assert client.name is not True