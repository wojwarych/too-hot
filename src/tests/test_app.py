import sys

import pytest
from fastapi.testclient import TestClient

from .factories import fake_sequence
from ..main import app
from ..models import Sequence

client = TestClient(app)


def test_list_sequences_returns_correct_data_on_200(mock_sequences, mongodb):
    response = client.get("/sequences/")

    assert response.status_code == 200
    assert len(response.json()) == mongodb.sequences.estimated_document_count()


def test_create_sequence_returns_correct_data_on_201(mongodb):
    fake_seq = fake_sequence()
    response = client.post("/sequences/", json=fake_seq)

    assert response.status_code == 201
    assert response.json()["name"] == fake_seq["name"]
