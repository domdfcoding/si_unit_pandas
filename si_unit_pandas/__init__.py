#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __init__.py
"""
Docstring Goes Here
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Based on cyberpandas
#  https://github.com/ContinuumIO/cyberpandas
#  Copyright (c) 2018, Anaconda, Inc.
#  Licensed under the BSD 3-Clause License:
#  |
#  |  Redistribution and use in source and binary forms, with or without
#  |  modification, are permitted provided that the following conditions are met:
#  |
#  |  * Redistributions of source code must retain the above copyright notice, this
#  |    list of conditions and the following disclaimer.
#  |
#  |  * Redistributions in binary form must reproduce the above copyright notice,
#  |    this list of conditions and the following disclaimer in the documentation
#  |    and/or other materials provided with the distribution.
#  |
#  |  * Neither the name of the copyright holder nor the names of its
#  |    contributors may be used to endorse or promote products derived from
#  |    this software without specific prior written permission.
#  |
#  |  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  |  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  |  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  |  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  |  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  |  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  |  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  |  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  |  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  |  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# this package
from .base import Celsius, Fahrenheit
from .parser import to_temperature
from .temperature_array import CelsiusType, TemperatureArray

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"

__license__: str = "GNU Lesser General Public License v3 or later (LGPLv3+)"
__version__: str = "0.0.1"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = [
		'__version__',
		'TemperatureArray',
		'CelsiusType',
		'to_temperature',
		]
