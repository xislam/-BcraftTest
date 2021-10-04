from rest_framework import serializers

from .models import Statistics

DATETIME_FORMAT = '%Y-%m-%d '


class StatisticsSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=DATETIME_FORMAT)

    class Meta:
        model = Statistics
        fields = '__all__'
