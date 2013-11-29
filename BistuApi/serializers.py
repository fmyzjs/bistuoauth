from django.forms import widgets
from rest_framework import serializers
from models import Student
class StudentSerializer(serializers.ModelSerializer):
    mystudentsdetail = serializers.HyperlinkedRelatedField(many=True, view_name='student-detail')
    class Meta:
        model = Student    
        fields = ('id','idtype','userid','username')

    email = serializers.EmailField()
    userid = serializers.CharField(max_length=10)

    pk = serializers.IntegerField()  # Note: `Field` is an untyped read-only field.
    id=pk


    username= serializers.CharField(max_length=20)



    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance

            instance.id = attrs['id']
            instance.userid = attrs['userid']
            instance.username = attrs['username']
            
            return instance

        # Create new instance
        return Student(**attrs)