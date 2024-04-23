import unittest

from q1_PedroCamara import *

class TestPaymentProcessing(unittest.TestCase):

    test_fund_transfer_successful = (lambda self: 
        self.assertEqual(
            accounts()['user1']['account_balance'],
            700
        )
        and self.assertEqual(
            accounts()['user2']['account_balance'],
            800
        )
    )

    test_account_balance_after_credit_transaction = (lambda self: 
        self.assertEqual(
            accounts()['user2']['account_balance'],
            800
        )
    )
    
    def test_credit_transaction(self):
        # Testa uma transação de crédito
        self.assertEqual((lambda: credit_transaction('user2', 300))(), ("Credit payment of 300 for user user2 processed.", True))
    

class TestStress(unittest.TestCase):

    test_payment_processing_stress_1 = (lambda self: 
        [payment_processing_flow('user2', f'tx{i}', 100, 'credit') for i in range(1000)]
    )

if __name__ == '__main__':
    unittest.main()
