from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from members.models import Member, Group, NextOfKin
from loans.models import LoanApplication, Security, SecurityShares, SecuritySavings, SecurityArticle, SecurityGuarantor
from members.serializers import MemberSerializer, MemberUserSerializer


class LoanSerializer(serializers.ModelSerializer):
    member = MemberUserSerializer()


class LoanApplicationSerializer(serializers.ModelSerializer):
    member = MemberUserSerializer()

    class Meta:
        model = LoanApplication


class SecuritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Security

    def to_representation(self, obj):
        """
        Because Security is Polymorphic
        """
        if isinstance(obj, SecuritySavings):
            return SecuritySavingsSerializer(obj, context=self.context). to_representation(obj)
        elif isinstance(obj, SecurityShares):
            return SecuritySharesSerializer(obj, context=self.context). to_representation(obj)
        elif isinstance(obj, SecurityArticle):
            return SecurityArticleSerializer(obj, context=self.context). to_representation(obj)
        elif isinstance(obj, SecurityGuarantor):
            return SecurityGuarantorSerializer(obj, context=self.context). to_representation(obj)

        return super(SecuritySerializer, self). to_representation(obj)


class SecuritySharesSerializer(serializers.ModelSerializer):
    security_type = serializers.SerializerMethodField()

    class Meta:
        model = SecurityShares
        exclude = ('polymorphic_ctype',)

    def get_security_type(self, obj):
        return obj.polymorphic_ctype.name


class SecuritySavingsSerializer(serializers.ModelSerializer):
    security_type = serializers.SerializerMethodField()

    class Meta:
        model = SecuritySavings
        exclude = ('polymorphic_ctype',)

    def get_security_type(self, obj):
        return obj.polymorphic_ctype.name

class SecurityArticleSerializer(serializers.ModelSerializer):
    security_type = serializers.SerializerMethodField()

    class Meta:
        model = SecurityArticle
        exclude = ('polymorphic_ctype',)

    def get_security_type(self, obj):
        return obj.polymorphic_ctype.name

class SecurityGuarantorSerializer(serializers.ModelSerializer):
    security_type = serializers.SerializerMethodField()

    class Meta:
        model = SecurityGuarantor
        exclude = ('polymorphic_ctype',)

    def get_security_type(self, obj):
        return obj.polymorphic_ctype.name