from django.urls import path
from . import views


urlpatterns = [
    path('addlaptop/',views.addLaptopView,name='add'),
    path('showlaptop/',views.showLaptopView,name='show'),
    path('update/<int:id>/',views.updateView,name='update'),
    path('delete/<int:id>/',views.deleteView,name='delete')
]