from unittest import TestCase
from authorize import run_validations


class AuthorizeTestCase(TestCase):
    def test_can_check_transaction_is_valid(self):
        transactions = [{
            "transaction": {
                "id": 1,
                "consumer_id": 10,
                "score": 600,
                "income": 4000,
                "requested_value": 10000,
                "installments": 15,
                "time": "2019-02-13T10:00:00.000Z"
            }
        }]

        results = run_validations(transactions)

        self.assertEqual(
            results, [{"transaction": {"id": 1, "violations": []}}])
