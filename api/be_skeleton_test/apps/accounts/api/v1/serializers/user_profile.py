from rest_framework import serializers

from be_skeleton_test.apps.accounts.models import UserAccount


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = UserAccount
        fields = ("email", "first_name", "last_name")
