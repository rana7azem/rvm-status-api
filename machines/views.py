from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RVM
from .serializers import RVMSerializer
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

class RVMListCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'POST':
           return [IsAuthenticated()]
        
        return [AllowAny()]

    def get(self, request):
        rvms = RVM.objects.all()
        #apply filtering by status
        status_filter = request.query_params.get('status', None)
        if status_filter:
            rvms = rvms.filter(Q(status=status_filter) | Q(status__icontains=status_filter))

        #apply ordering by last_usage
        order_by = request.query_params.get('order_by', 'last_usage')
        if order_by:
            rvms = rvms.order_by(order_by)

        #apply search by location
        search = request.query_params.get('search', None)
        if search:
            rvms = rvms.filter(location__icontains=search)
        

        serializer = RVMSerializer(rvms, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("RAW DATA:", request.body)  
        print("PARSED DATA:", request.data)  

        serializer = RVMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  

