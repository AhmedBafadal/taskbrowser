# Task.objects.filter(parent_id=None)
# children[0].parent_task.all().exists()
# a[0].children_tasks.all()
# if none subtasks strted, scheduled.
# list of parents until access leaf node

# leaf task based on time
# parent task based on children
# a.parent_task.all().values_list("status", flat=True)
# from django.db.models import Max
# a.parent_task.all().aggregate(Max("end_timestamp"))["end_timestamp__max"]
