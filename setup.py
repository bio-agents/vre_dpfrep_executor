#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2020-2022 Barcelona Supercomputing Center (BSC), Spain
# Copyright 2020-2022 University of Naples Federico II (UNINA), Italy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setupagents
import re
import os
import sys

# In this way, we are sure we are getting
# the installer's version of the library
# not the system's one
sys.path.insert(0, os.path.dirname(__file__))

from agent import __version__ as version
from agent import __author__ as author
from agent import __license__ as license

# Populating the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

# Populating the install requirements
with open('requirements.txt') as f:
    requirements = []
    egg = re.compile(r"#[^#]*egg=([^=&]+)")
    for line in f.read().splitlines():
        m = egg.search(line)
        requirements.append(line if m is None else m.group(1))

setupagents.setup(
    name="vre_dpfrep_executor",
    version=version,
    scripts=["VRE_RUNNER.py"],
    author=author,
    author_email="username@users.noreply.github.com",
    license=license,
    description="VRE DpFrEP Executor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inab/vre_dpfrep_executor",
    packages=setupagents.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
