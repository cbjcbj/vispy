# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
"""
Provides functionality for composing shaders from multiple GLSL
code snippets.
"""

__all__ = ['ModularProgram', 'Function', 'MainFunction', 'Variable', 'Varying',
           'FunctionChain', 'Compiler']

from .program import ModularProgram  # noqa
from .function import Function, MainFunction, FunctionChain  # noqa
from .function import StatementList  # noqa
from .variable import Variable, Varying  # noqa
from .compiler import Compiler  # noqa
