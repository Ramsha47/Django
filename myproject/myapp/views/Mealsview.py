from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Meal
from myapp.api.serializer import MealSerializer

@api_view(['GET'])
def meals_list(request):
    cached_data = cache.get('meals_list')
    if cached_data:
        return Response({'source': 'cache', 'data': cached_data})
    else:
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        cache.set('meals_list', serializer.data, timeout=60)  # Cache for 1 hour
        return Response({'source': 'database', 'data': serializer.data})
@api_view(['GET'])
def meal_detail(request, pk):
    try:
        meal = Meal.objects.get(pk=pk)
    except Meal.DoesNotExist:
        return Response(status=404)

    serializer = MealSerializer(meal)
    return Response(serializer.data)
