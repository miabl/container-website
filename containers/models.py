import time

import boto3
from django.db import models
from django.urls import reverse


class Container(models.Model):
    """A class containing information about the containers stored on AWS"""

    # Fields
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the container')
    instructions = models.TextField(max_length=1000, help_text='Enter any instructions required for the container')
    flag = models.CharField(max_length=200, blank=True)
    cluster = models.CharField(max_length=200, blank=True)
    subnet = models.CharField(max_length=200, blank=True)
    task_definition = models.CharField(max_length=200, blank=True)
    security_group = models.CharField(max_length=200, blank=True)

    def __str__(self):
        """ String for representing the container object """
        return self.name

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this container."""
        return reverse('container-detail', args=[str(self.id)])


class ContainerInstance(models.Model):
    """ A class containing information about one instance of a container"""
    container = models.ForeignKey('Container', on_delete=models.CASCADE)
    containerARN = models.CharField(max_length=2048, blank=True, null=True)
    public_ip = models.CharField(max_length=15, blank=True, null=True)

    def get_absolute_url(self):
        """ Returns the url to access a detail record of the container instance """
        return reverse('container-instance-detail', args=[str(self.id)])

    def check_status(self):
        """ Returns the desired and running status of the container instance """
        fg = boto3.client("ecs")
        # grab task info
        task_info = fg.describe_tasks(
            cluster=self.container.cluster,
            tasks=[
                self.containerARN,
            ],
        )

        # get last status and desired status
        last_status = task_info.get("tasks")[0].get("lastStatus")
        desired_status = task_info.get("tasks")[0].get("desiredStatus")

        return last_status, desired_status

    def stop_instance(self):
        fg = boto3.client("ecs")
        stop_response = fg.stop_task(
            cluster=self.container.cluster,
            task=self.containerARN,
        )

    def start_task(self):
        fg = boto3.client("ecs")

        # run fargate task with supplied subnet and security group
        res = fg.run_task(
            cluster=self.container.cluster,
            count=1,
            launchType="FARGATE",
            networkConfiguration={
                "awsvpcConfiguration": {
                    "subnets": [
                        self.container.subnet,
                    ],
                    "securityGroups": [
                        self.container.security_group,
                    ],
                    "assignPublicIp": "ENABLED",
                }
            },
            taskDefinition=self.container.task_definition,
        )
        # task ARN from response

        return res.get("tasks")[0].get("taskArn")

    def start_instance(self):
        self.start_task()
        last_status, desired_status = self.check_status()
        count = 0
        while count < 10 and last_status != desired_status:
            time.sleep(3)
            last_status, desired_status = self.check_status()
            print("DESIRED_STATUS:", desired_status)
            print("LAST_STATUS:", last_status)
            if last_status == desired_status:
                break
            count += 1
        return last_status == desired_status

    def get_ip(self):
        fg = boto3.client("ecs")
        if self.check_status()[0] == 'RUNNING':
            task_info = fg.describe_tasks(
                cluster=self.container.cluster,
                tasks=[
                    self.containerARN,
                ]
            )
            eni_id = (
                task_info.get("tasks")[0].get("attachments")[0].get("details")[1].get("value")
            )
            eni = boto3.resource("ec2").NetworkInterface(eni_id)
            return eni.association_attribute["PublicIp"]
        else:
            return
