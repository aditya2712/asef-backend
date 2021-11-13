from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from rest_framework import serializers

# API view to return List of jobs
class JobListView(APIView):
    class JobSerializer(serializers.ModelSerializer):
        class Meta:
            model = Job
            fields = ("id", "position", "company")

    def get(self, request):
        jobs = Job.objects.all()
        serializer = self.JobSerializer(jobs, many=True)
        return Response(serializer.data)


# API view to return a single job
class JobDetailView(APIView):
    class JobSerializer(serializers.ModelSerializer):
        class Meta:
            model = Job
            fields = "__all__"

    def get(self, request, job_id):
        job = Job.objects.get(pk=job_id)
        serializer = self.JobSerializer(job)
        return Response(serializer.data)


# API view to create a new job
class JobCreateView(APIView):
    class JobSerializer(serializers.ModelSerializer):
        class Meta:
            model = Job
            fields = "__all__"

        def create(self, validated_data):
            job = Job(**validated_data)
            job.full_clean()
            job.save()
            return job

    def post(self, request):
        serializer = self.JobSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=400)
