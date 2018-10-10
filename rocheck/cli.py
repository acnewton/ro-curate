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

import sys
import argparse
from rocheck import VERSION
from rocheck.validation import validate


def parse_arguments():
    """
    This procedure parses the program's command line arguments and returns the
    resulting `argparse` namespace.
    """
    parser = argparse.ArgumentParser(description='Validate research objects.')

    # Add arguments
    parser.add_argument(
        '--version', action='version', version=VERSION)
    parser.add_argument(
        'paths', nargs='+', help='paths to research objects to be validated')

    return parser.parse_args()


def main():
    args = parse_arguments()
    for path in args.paths:
        validate(path)


if __name__ == '__main__':
    sys.exit(main())
