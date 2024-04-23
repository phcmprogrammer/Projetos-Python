# Variáveis globais simulando um banco de dados de contas e transações
accounts_dict = {
    'user1': {'account_balance': 1000, 'password': 'hashed_password1'},
    'user2': {'account_balance': 500, 'password': 'hashed_password2'}
}
accounts = lambda: accounts_dict

# Funções de ação simulando os fluxos do diagrama UML
create_transaction = lambda user_id, amount: (f"Transaction created for user {user_id} for the amount of {amount}", True)

update_account_balance = lambda user_id, amount_diff: (
    lambda: accounts()[user_id].update({'account_balance': accounts()[user_id]['account_balance'] + amount_diff})
)

check_balance = lambda user_id, amount: accounts()[user_id]['account_balance'] >= amount

cash_transaction = lambda user_id, amount: (
    (f"Cash payment of {amount} for user {user_id} successful.", update_account_balance(user_id, -amount)())
    if check_balance(user_id, amount) else
    (f"Insufficient balance for cash payment for user {user_id}.", False)
)

credit_transaction = lambda user_id, amount: (f"Credit payment of {amount} for user {user_id} processed.", True)

fund_transfer = lambda from_user, to_user, amount: (
    update_account_balance(from_user, -amount)(),
    update_account_balance(to_user, amount)(),
    "Fund transfer completed"
) if check_balance(from_user, amount) else (f"Insufficient funds in {from_user}'s account for transfer.", False)

print_payment_receipt = lambda transaction_id: f"Payment receipt printed for transaction: {transaction_id}"

return_payment_receipt = lambda transaction_id: f"Payment receipt returned for transaction: {transaction_id}"

complete_transaction = lambda transaction_id: f"Transaction {transaction_id} completed successfully."

close_transaction = lambda transaction_id: f"Transaction {transaction_id} closed."

cancel_transaction = lambda transaction_id: f"Transaction {transaction_id} cancelled."

# Função para processar transações
payment_processing_flow = lambda user_id, transaction_id, amount, payment_type: [
    print(create_transaction(user_id, amount)[0]),
    print(fund_transfer(user_id, 'user2', amount) if payment_type == 'credit' else None),
    print(cash_transaction(user_id, amount)[0]) if payment_type == 'cash' else None,
    print(credit_transaction(user_id, amount)[0]) if payment_type == 'credit' else None,
    print(print_payment_receipt(transaction_id)),
    print(return_payment_receipt(transaction_id)),
    print(complete_transaction(transaction_id)),
    print(close_transaction(transaction_id))
] if (payment_type == 'cash' and check_balance(user_id, amount)) or payment_type == 'credit' else [
    print(cancel_transaction(transaction_id))
]

# Testando os fluxos de pagamento e transações bancárias

payment_processing_flow('user1', 'tx123', 1100, 'cash')  # Falha
payment_processing_flow('user2', 'tx124', 300, 'credit')  # Sucesso

# Verifica e exibe os saldos iniciais de user1 e user2
print("Initial Balances:")
print(f"User1: {accounts()['user1']['account_balance']}")
print(f"User2: {accounts()['user2']['account_balance']}")

# Executa uma transferência de fundos de user1 para user2
transaction_id = 'tx125'
amount_to_transfer = 300  # Define a quantidade a ser transferida

# Verifica se 'user1' tem fundos suficientes e, em caso afirmativo, realiza a transferência como parte de uma operação de crédito
if check_balance('user1', amount_to_transfer):
    # Inicia uma transação de crédito e realiza a transferência
    print("\nProcessing credit transaction with fund transfer...")
    payment_processing_flow('user1', transaction_id, amount_to_transfer, 'credit')
else:
    print("\nUser1 does not have sufficient funds for this transfer.")
    print(cancel_transaction(transaction_id))

# Exibe os saldos após a transferência
print("\nBalances after Transfer:")
print(f"User1: {accounts()['user1']['account_balance']}")
print(f"User2: {accounts()['user2']['account_balance']}")
