import boto3
import time


def spawn_container():
    fg = boto3.client("ecs")

    # run fargate task with preconfigured subnet and security group
    response = fg.run_task(
        cluster="cookiemonster-cluster",
        count=1,
        launchType="FARGATE",
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": [
                    "subnet-049f2a7f36aaa7e23",
                ],
                "securityGroups": [
                    "sg-0473216f490010ab8",
                ],
                "assignPublicIp": "ENABLED",
            }
        },
        taskDefinition="cookiemonster-task",
    )

    # task id from response
    task_id = response.get("tasks")[0].get("taskArn")

    # task info from task id
    task_info = fg.describe_tasks(
        cluster="cookiemonster-cluster",
        tasks=[
            task_id,
        ],
    )

    # get last status and desired status (running)
    lastStatus = task_info.get("tasks")[0].get("lastStatus")
    desiredStatus = task_info.get("desiredStatus")

    print("desiredStatus:", desiredStatus)
    print("lastStatus:", lastStatus)

    # keep checking status until container is running
    while lastStatus != desiredStatus:
        task_info = fg.describe_tasks(
            cluster="cookiemonster-cluster",
            tasks=[
                task_id,
            ],
        )
        desiredStatus = task_info.get("tasks")[0].get("desiredStatus")
        lastStatus = task_info.get("tasks")[0].get("lastStatus")
        print("desiredStatus:", desiredStatus)
        print("lastStatus:", lastStatus)
        if lastStatus != desiredStatus:
            time.sleep(5)

    # when container is running, grab eni ID for public ip
    if lastStatus == desiredStatus:
        print("container is running")
        eni_id = (
            task_info.get("tasks")[0].get("attachments")[0].get("details")[1].get("value")
        )
        eni = boto3.resource("ec2").NetworkInterface(eni_id)
        return eni.association_attribute["PublicIp"]

    # print("stopping container...")

    # stop container while testing - separate into separate function for actual use
    # stop_response = fg.stop_task(
    #     cluster="cookiemonster-cluster",
    #     task=task_id,
    # )
    # print(stop_response)
