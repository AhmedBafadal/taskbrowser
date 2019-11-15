from core.models import Task
from datetime import datetime, timezone
from collections import Counter


def check_if_leaf(task):
    task_children = task.children_tasks.all()
    if not task_children.exists():
        return True
    else:
        return False


def leaf_node(tasks_queryset, leaf_nodes_list, parents_node_list):
    for task in tasks_queryset:
        if check_if_leaf(task):
            leaf_nodes_list.append(task)

        else:
            parents_node_list.append(task)
            leaf_node(task.children_tasks.all(), leaf_nodes_list, parents_node_list)
    # reverse parents list to set parent statuses in correct order (e.g. B1 before B)
    return leaf_nodes_list, reverse(parents_node_list)


def leaf_nodes():
    leaf_nodes_list = []
    root_parent_tasks = Task.objects.filter(parent=None)
    
    return leaf_node(root_parent_tasks, leaf_nodes_list,)


def set_status_leafnodes(nodes):
    for task in nodes:
        if task.start_timestamp > datetime.now():
            task.status = 'scheduled'
            task.save()
        elif  task.start_timestamp < datetime.now() < task.end_timestamp:
            task.status = 'running'
            task.save()
        elif datetime.now() > task.end_timestamp:
            task.status = 'complete'
            task.save()


def set_status_parent_node(parent_nodes):
    # need to go bottom up. tasks ordered that way to decipher parent node status
    # order parent nodes
    for task in parent_nodes:
        # list of statuses of children
        children_tasks_status = list(task.children_tasks.values_list('status', flat=True))
        if all(children_tasks_status  == 'scheduled'):
            task.status = 'scheduled'
            task.save()
        elif any(children_tasks_status == 'running'):
            task.status = 'running'
            task.save()
            # multi-runs
            

        elif Counter(children_tasks_status).get('running'))>2:
            task.status = 'multi_runs'
            task.save()
        # idle
        elif any(children_tasks_status == 'complete') and any(children_tasks_status == 'scheduled') and all(children_tasks_status!='running'):
            task.status = 'idle'
            task.save()

# write script to load test data
# the status of hte application owuld need to be refreshed every x mins due to leaf nodes depending on current time
# view to visualise
# read only fields status
# script to add dummy data to the database
# authentication
# ptyhon manage.py shell docker exec -it <containerid>
if __name__ == "__main__":
    leaf_nodes_list, parents_node_list = leaf_nodes()
    set_status_leafnodes(leaf_nodes_list)
    set_status_parent_node(parents_node_list)