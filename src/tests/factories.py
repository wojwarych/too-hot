import random

from faker import Faker

from ..models import NUCLEOTIDES, Sequence

fake = Faker()


def fake_sequence():
    return dict(
        name=fake.pystr(),
        sequence="".join(random.choices(NUCLEOTIDES, k=fake.pyint()))
    )


def fake_incorrect_sequence():
    return dict(
        name=fake.pystr(),
        sequence=fake.pystr()
    )
