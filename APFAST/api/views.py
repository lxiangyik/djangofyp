from django.http import HttpResponse, JsonResponse
from APFAST.models import Announcement
from .serializer import AnnouncementSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def AnnoucementList(request): 

    if request.method == 'GET': #get all annoucement data
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return JsonResponse({'Annoucement' : serializer.data}, safe=False)

    if request.method == 'POST': #add annoucement
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def AnnouncementDetail(request, pk):
    #check is it valid, try run (actions), except will handle the error, break with return, else continue after try
    try:
        announcements = Announcement.objects.get(id=pk) #get the certain id table data, for example get data id 1
    except Announcement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        
    #show certain data
    if request.method == 'GET': 
        serializer = AnnouncementSerializer(announcements) 
        return Response(serializer.data) 
        # return JsonResponse(serializer.data, safe=False) same thing but with rest response
    
    #update certain data
    elif request.method == 'PUT': 

        #replace the old data with edited data
        serializer = AnnouncementSerializer(announcements, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete certain data
    elif request.method == 'DELETE':
        announcements.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

