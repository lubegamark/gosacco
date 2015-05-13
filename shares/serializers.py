from rest_framework import serializers

from shares.models import ShareType, Shares


class SharesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shares


class ShareTypeSerializer(serializers.ModelSerializer):
    shareType = SharesSerializer(many=True, read_only=True)

    class Meta:
        model = ShareType
        # fields = ()