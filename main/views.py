# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Note
from main.serializer import NoteSerializer


class AddNote(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        data = request.data
        ser = NoteSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response('invalid')


class GetNotes(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        notes = Note.objects.all()
        ser = NoteSerializer(notes, many=True)

        return Response(ser.data, content_type='json')
