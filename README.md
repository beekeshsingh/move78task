Task:
1) Create a Django Webapp
2) Display and store a binary search tree
(Database of your choice)
3) User can add and delete a tree
4) On adding a tree, user should be prompted to enter at least 3 nodes
5) User can add nodes to an existing tree
6) A binary search tree structure should be displayed when a tree is selected, with its
respective nodes in the order of insertion
7) Buttons for printing preorder, postorder, inorder should also be there for each tree
8) All changes must be updated in the database
9) Extra points for highlighting nodes while traversing in either of the above orders
Development:
The main page should display all the trees and a button to add more trees. You can ask the
user to name each tree or just save it like tree1, tree2 and so on.
When a tree is selected on the home page, the structure of the tree should be displayed
and the buttons for displaying various orders, deleting the tree or adding new node.


Setup:

1. clone the task https://github.com/beekeshsingh/move78task.git
2. required Python 3.7.4, Django==2.2.7, mysqlclient==1.4.5, pip3
3. create venv and run pip3 freeze < requirements.txt
4. python3 manage.py makemigrations;
5. python3 manage.py migrate;
6. python3 manage.py runserver


