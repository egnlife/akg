# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""asin test case"""

import os
import pytest
from base import TestBase
from nose.plugins.attrib import attr
from test_run.asin_run import asin_run


class TestCase(TestBase):

    def setup(self):
        case_name = "test_akg_asin_001"
        case_path = os.getcwd()
        self.params_init(case_name, case_path)
        self.caseresult = True
        self._log.info("======================== %s Setup case=================", self.casename)
        self.testarg = [
            ("asin_001", asin_run, ((16, 16), "float16")),
            ("asin_002", asin_run, ((16, 16), "float32")),
        ]
        return

    @pytest.mark.rpc_mini
    @pytest.mark.level1
    @pytest.mark.env_onecard
    @pytest.mark.platform_x86_ascend_training
    def test_run(self):
        self.common_run(self.testarg)

    @pytest.mark.rpc_cloud
    @pytest.mark.env_onecard
    @pytest.mark.platform_x86_ascend_training
    def test_cloud_run(self):
        self.common_run(self.testarg)

    def teardown(self):
        self._log.info("============= %s Teardown============", self.casename)
        return