# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025-07-17 22:32:37
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Base methods.
"""


from reykit.rbase import Base


__all__ = (
    'BaseWeb',
    'API'
)


class BaseWeb(Base):
    """
    Web base type.
    """


class API(BaseWeb):
    """
    External API type.
    """
