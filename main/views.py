from django.shortcuts import render,HttpResponse
from main.models import NFTData
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.http import JsonResponse


# Create your views here.


@csrf_exempt
def nft(request):
    if request.method == 'GET':
        NFT_json = serializers.serialize("json", NFTData.objects.all())
        # NFT_json = NFTData.objects.all()
        # NFT_json = {"data" : NFTData.objects.all()}
        # return HttpResponse(NFT_json, content_type='application/json')
        return HttpResponse(NFT_json, content_type='application/json')
    else:
        data = request.body.decode('utf-8')
        recieved_data = json.loads(data)
        # obj = NFTData(key =  recieved_data['name'], image_url = recieved_data['image_url'])
        obj = NFTData(data = recieved_data)
        obj.save()
        return HttpResponse("successful")