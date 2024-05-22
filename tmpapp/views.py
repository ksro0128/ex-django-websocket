from django.shortcuts import render

# Create your views here.
def websocket_test_view(request):
    return render(request, 'tmpapp/websocket_test.html')

def index(request):
    return render(request, 'tmpapp/index.html')

def room(request, room_name):
	return render(request, 'tmpapp/room.html', {
		'room_name': room_name
	})
