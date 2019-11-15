# import psycopg2
# import os
from core.models import Task

# conn = psycopg2.connect("host='localhost' dbname='app' user='postgres' password='secretpassword'")
# cur = conn.cursor()
values = [('Task A', '2019-07-02T09:55:17Z','2019-07-02T10:55:17Z') ,('Task A.1', '2019-07-02T09:55:17Z','2019-07-02T10:55:17Z'),('Task A.2', '2019-07-02T10:50:17Z', '2019-07-02T11:55:17Z'),('Task B', '2019-07-02T10:50:17Z','2019-07-02T11:55:17Z'),('Task B.1', '2019-07-02T12:00:00Z','2019-07-02T13:00:00Z'),('Task B.1.1', '2019-07-02T12:00:00Z','2019-07-02T12:30:00Z'),('Task B.1.2', '2020-07-02T12:30:00Z','2019-07-02T13:00:00Z'),('Task B.2', '2019-07-02T10:00:00Z','2019-07-02T14:00:00Z'),('Task C', '2018-07-02T13:00:00Z','2019-07-02T15:00:00Z')]
for i in values:
    Task.create(name= values[0],start_timestamp= values[1], end_timestamp=values[2])
#     cur.execute("""INSERT INTO task (name, start_timestamp, end_timestamp) VALUES (i[0], i[1], i[2])""")
#     conn.commit()
# conn.close()