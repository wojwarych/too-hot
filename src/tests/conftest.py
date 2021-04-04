import pytest

from .factories import fake_sequence


@pytest.fixture
def mock_sequences(faker, mongodb):
    sequences = [fake_sequence() for i in range(faker.pyint(max_value=10))]
    mongodb.sequences.insert_many(sequences)
