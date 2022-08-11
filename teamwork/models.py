from django.db import models
from django.contrib.auth.models import AbstractUser
from slugify import slugify


class RoleChoice(models.TextChoices):
    worker = "Worker"
    manager = "Manager"
    admin = "Admin"


class StatusChoice(models.TextChoices):
    fired = "fired"
    in_team = "in_team"
    bench = "bench"


class TaskChoice(models.TextChoices):
    backlog = "Backlog"
    ready_to_dev = "Ready to Dev"
    in_progress = "In progress"
    ready_to_qa = "Ready to QA"
    production = "Production"


class User(AbstractUser):
    role = models.CharField(max_length=15, choices=RoleChoice.choices)
    status = models.CharField(
        max_length=15, choices=StatusChoice.choices, default=StatusChoice.bench
    )
    team = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, null=True, related_name="employers"
    )
    slug = models.SlugField(editable=False, default="", blank=True, null=True)

    def set_status(self):
        status = {
            True: StatusChoice.in_team,
            False: StatusChoice.bench,
        }
        if self.status == StatusChoice.fired:
            self.team = None
            return
        self.status = status[bool(self.team)]

    @property
    def count_tasks(self):
        return self.assigned_task.count()

    def generate_slug(self):
        if not self.slug:
            self.slug = slugify.slugify(self.username)

    def save(self, *args, **kwargs):
        self.set_status()
        self.generate_slug()
        return super().save(*args, **kwargs)


class Team(models.Model):
    name = models.CharField(max_length=50)
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="manager",
        limit_choices_to={"role": RoleChoice.manager, "status": StatusChoice},
    )

    @property
    def employers_count(self):
        return self.employers.count()


class Task(models.Model):
    name = models.CharField(max_length=30)
    # description = models.TextField()
    # deadline = models.DateTimeField(null=True, blank=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    assigned_task = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="assigned_task"
    )
    status = models.CharField(max_length=15, choices=TaskChoice.choices)
    creator = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        max_length=15,
        limit_choices_to={"role": (RoleChoice.manager, RoleChoice.admin)},
    )


class Images(models.Model):
    image = models.ImageField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
