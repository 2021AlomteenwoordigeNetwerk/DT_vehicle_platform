import datetime as datetime
from django.http import HttpResponse
from web.models import infrared, ultrasonic, images
import datetime
import uuid
import json
def getInfraredData(request):
    data = infrared.objects.all()
    response = "["
    for var in data:
        response += "{ \"id\": \"" + str(
            var.id) + "\", \"infrared_data\": \"" + str(var.infrared_data) + "\", \"get_data_time\": \"" \
                    + str(var.get_data_time) + "\"},"
    response = response[:-1]
    response += "]"
    return HttpResponse(response)
def saveInfraredData(request):
    id = uuid.uuid1().hex
    infrared_data = request.GET['infrared_data']
    get_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = infrared(id=id, infrared_data=infrared_data, get_data_time=get_data_time)
    data.save()
    return HttpResponse("success")
def updateInfraredData(request):
    id = request.GET['id']
    infrared_data = request.GET['infrared_data']
    data = infrared.objects.get(id=id)
    data.infrared_data = infrared_data
    data.save()
    return HttpResponse("success")
def deleteInfraredData(request):
    id = request.GET['id']
    data = infrared.objects.get(id=id)
    data.delete()
    return HttpResponse("success")
def getUltrasonicData(request):
    data = ultrasonic.objects.all()
    response = "["
    for var in data:
        response += "{ \"id\": \"" + str(
            var.id) + "\", \"ultrasonic_data\": \"" + str(var.ultrasonic_data) + "\", \"get_data_time\": \"" \
                    + str(var.get_data_time) + "\"},"
    response = response[:-1]
    response += "]"
    return HttpResponse(response)
def saveUltrasonicData(request):
    id = uuid.uuid1().hex
    ultrasonic_data = request.GET['ultrasonic_data']
    get_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = ultrasonic(id=id, ultrasonic_data=ultrasonic_data, get_data_time=get_data_time)
    data.save()
    return HttpResponse("success")
def updateUltrasonicData(request):
    id = request.GET['id']
    ultrasonic_data = request.GET['ultrasonic_data']
    data = ultrasonic.objects.get(id=id)
    data.ultrasonic_data = ultrasonic_data
    data.save()
    return HttpResponse("success")
def deleteUltrasonicData(request):
    id = request.GET['id']
    data = ultrasonic.objects.get(id=id)
    data.delete()
    return HttpResponse("success")
def getImagesData(request):
    data = images.objects.all()
    response = "["
    for var in data:
        response += "{ \"id\": \"" + str(
            var.id) + "\", \"images_data\": \"" + str(var.images_data) + "\", \"get_data_time\": \"" \
                    + str(var.get_data_time) + "\"},"
    response = response[:-1]
    response += "]"
    return HttpResponse(response)
def saveImagesData(request):
    id = uuid.uuid1()
    image_data = request.FILES.get('image')
    get_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    res = images(id=id, images_data=image_data, get_data_time=get_data_time)
    res.save()
    return HttpResponse('yes')
def updateImagesData(request):
    id = request.GET['id']
    images_data = request.GET['images_data']
    data = images.objects.get(id=id)
    data.images_data = images_data
    data.save()
    return HttpResponse("success")
def deleteImagesData(request):
    id = request.GET['id']
    data = images.objects.get(id=id)
    data.delete()
    return HttpResponse("success")