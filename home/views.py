import json
import logging
from django.http import JsonResponse
from .models import BinaryTree, TreeNode
from django.shortcuts import render, redirect, get_object_or_404
from .Traversal import *

# get an instance of logger
logger = logging.getLogger(__name__)
# landing page function
def home(request):
	template_name = "home/home.html"
	try:
		if request.method == 'GET':
			trees = BinaryTree.objects.filter(status=1).order_by('-id')
			context = {'trees': trees}
			return render(request, template_name, context)
	except Exception as e:
		logger.error(e)
		return render(request, template_name)

# add new tree and nodes of that tree
def addTree(request):
	template_name = "home/addtree.html"
	if request.method == 'GET':
		return render(request, template_name)
	elif request.method == 'POST':
		tree_name = request.POST['name'].strip()
		node = request.POST['node']
		nodes = node.split(",")
		#  remove white space and empty string from nodes input
		finalnodes = []
		for item in nodes:
			if item.strip():
				finalnodes.append(item)
		current_parent_id = 0
		posistion_node = TreeNode.OTHER
		btree = BinaryTree()
		if not tree_name:
			tree_get_id = BinaryTree.objects.all().order_by('-id')[:1]
			if tree_get_id:
				tree_name = "tree"+str(tree_get_id[0].id+1)
			else:
				tree_name = "tree1"
		try:
			BinaryTree.objects.get(name=tree_name)
			context = {'error': "Tree already exists! Try with other name..."}
			return render(request, template_name, context)
		except BinaryTree.DoesNotExist:
			btree.name = tree_name
			if len(finalnodes) > 2:
				btree.save()
				for item in finalnodes:
					node_value = item.strip()
					treeNodeObj = TreeNode(value=node_value, parent_id=current_parent_id, position=posistion_node, tree_id=btree.id)
					if current_parent_id == 0 and node_value:
						treeNodeObj.save()
						current_parent_id = treeNodeObj.id
						posistion_node = TreeNode.LEFT
					elif posistion_node == TreeNode.LEFT and node_value:
						treeNodeObj.save()
						posistion_node = TreeNode.RIGHT
					elif posistion_node == TreeNode.RIGHT and node_value:
						treeNodeObj.save()
						current_parent_id = treeNodeObj.id
						posistion_node = TreeNode.LEFT
				return redirect('home')
			else:
				context = {'error': "Nodes count must be greater than equal to 3"}
				return render(request, template_name, context)

# get single tree data function
def getTree(request, id):
	template_name = "home/singleTree.html"
	tree = BinaryTree.objects.filter(id=id).filter(status=1)
	if tree:
		nodes = list(TreeNode.objects.filter(tree=id).order_by('id'))
		context = {'tree': tree,'nodes': nodes}
		return render(request, template_name, context)
	else:
		return redirect('home')

# add new node in existing tree function
def addNode(request):
	if request.method == 'POST':
		tid = request.POST['tree']
		node_data = request.POST['node'].strip()
		if node_data:
			node = TreeNode.objects.filter(tree=tid).order_by('-id')[:2]
			inNode = TreeNode()
			if node[0].position == TreeNode.RIGHT:
				if node[0].parent_id == node[1].parent_id:
					inNode.parent_id = node[0].parent_id + 2
				else:
					inNode.parent_id = node[0].parent_id
				inNode.value = request.POST['node']
				inNode.tree = get_object_or_404(BinaryTree, id=tid)
				inNode.position = TreeNode.LEFT
				inNode.save()
			elif node[0].position == TreeNode.LEFT:
				if node[0].parent_id == node[1].parent_id:
					inNode.parent_id = node[0].parent_id + 2
				else:
					inNode.parent_id = node[0].parent_id
				inNode.value = request.POST['node']
				inNode.tree = get_object_or_404(BinaryTree, id=tid)
				inNode.position = TreeNode.RIGHT
				inNode.save()
			return redirect('tree/'+tid)
		else:
			return redirect('tree/'+tid)

# In Order, Pre Order Post Order Travesal function 
def treeTraversal(request):
	if request.method == 'POST':
		try:
			tree_id = request.POST.get('tree', None)
			type = request.POST.get('type', None)
			nodes = list(TreeNode.objects.filter(tree=tree_id).order_by('id').values('value'))
			root = None
			travel = Traversal()
			root = insertLevelOrder(nodes, root, 0, len(nodes))
			result = []
			# below conditions are assign the result value according to the requirement of client
			if type == 'inorder':
				result = travel.inorderTraversal(root)
			if type == 'preorder':
				result = travel.preorderTraversal(root)
			elif type =='postorder':
				result = travel.postorderTraversal(root)
			return JsonResponse({'nodes': result}, safe=True)
		except Exception as e:
			return JsonResponse({'nodes': e})

# delete tree 
def deleteTree(request,id):
	if request.method == 'POST':
		BinaryTree.objects.filter(id=id).update(status=0)
		return redirect('home')