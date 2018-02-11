# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import boto3_wasabi

from tests import mock, unittest


class Testboto3_wasabi(unittest.TestCase):
    def setUp(self):
        self.session_patch = mock.patch('boto3_wasabi.Session', autospec=True)
        self.Session = self.session_patch.start()

    def tearDown(self):
        boto3_wasabi.DEFAULT_SESSION = None
        self.session_patch.stop()

    def test_create_default_session(self):
        session = self.Session.return_value

        boto3_wasabi.setup_default_session()

        self.assertEqual(boto3_wasabi.DEFAULT_SESSION, session,
            'Default session not created properly')

    def test_create_default_session_with_args(self):
        boto3_wasabi.setup_default_session(
            aws_access_key_id='key',
            aws_secret_access_key='secret')

        self.Session.assert_called_with(
            aws_access_key_id='key',
            aws_secret_access_key='secret')

    @mock.patch('boto3_wasabi.setup_default_session',
                wraps=boto3_wasabi.setup_default_session)
    def test_client_creates_default_session(self, setup_session):
        boto3_wasabi.DEFAULT_SESSION = None

        boto3_wasabi.client('sqs')

        self.assertTrue(setup_session.called,
            'setup_default_session not called')
        self.assertTrue(boto3_wasabi.DEFAULT_SESSION.client.called,
            'Default session client method not called')

    @mock.patch('boto3_wasabi.setup_default_session',
                wraps=boto3_wasabi.setup_default_session)
    def test_client_uses_existing_session(self, setup_session):
        boto3_wasabi.DEFAULT_SESSION = self.Session()

        boto3_wasabi.client('sqs')

        self.assertFalse(setup_session.called,
            'setup_default_session should not have been called')
        self.assertTrue(boto3_wasabi.DEFAULT_SESSION.client.called,
            'Default session client method not called')

    def test_client_passes_through_arguments(self):
        boto3_wasabi.DEFAULT_SESSION = self.Session()

        boto3_wasabi.client('sqs', region_name='us-west-2', verify=False)

        boto3_wasabi.DEFAULT_SESSION.client.assert_called_with(
            'sqs', region_name='us-west-2', verify=False)

    @mock.patch('boto3_wasabi.setup_default_session',
                wraps=boto3_wasabi.setup_default_session)
    def test_resource_creates_default_session(self, setup_session):
        boto3_wasabi.DEFAULT_SESSION = None

        boto3_wasabi.resource('sqs')

        self.assertTrue(setup_session.called,
            'setup_default_session not called')
        self.assertTrue(boto3_wasabi.DEFAULT_SESSION.resource.called,
            'Default session resource method not called')

    @mock.patch('boto3_wasabi.setup_default_session',
                wraps=boto3_wasabi.setup_default_session)
    def test_resource_uses_existing_session(self, setup_session):
        boto3_wasabi.DEFAULT_SESSION = self.Session()

        boto3_wasabi.resource('sqs')

        self.assertFalse(setup_session.called,
            'setup_default_session should not have been called')
        self.assertTrue(boto3_wasabi.DEFAULT_SESSION.resource.called,
            'Default session resource method not called')

    def test_resource_passes_through_arguments(self):
        boto3_wasabi.DEFAULT_SESSION = self.Session()

        boto3_wasabi.resource('sqs', region_name='us-west-2', verify=False)

        boto3_wasabi.DEFAULT_SESSION.resource.assert_called_with(
            'sqs', region_name='us-west-2', verify=False)
