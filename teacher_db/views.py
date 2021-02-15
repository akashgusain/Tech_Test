import csv
import io

from django.core.files import File
from rest_framework import viewsets, filters, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Teacher, Subject
from .serializers import TeacherSerializer, UploadSerializer, SubjectSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing teacher instances.
    """
    parser_classes = (MultiPartParser,)
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
        data_list = []

        for row in reader:
            teacher_dict = {}
            """Image not found , will take default image"""
            try:
                image_file = File(open('teacher_image/' + row[2], 'rb'))

                teacher_dict.update({"image": image_file})
            except IOError:
                pass

            subjects = [x.strip() for x in row[6].split(',')]

            if len(subjects) > 5:
                return Response(
                    row[0] + " " + row[1] + " A teacher can teach no more than 5 subjects, Please Check Excel sheet",
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    sublist = [Subject.objects.get(subject__istartswith=sub).id for sub in subjects]
                except Exception as ex:
                    return Response("Subjects listed in Excel File, Not present in DB",
                                    status=status.HTTP_400_BAD_REQUEST)

            teacher_dict.update({"first_name": row[0], "last_name": row[1],
                                 "email_id": row[3], "phone": row[4], "room_no": row[5], "subject": sublist})

            data_list.append(teacher_dict)

        serializer = TeacherSerializer(data=data_list, many=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
