from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )
