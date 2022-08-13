import factory
import factory.fuzzy as fuzzy
import random

from ..app.app import db
from ..app.models import Client, Parking


class ClientFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Client
        sqlalchemy_session = db.session

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    credit_card = factory.Sequence(lambda n: '1231-5551-0000-%04d' % n)
    car_number = factory.Sequence(lambda n: 'A%03dAA99' % n)


class ParkingFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Parking
        sqlalchemy_session = db.session

    address = fuzzy.FuzzyText(prefix='Адрес ')
    opened = random.choice([True, False])
    count_places = random.randrange(0, 100)
    count_available_places = factory.LazyAttribute(lambda obj: '%s' % obj.count_places)
