from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .this_scrapper import THIS_SCRAPPER


@api_view(['PUT'])
def setUsersCollectorFilter(request):
    THIS_SCRAPPER.users_collector.setSearchFilter(request.data)
    return Response()


@api_view(['PUT'])
def setUsersCollectorSettings(request):
    THIS_SCRAPPER.users_collector.setSettings(request.data)
    return Response()


@api_view(['PUT'])
def runUsersCollector(request):
    THIS_SCRAPPER.users_collector.run()
    return Response()


@api_view(['PUT'])
def pauseUsersCollector(request):
    THIS_SCRAPPER.users_collector.pause()
    return Response()


@api_view(['PUT'])
def unpauseUsersCollector(request):
    THIS_SCRAPPER.users_collector.unpause()
    return Response()


@api_view(['PUT'])
def stopUsersCollector(request):
    THIS_SCRAPPER.users_collector.stop()
    return Response()


@api_view(['PUT'])
def startEndlessUsersCollector(request):
    THIS_SCRAPPER.users_collector.start()
    return Response()


@api_view(['PUT'])
def setPhotosCollectorFilter(request):
    THIS_SCRAPPER.usersdata_collector.setSearchFilter(request.data)
    return Response()


@api_view(['PUT'])
def setPhotosCollectorSettings(request):
    THIS_SCRAPPER.usersdata_collector.setSettings(request.data)
    return Response()


@api_view(['PUT'])
def runPhotosCollector(request):
    THIS_SCRAPPER.usersdata_collector.run()
    return Response()


@api_view(['PUT'])
def pausePhotosCollector(request):
    THIS_SCRAPPER.usersdata_collector.pause()
    return Response()


@api_view(['PUT'])
def unpausePhotosCollector(request):
    THIS_SCRAPPER.usersdata_collector.unpause()
    return Response()


@api_view(['PUT'])
def stopPhotosCollector(request):
    THIS_SCRAPPER.usersdata_collector.stop()
    return Response()


@api_view(['PUT'])
def startEndlessPhotosCollector(request):
    THIS_SCRAPPER.usersdata_collector.start()
    return Response()


@api_view(['GET'])
def status(request):
    return Response(data={
        "users_collector": THIS_SCRAPPER.users_collector.get_status(),
        "usersdata_collector": THIS_SCRAPPER.usersdata_collector.get_status(),
    })
