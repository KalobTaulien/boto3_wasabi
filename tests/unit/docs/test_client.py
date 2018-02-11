# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests.unit.docs import BaseDocsTest

from boto3_wasabi.docs.client import boto3_wasabiClientDocumenter


class Testboto3_wasabiClientDocumenter(BaseDocsTest):
    def setUp(self):
        super(Testboto3_wasabiClientDocumenter, self).setUp()
        self.client_documenter = boto3_wasabiClientDocumenter(self.client)

    def test_document_client(self):
        self.client_documenter.document_client(self.doc_structure)
        self.assert_contains_lines_in_order([
            '======',
            'Client',
            '======',
            '.. py:class:: MyService.Client',
            '  A low-level client representing AWS MyService::',
            '    import boto3_wasabi',
            '    client = boto3_wasabi.client(\'myservice\')',
            '  These are the available methods:',
            '  *   :py:meth:`~MyService.Client.can_paginate`',
            '  *   :py:meth:`~MyService.Client.get_paginator`',
            '  *   :py:meth:`~MyService.Client.get_waiter`',
            '  *   :py:meth:`~MyService.Client.sample_operation`',
            '  .. py:method:: can_paginate(operation_name)',
            '  .. py:method:: get_paginator(operation_name)',
            '  .. py:method:: get_waiter(waiter_name)',
            '  .. py:method:: sample_operation(**kwargs)',
            '    **Request Syntax**',
            '    ::',
            '      response = client.sample_operation(',
            '          Foo=\'string\'',
            '          Bar=\'string\'',
            '      )',
            '    :type Foo: string',
            '    :param Foo: Documents Foo',
            '    :type Bar: string',
            '    :param Bar: Documents Bar',
            '    :rtype: dict',
            '    :returns:',
            '      **Response Syntax**',
            '      ::',
            '        {',
            '            \'Foo\': \'string\'',
            '            \'Bar\': \'string\'',

            '        }',
            '      **Response Structure**',
            '      - *(dict) --*',
            '        - **Foo** *(string) --*',
            '        - **Bar** *(string) --*'

        ])
