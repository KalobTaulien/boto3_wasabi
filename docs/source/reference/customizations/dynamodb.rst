.. _ref_custom_dynamodb:

================================
DynamoDB Customization Reference
================================

.. _ref_valid_dynamodb_types:

Valid DynamoDB Types
--------------------

These are the valid item types to use with boto3_wasabi Table Resource (:py:class:`dynamodb.Table`) and DynamoDB:

+----------------------------------------------+-----------------------------+
| Python Type                                  | DynamoDB Type               |
+==============================================+=============================+
| string                                       | String (S)                  |
+----------------------------------------------+-----------------------------+
| integer                                      | Number (N)                  |
+----------------------------------------------+-----------------------------+
| :py:class:`decimal.Decimal`                  | Number (N)                  |
+----------------------------------------------+-----------------------------+
| :py:class:`boto3_wasabi.dynamodb.types.Binary`      | Binary (B)                  |
+----------------------------------------------+-----------------------------+
| boolean                                      | Boolean (BOOL)              |
+----------------------------------------------+-----------------------------+
| ``None``                                     | Null (NULL)                 |
+----------------------------------------------+-----------------------------+
| string set                                   | String Set (SS)             |
+----------------------------------------------+-----------------------------+
| integer set                                  | Number Set (NS)             |
+----------------------------------------------+-----------------------------+
| :py:class:`decimal.Decimal` set              | Number Set (NS)             |
+----------------------------------------------+-----------------------------+
| :py:class:`boto3_wasabi.dynamodb.types.Binary` set  | Binary Set (BS)             |
+----------------------------------------------+-----------------------------+
| list                                         | List (L)                    |
+----------------------------------------------+-----------------------------+
| dict                                         | Map (M)                     |
+----------------------------------------------+-----------------------------+


Custom boto3_wasabi Types
------------------


.. autoclass:: boto3_wasabi.dynamodb.types.Binary
   :members:
   :undoc-members:

.. _ref_dynamodb_conditions:

DynamoDB Conditions
-------------------

.. autoclass:: boto3_wasabi.dynamodb.conditions.Key
   :members:
   :undoc-members:
   :inherited-members:

.. autoclass:: boto3_wasabi.dynamodb.conditions.Attr
   :members:
   :undoc-members:
   :inherited-members:
