import unittest
from authorize import Authorizer


class AuthorizerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = b"""
        { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000,
        "installments": 15, "time": "2019-02-13T10:00:00.000Z"}}
        { "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000,
        "installments": 15, "time": "2019-03-13T10:00:00.000Z"}}
        { "transaction": { "id": 3, "consumer_id": 10, "score": 500, "income": 4000, "requested_value": 10000,
        "installments": 0, "time": "2019-04-13T10:00:00.000Z"}}
        """

    def test_can_i_get_transactions_from_a_concatenated_json(self):
        instance = Authorizer(self.data)

        operations = instance.operations
        print(operations)
        self.assertEqual(len(operations), 3)
        self.assertDictEqual(operations[0], {
            'transaction': {
                'id': 1,
                'consumer_id': 10,
                'score': 600,
                'income': 4000,
                'requested_value': 10000,
                'installments': 15,
                'time': '2019-02-13T10:00:00.000Z'
            }
        })
        self.assertDictEqual(operations[-1], {
            'transaction': {
                'id': 3,
                'consumer_id': 10,
                'score': 500,
                'income': 4000,
                'requested_value': 10000,
                'installments': 0,
                'time': '2019-04-13T10:00:00.000Z'
            }
        })

    def test_can_check_transaction_is_valid(self):
        operations = b"""[{
            "transaction": {
                "id": 1,
                "consumer_id": 10,
                "score": 600,
                "income": 4000,
                "requested_value": 10000,
                "installments": 15,
                "time": "2019-02-13T10:00:00.000Z"
            }
        }]"""

        authorize = Authorizer(operations)

        self.assertEqual(
            authorize.violations(),
            [{'transaction': {'id': 1, 'violations': []}}]
        )


if __name__ == '__main__':
    unittest.main()
