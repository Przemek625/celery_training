from celery import group
from celery.result import AsyncResult
from celery_app import app
import tasks

if __name__ == '__main__':
    result1: AsyncResult = tasks.add.delay(2, 2)
    result2: AsyncResult = tasks.mul.delay(2, 2)
    result3: AsyncResult = tasks.hello.delay()
    result4: AsyncResult = tasks.xsum.delay([2, 2])
    result5: AsyncResult = tasks.xsum.apply_async(kwargs={'numbers': [2, 2]}, countdown=10)
    result6: AsyncResult = tasks.add.apply_async(args=(2, 2), countdown=10)
    result7: AsyncResult = tasks.xsum.apply_async(args=([2, 2],), countdown=10)
    # As expected this will first launch one task calculating 2 + 2, then another task calculating 4 + 8.
    result8: AsyncResult = tasks.xsum.apply_async(
        args=([2, 2],),
        countdown=10,
        link=tasks.add.s(2)
    )
    # result3 = add_task.delay()

    # if result2.ready():
    #     print("result 2 is ready")
    #     print(result2.get())
    #
    #
    # while not result1.ready():
    #     print("result 1 is ready")

    # print(result1.get())
    # print(result2.get())
    # print(tasks.MyFirstTask().apply_async(countdown).get())
    # print(tasks.MyFirstTask().s(countdown).get())


    print(result1.get())
    print(result2.get())
    print(result3.get())
    print(result4.get())
    print("TASK 5")
    print(result5.get())
    print(result7.get())
    print("TASK 8")
    print(result8.get())
    print("TASK 8 child: ")
    print(result8.children)
    # z jakiegos powodu zawiesza skrypt
    # print(result8.children[0].get())

    job = group([
        tasks.add.s(2, 2),
        tasks.add.s(2, 4),
        tasks.add.s(2, 5),
        tasks.add.s(2, 6),
        tasks.add.s(2, 7),
    ])

    job_result: AsyncResult = job.apply_async()

    print(job_result.successful())
    print(job_result.failed())
    print(job_result.get())

