# -*- coding: utf-8 -*-
"""
    {{ app_name }}.models
    ~~~~~~~~~~~~~~

    {{ app_name }} models file

    :copyright: (c) 2014 by arruda.
"""

from django.db import models


class SomeModel(models.Model):
    """
    Some model descption
    """

    class Meta:
        app_label = '{{ app_name }}'
