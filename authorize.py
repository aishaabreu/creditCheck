"""
    This is a small personal credit availability check applicatioN
"""

import json


class ViolationsChecker:
    """
        Manages checks violations
    """

    # Validations Variables
    MIN_SCORE = 200
    MIN_INSTALLMENTS = 6
    COMPROMISED_INCOME = 0.3
    DOUBLE_TRANSACTIONS_MINUTES = 2

    # Errors MSG
    MSG_COMPROMISED_INCOME = 'compromised-income'
    MSG_LOW_SCORE = 'low-score'
    MSG_MINIMUM_INSTALLMENTS = 'minimum-installments'
    MSG_DOUBLE_TRANSACTIONS = 'doubled-transactions'
    MSG_INVALID_DATA = 'Invalid Data'

    # Data
    TRASACTION_KEY = 'transaction'

    ID_FIELD = 'id'
    CONSUMER_FIELD = 'consumer_id'
    SCORE_FIELD = 'score'
    INCOME_FIELD = 'income'
    VALUE_FIELD = 'requested_value'
    INSTALLMENTS_FIELD = 'installments'
    TIME_FIELD = 'time'
    VIOLATIONS_FIELD = 'violations'
    ERROR_FIELD = 'error'

    DATA_FIELD_SET = {
        ID_FIELD,
        CONSUMER_FIELD,
        SCORE_FIELD,
        INCOME_FIELD,
        VALUE_FIELD,
        INSTALLMENTS_FIELD,
        TIME_FIELD
    }

    def __init__(self, operations):
        self.operations = operations

    def compromised_income(self, operation):
        max_installment = operation[self.TRASACTION_KEY][self.INCOME_FIELD] * self.COMPROMISED_INCOME
        installments = operation[self.TRASACTION_KEY][self.INSTALLMENTS_FIELD]
        installment = (
            operation[self.TRASACTION_KEY][self.INSTALLMENTS_FIELD] and
            operation[self.TRASACTION_KEY][self.VALUE_FIELD] / operation[self.TRASACTION_KEY][self.INSTALLMENTS_FIELD])
        return installment > max_installment

    def low_score(self, operation):
        return operation[self.TRASACTION_KEY][self.SCORE_FIELD] < self.MIN_SCORE

    def minimum_installments(self, operation):
        return operation[self.TRASACTION_KEY][self.INSTALLMENTS_FIELD] < self.MIN_INSTALLMENTS

    def validate_doubled_transactions(self, violations):
        # TODO: Listar operacoes ordenando pelo tempo
        # Validar se tem menos de 2 minutos que da ultima transaação
        # retornar lista com ids das transações duplicadas
        return violations

    def violations(self):
        violations = []
        for operation in self.operations:
            try:
                data = {
                    self.ID_FIELD: operation[self.TRASACTION_KEY][self.ID_FIELD],
                    self.VIOLATIONS_FIELD: []
                }
                if self.low_score(operation):
                    data[self.VIOLATIONS_FIELD].append(
                        self.MSG_LOW_SCORE
                    )
                if self.compromised_income(operation):
                    data[self.VIOLATIONS_FIELD].append(
                        self.MSG_COMPROMISED_INCOME
                    )
                if self.minimum_installments(operation):
                    data[self.VIOLATIONS_FIELD].append(
                        self.MSG_MINIMUM_INSTALLMENTS
                    )
                violations.append({self.TRASACTION_KEY: data})
            except:
                violations.append({
                    self.ERROR_FIELD: self.MSG_INVALID_DATA
                })

        violations = self.validate_doubled_transactions(violations)

        return violations


class Authorizer:
    """
        Manages authorization
    """

    MSG_INVALID_JSON = 'Invalid JSON'

    def __init__(self, data):
        self._data = data

    def _from_json(self, data, decoded=None):
        """
            Run the binary looking for valid json data
        """
        decoded = decoded or []
        try:
            data = json.loads(data)
            if isinstance(data, list):
                decoded = decoded + data
            else:
                decoded.append(data)
        except json.decoder.JSONDecodeError as error:
            decoded.append(json.loads(data[:error.pos]))
            return self._from_json(data[error.pos:], decoded)
        return decoded

    @property
    def operations(self):
        try:
            return self._from_json(self._data)
        except:
            return [{'error': self.MSG_INVALID_JSON}]

    def violations(self):
        instance = ViolationsChecker(self.operations)
        return instance.violations()
