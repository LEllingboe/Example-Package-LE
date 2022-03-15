from example_package_le.main import custom_add


def test_custon_add():
    assert custom_add(1, 4) == 5
    assert custom_add(5, 7) == 12
    assert custom_add(2, 3) == 5
