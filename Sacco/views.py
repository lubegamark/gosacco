from Sacco.models import Member, Group
from Sacco.serializers import MemberSerializer, GroupSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def member_list(request):
    """
    List all members, or create a new member.
    """
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def group_list(request):
    """
    List all groups, or create a new group.
    """
    if request.method == 'GET':
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def member_detail(request, pk):
    """
    Retrieve, update or delete a member.
    """
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(member, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        member.delete()
        return HttpResponse(status=204)


@csrf_exempt
def group_detail(request, pk):
    """
    Retrieve, update or delete a member group.
    """
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(group, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        group.delete()
        return HttpResponse(status=204)