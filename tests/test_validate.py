#   Copyright 2018 Adam Cowdy
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import unittest
from rocurate import (
        validate,
        MissingManifestError,
        MissingResourceError,
    )
from . import data


class TestValidate(unittest.TestCase):
    def test_validate_for_simple_correct_bundle_succeeds(self):
        with self.assertRaises(StopIteration):
            next(validate(data.bundle('simple')))

    def test_validate_for_empty_bundle_fails(self):
        errors = validate(data.bundle('empty'))
        assert isinstance(next(errors), MissingManifestError)

    def test_validate_for_missing_remote_resource_fails(self):
        errors = validate(data.bundle('missing-remote-profile'))
        assert isinstance(next(errors), MissingResourceError)
