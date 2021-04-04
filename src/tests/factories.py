from faker import Faker

from ..models import Sequence

fake = Faker()


def fake_sequence():
    return Sequence(name=fake.pystr(), sequence=fake.pystr()).dict()
