import csv
import io

from django.core.files import File
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, filters, status
from .serializers import TeacherSerializer, UploadSerializer, SubjectSerializer
from .models import Teacher, Subject
from rest_framework.response import Response


class TeacherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing teacher instances.
    """
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['last_name', 'subject__subject']


class SubjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing subject instances.
    """
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class UploadViewSet(viewsets.ViewSet):
    serializer_class = UploadSerializer

    def create(self, request):

        csv_file = request.data['file']
        decoded_file = csv_file.read().decode('utf-8')
        reader = csv.reader(io.StringIO(decoded_file), delimiter=',')
        next(reader, None)

        for row in reader:
            data = {}
            """Image not found , will take default image"""
            try:
                image_file = File(open('media/' + row[2], 'rb'))
                data.update({"image": image_file})
            except IOError:
                pass

            subjects = [x.strip() for x in row[6].split(',')]

            if len(subjects) > 5:
                return Response(
                    row[0] + " " + row[1] + "A teacher can teach no more than 5 subjects, Please Check Excel sheet",
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    sublist = [Subject.objects.get(subject__startswith=sub).id for sub in subjects]
                except Exception:
                    return Response("Subjects listed in Excel File, Not present in DB",
                                    status=status.HTTP_400_BAD_REQUEST)

            data.update({"first_name": row[0], "last_name": row[1],
                         "email_id": row[3], "phone": row[4], "room_no": row[5], "subject": sublist})

            serializer = TeacherSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
