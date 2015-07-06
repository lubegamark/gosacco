from rest_framework import serializers

from shares.models import ShareType, Shares, SharePurchase, ShareTransfer


class SharesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shares


class ShareTypeSerializer(serializers.ModelSerializer):
    # shareType = SharesSerializer(many=True, read_only=True)

    class Meta:
        model = ShareType
        fields = ('id','share_class','share_price','minimum_shares','maximum_shares')

class SharePurchaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = SharePurchase

class ShareTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareTransfer