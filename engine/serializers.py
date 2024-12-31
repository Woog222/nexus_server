from rest_framework import serializers
from .models import NexusFile

class NexusFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NexusFile
        fields = ['name', 'extension']

    def to_representation(self, instance):
        # Customize the representation format to "name.file_extension"
        return f"{instance.name}.{instance.file_extension}"
