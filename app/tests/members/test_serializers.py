from members.serializers import MemberSerializer


def test_valid_member_serializer():
    valid_serializer_data = {
        "name": "Phanos",
        "position": "Co-founder & CEO",
        "fun_fact": "Obsessed with the sea, movement, cooking and working on changing the world!",
    }
    serializer = MemberSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_member_serializer():
    invalid_serializer_data = {
        "name": "Phanos",
        "position": "Co-founder & CEO",
    }
    serializer = MemberSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"fun_fact": ["This field is required."]}
