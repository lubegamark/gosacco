from rest_framework import serializers
from members.serializers import MemberSerializer
from shares.models import ShareType, Shares, SharePurchase, ShareTransfer


class ShareTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareType
        fields=('id','share_class','share_price','minimum_shares','maximum_shares')

class SharesSerializer(serializers.ModelSerializer):
    share_type = ShareTypeSerializer()
    member = MemberSerializer()
    class Meta:
        model = Shares
        fields =('id','member','share_type','number_of_shares','date')


class SharePurchaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = SharePurchase
        # fields = ('id','member','current_share_price','number_of_shares','date','share_type')

class ShareTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareTransfer
