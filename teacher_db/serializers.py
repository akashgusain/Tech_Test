from rest_framework import serializers
from rest_framework.serializers import FileField
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """
    used for returning the teacher details
    """
    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Teacher
        fields = '__all__'

    def validate_subject(self, value):
        subjects = value.split(',')
        if len(subjects) > 5:
            raise serializers.ValidationError("A teacher can teach no more than 5 subjects")
        return value


class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)
