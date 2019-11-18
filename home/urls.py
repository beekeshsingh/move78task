from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('addtree', views.addTree, name='addtree'),
	path('tree/<id>', views.getTree, name='tree'),
	path('delete/<id>', views.deleteTree, name='delete'),
	path('addnode', views.addNode, name='addnode'),
	path('traversal', views.treeTraversal, name='traversal')
]