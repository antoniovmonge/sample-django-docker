import pytest

from members.models import Member


@pytest.mark.django_db
def test_add_member(client):
    members = Member.objects.all()
    assert len(members) == 0

    resp = client.post(
        "/api/members/",
        {
            "name": "Bill Gates",
            "position": "IT Intern",
            "fun_fact": "He makes great coffee",
        },
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "Bill Gates"

    members = Member.objects.all()
    assert len(members) == 1


@pytest.mark.django_db
def test_add_member_invalid_json(client):
    members = Member.objects.all()
    assert len(members) == 0

    resp = client.post("/api/members/", {}, content_type="application/json")
    assert resp.status_code == 400

    members = Member.objects.all()
    assert len(members) == 0


@pytest.mark.django_db
def test_add_member_invalid_json_keys(client):
    members = Member.objects.all()
    assert len(members) == 0

    resp = client.post(
        "/api/members/",
        {
            "name": "Thomas A. Anderson - Neo",
            "position": "Microsoft Excel expert",
        },
        content_type="application/json",
    )
    assert resp.status_code == 400

    members = Member.objects.all()
    assert len(members) == 0


@pytest.mark.django_db
def test_get_single_member(client, add_member):
    member = add_member(
        name="Thomas A. Anderson - Neo",
        position="Microsoft Excel Expert",
        fun_fact="He likes Trinity and flying",
    )
    resp = client.get(f"/api/members/{member.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Thomas A. Anderson - Neo"


def test_get_single_member_incorrect_id(client):
    resp = client.get("/api/members/foo")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_members(client, add_member):
    member_one = add_member(
        name="Thomas A. Anderson - Neo",
        position="Microsoft Excel Expert",
        fun_fact="He likes Trinity and flying",
    )
    member_two = add_member(
        "Elliot Alderson",
        "Microsoft Word Intern",
        "Learning to use the keyboard looking only at the screen",
    )
    resp = client.get("/api/members/")
    assert resp.status_code == 200
    assert resp.data[0]["name"] == member_one.name
    assert resp.data[1]["name"] == member_two.name
