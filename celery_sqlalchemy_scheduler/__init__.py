# coding=utf-8
# flake8:noqa


SCHEMA_NAME = "public"

def config(schema_name):
    """Set the configuration for the package."""

    global SCHEMA_NAME
    SCHEMA_NAME = schema_name

    from .session import SessionManager
    from .models import (
        PeriodicTask, PeriodicTaskChanged,
        CrontabSchedule, IntervalSchedule,
        SolarSchedule,
    )
    from .schedulers import DatabaseScheduler
