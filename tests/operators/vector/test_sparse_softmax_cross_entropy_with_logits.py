# Copyright 2019 Huawei Technologies Co., Ltd
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

"""
################################################

Testcase_PrepareCondition:

Testcase_TestSteps:

Testcase_ExpectedResult:

"""

import os

from base import TestBase
import pytest
from test_run.sparse_softmax_cross_entropy_with_logits_run import sparse_softmax_cross_entropy_with_logits_run


############################################################
# TestCase= class: put to tests/*/
############################################################
class TestCase(TestBase):
    def setup(self):
        case_name = "test_akg_sparse_softmax_cross_entropy_with_logits_001"
        case_path = os.getcwd()

        # params init
        self.params_init(case_name, case_path)

        self.caseresult = True
        self._log.info("============= {0} Setup case============".format(self.casename))
        self.testarg = [
            ## testflag,opfuncname,testRunArgs, dimArgs
            ("sparse_softmax_cross_entropy_with_logits_02", sparse_softmax_cross_entropy_with_logits_run, [(16,), "int32", (16, 16), "float16", "none", "sparse_softmax_cross_entropy_with_logits_fp16"]),
            ("sparse_softmax_cross_entropy_with_logits_03", sparse_softmax_cross_entropy_with_logits_run, [(16,), "int32", (16, 16), "float16", "sum", "sparse_softmax_cross_entropy_with_logits_fp16"]),
            ("sparse_softmax_cross_entropy_with_logits_04", sparse_softmax_cross_entropy_with_logits_run, [(32,), "int32", (32, 1001), "float16", "mean", "sparse_softmax_cross_entropy_with_logits_fp16"]),
            ("sparse_softmax_cross_entropy_with_logits_05", sparse_softmax_cross_entropy_with_logits_run, [(1,), "int32", (1, 1001), "float16", "mean", "sparse_softmax_cross_entropy_with_logits_fp16"]),
            ("sparse_softmax_cross_entropy_with_logits_06", sparse_softmax_cross_entropy_with_logits_run, [(32,), "int32", (32, 10), "float16", "mean", "sparse_softmax_cross_entropy_with_logits_fp16"]),
            ("sparse_softmax_cross_entropy_with_logits_07", sparse_softmax_cross_entropy_with_logits_run, [(751,), "int32", (751, 1), "float16", "mean", "sparse_softmax_cross_entropy_with_logits_fp16"]),
        ]
        self.testarg_cloud = [
            ## testflag,opfuncname,testRunArgs, dimArgs
            ("sparse_softmax_cross_entropy_with_logits_fp32_01", sparse_softmax_cross_entropy_with_logits_run, [(16,), "int32", (16, 16), "float32", "mean", "sparse_softmax_cross_entropy_with_logits_fp32"]),
        ]
        self.testarg_rpc_cloud = [
            ("sparse_softmax_cross_entropy_with_logits_fp32_02", sparse_softmax_cross_entropy_with_logits_run, [(32,), "int32", (32, 1001), "float32", "mean", "sparse_softmax_cross_entropy_with_logits_fp32"]),
            ("sparse_softmax_cross_entropy_with_logits_fp32_03", sparse_softmax_cross_entropy_with_logits_run, [(32,), "int32", (32, 10), "float32", "mean", "sparse_softmax_cross_entropy_with_logits_fp32"]),
            ("sparse_softmax_cross_entropy_with_logits_fp32_04", sparse_softmax_cross_entropy_with_logits_run, [(1,), "int32", (1, 1001), "float32", "mean", "sparse_softmax_cross_entropy_with_logits_fp32"]),
        ]
        return

    @pytest.mark.rpc_mini
    @pytest.mark.level0
    @pytest.mark.env_onecard
    @pytest.mark.platform_x86_ascend_training
    def test_run(self):
        """
        run case.#
        :return:
        """
        self.common_run(self.testarg)

    @pytest.mark.aicmodel
    @pytest.mark.env_onecard
    @pytest.mark.platform_x86_ascend_training
    def test_run_cloud(self):
        """
        run case.#
        :return:
        """
        self.common_run(self.testarg_cloud)

    @pytest.mark.rpc_cloud
    @pytest.mark.env_onecard
    @pytest.mark.platform_x86_ascend_training
    def test_rpc_cloud(self):
        """
        run case.#
        :return:
        """
        self.common_run(self.testarg_rpc_cloud)

    def teardown(self):
        """
        clean environment
        :return:
        """
        self._log.info("============= {0} Teardown============".format(self.casename))
        return