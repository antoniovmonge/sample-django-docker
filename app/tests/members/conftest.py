import pytest

from members.models import Member


@pytest.fixture(scope="function")
def add_member():
    def _add_member(name, position, fun_fact):
        member = Member.objects.create(name=name, position=position, fun_fact=fun_fact)
        return member

    return _add_member
