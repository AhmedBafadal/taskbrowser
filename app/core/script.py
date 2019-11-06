from core.models import Task
from datetime import datetime, timezone
# callback funcs


def check_if_leaf(task):
    task_children = task.children_tasks.all()
    if not task_children.exists():
        return True
    else:
        return False


def leaf_node(tasks_queryset, leaf_nodes_list):
    for task in tasks_queryset:
        if check_if_leaf(task):
            leaf_nodes_list.append(task)
        else:
            leaf_node(task.children_tasks.all(), leaf_nodes_list)
            break
    return leaf_nodes_list


def leaf_nodes():
    leaf_nodes_list = []
    root_parent_tasks = Task.objects.filter(parent=None)

    return leaf_node(root_parent_tasks, leaf_nodes_list)


if __name__ == "__main__":
    leaf_nodes()
