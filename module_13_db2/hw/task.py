import faker

fake = faker.Faker()

numbers = set(fake.unique.random_int() for i in range(100))
print(numbers)
assert len(numbers) == 100