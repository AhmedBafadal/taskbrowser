from rest_framework import viewsets, mixins
from core.models import Task
from . import serializers
from . import task_helper
# Create your views here.
from django.views.generic import ListView



class TaskViewSet(viewsets.GenericViewSet, mixins.ListModelMixin
            ,mixins.RetrieveModelMixin):
    """Manage Tasks in database"""
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        queryset = Task.objects.filter(parent=None)
        leaf_nodes_list, parents_node_list = task_helper.leaf_nodes(Task.objects.filter(parent=None))
        task_helper.set_status_leafnodes(leaf_nodes_list)
        task_helper.set_status_parent_node(parents_node_list)
        return self.queryset.order_by('id')


    def get(self, request):
        print('HEY IM HERE')
        print(request)
        return self.list(request)


