from django.db import models

# Create your models here.

class BinaryTree(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, unique=True)
	status = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = "tree"

	def __str__(self):
		return self.name


class TreeNode(models.Model):
	LEFT = 'L'
	RIGHT = 'R'
	OTHER = 'N'
	POSITION = (
        (LEFT, 'L'),
        (RIGHT, 'R'),
    )
	id = models.AutoField(primary_key=True)
	tree = models.ForeignKey(BinaryTree, on_delete=models.CASCADE)
	value = models.CharField(max_length=150)
	parent_id = models.IntegerField(default=0)
	position = models.CharField(max_length=2, choices=POSITION, default=OTHER)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = "node"

	def __str__(self):
		return self.value