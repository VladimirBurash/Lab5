from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
data = {
    'artists': [
        {'id': 1, 'name': 'Каста', 'author':'Влади,Шым,Хамиль,Змей'},
        {'id': 2, 'name': 'Жара', 'author': 'Артем Кечиев'},
        {'id': 3, 'name': 'Макс Корж', 'author': 'Максим корж'},
        {'id': 4, 'name': 'Чаян Фамали', 'author': 'Артур Чаянов,Андрей Ворон'},
        {'id': 5, 'name': 'ГРОТ', 'author': 'Витайли Явсеев,Матвей Рябов,Дмитрий Геращенко'},
    ]
}
def function_view(request):
    return HttpResponse('response from function view')

class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')

class ArtistsView(View):
    def get(self, request):
        return render(request, 'listPage.html', data)

class ArtistView(View):
    def get(self, request, id):
        selectedArtists = None
        for artist in data['artists']:
            if int(id) == artist['id']:
                selectedArtists = artist
        return render(request, 'artistPage.html', selectedArtists)
