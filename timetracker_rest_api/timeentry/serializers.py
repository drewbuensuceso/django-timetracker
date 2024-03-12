from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'tasks']
        
    def create(self, validated_data):

        project = Project(
            name = validated_data['name'],
            tasks = validated_data['tasks']
        )
        project.save()

        return project
    
    def delete(self, validated_data):

        project = Project(
            name = validated_data['name'],
            tasks = validated_data['tasks']
        )
        project.delete()
        
        return project