from rest_framework import serializers
from rest_framework.serializers import FileField
from .models import Teacher, Subject


class TeacherSerializer(serializers.ModelSerializer):
    """
    used for returning the teacher details
    """
    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    # subject = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["subject"] = SubjectSerializer(instance.subject.values('subject'), many=True).data
        return rep

    def validate_subject(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("A teacher can teach no more than 5 subjects")
        return value


class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
