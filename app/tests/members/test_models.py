import pytest

from members.models import Member


@pytest.mark.django_db
def test_member_model():
    member = Member(
        name="Phanos",
        position="Co-founder & CEO",
        fun_fact="""
            Obsessed with the sea, movement, cooking and working on changing the world!
            """,
    )
    member.save()
    assert member.name == "Phanos"
    assert member.position == "Co-founder & CEO"
    assert (
        member.fun_fact
        == """
            Obsessed with the sea, movement, cooking and working on changing the world!
            """
    )
    assert member.created_date
    assert member.updated_date
    assert str(member) == member.name
