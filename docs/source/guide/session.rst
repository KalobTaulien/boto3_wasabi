.. _guide_session:

Session
=======
A session manages state about a particular configuration. By default a
session is created for you when needed. However it is possible and
recommended to maintain your own session(s) in some scenarios. Sessions
typically store:

* Credentials
* Region
* Other configurations

Default Session
---------------
The ``boto3_wasabi`` module acts as a proxy to the default session, which is
created automatically when needed. Example default session use::

    # Using the default session
    sqs = boto3_wasabi.client('sqs')
    s3 = boto3_wasabi.resource('s3')

Custom Session
--------------
It is also possible to manage your own session and create clients or
resources from it::

    # Creating your own session
    session = boto3_wasabi.session.Session()

    sqs = session.client('sqs')
    s3 = session.resource('s3')
