from datetime import timedelta

from django.http import Http404
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.models import Statistics
from api_v1.serializers import StatisticsSerializer


class StatisticsView(APIView):
    serializer_class = StatisticsSerializer

    def get(self, request):
        statistic = Statistics.objects.all()
        serializer = StatisticsSerializer(statistic, many=True)
        for evidences in statistic:
            cpcs = evidences.cost / evidences.clicks
            cpms = evidences.cost / evidences.views * 1000
            Statistics.objects.update(
                date=evidences.date,
                views=evidences.views,
                clicks=evidences.clicks,
                cost=evidences.cost,
                cpc=cpcs,
                cpm=cpms,
            )
        return Response({"statistic": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        # Create an statistic from the above data
        serializer = StatisticsSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            statistic_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(statistic_saved.title)})

    def put(self, request, pk):
        saved_statistic = get_object_or_404(Statistics.objects.all(), pk=pk)
        data = request.data.get('statistic')
        serializer = StatisticsSerializer(instance=saved_statistic, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            statistic_saved = serializer.save()
            return Response({
                "success": "'{}' updated successfully".format(statistic_saved.title)
            })


class PurchaseList(generics.ListAPIView):
    serializer_class = StatisticsSerializer

    def get_queryset(self):
        queryset = Statistics.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

            return queryset


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Statistics.objects.get(pk=pk)
        except Statistics.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StatisticsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StatisticsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
