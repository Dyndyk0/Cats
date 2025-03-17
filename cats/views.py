from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .utils import get_random_cats, get_random_dogs
from .models import Cat
from .serializers import CatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random

@csrf_exempt
def cat_gallery_view(request):
    cats_data = get_random_cats()
    dogs_data = get_random_dogs()
    saved_cat_ids = Cat.objects.values_list('cat_id', flat=True)

    pets_data = cats_data + dogs_data
    random.shuffle(pets_data)

    if request.method == 'POST':
        cat_id = request.POST.get('cat_id')
        url = request.POST.get('url')

        if cat_id and url and cat_id not in saved_cat_ids:
            Cat.objects.create(cat_id=cat_id, url=url)
            return JsonResponse({'message': 'Котик сохранён!', 'status': 'success', 'cat_id': cat_id }) # JSON response
        elif cat_id in saved_cat_ids:
           return JsonResponse({'message': 'Котик уже ранее был сохранён!', 'status': 'error', 'cat_id': cat_id}) # JSON response

    return render(request, 'cats/cat_gallery.html', {'cats': pets_data, 'saved_cat_ids': saved_cat_ids})

@csrf_exempt
def saved_images_view(request):
    all_cats = Cat.objects.all()
    all_cats = reversed(all_cats)

    if request.method == 'DELETE':
        try:
            data = json.loads(request.body.decode('utf-8')) # Парсим тело запроса JSON
            cat_id = data.get('cat_id') # Извлекаем cat_id
            if cat_id:
                try:
                    cat = get_object_or_404(Cat, cat_id=cat_id)
                    cat.delete()
                    return JsonResponse({'message': 'Котик удалён!', 'status': 'success', 'cat_id': cat_id })
                except Exception as e:
                    return JsonResponse({'message': 'Котик уже был удалён!', 'status': 'error', 'cat_id': cat_id })
            else:
                return HttpResponse("Неверные данные", status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Ошибка JSON', 'status': 'error', "error": str(e)}, status=400)
    return render(request, 'cats/saved_images.html', {'cats': all_cats})

class CatList(APIView):
    def get(self, request):
        all_pets = Cat.objects.all()
        all_pets = reversed(all_pets)
        serializer = CatSerializer(all_pets, many=True)
        return Response(serializer.data)

@csrf_exempt
def delete_cat(request, cat_id):
    if request.method == 'DELETE':
        try:
            cat = get_object_or_404(Cat, cat_id=cat_id)
            cat.delete()
            return JsonResponse({'message': 'Картинка удалена'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse("Method not allowed", status=405)