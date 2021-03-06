# Copyright 2017 Open Source Robotics Foundation, Inc.
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

from argparse import Namespace
from contextlib import redirect_stderr
from io import StringIO

from ros2topic.verb.info import InfoVerb


def _generate_expected_error_output(topic_name):
    return "Unknown topic '%s'" % topic_name


def test_info_zero_publishers_subscribers():
    args = Namespace()
    args.topic_name = '/test_ros2_topic_cli'
    s = StringIO()
    with redirect_stderr(s):
        info_verb = InfoVerb()
        err_msg = info_verb.main(args=args)
        expected_output = _generate_expected_error_output(args.topic_name)
        assert expected_output == err_msg
