from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Simulação de um banco de dados de contas e transações
accounts_dict = {
    'user1': {'account_balance': 1000, 'password': generate_password_hash('password1')},
    'user2': {'account_balance': 500, 'password': generate_password_hash('password2')}
}

# Funções Lambda para acesso às contas e atualização de saldo
accounts = lambda: accounts_dict
update_account_balance = lambda user_id, amount_diff: accounts()[user_id].update({'account_balance': accounts()[user_id]['account_balance'] + amount_diff})

# Verifica se a senha fornecida corresponde à senha criptografada armazenada
check_password = lambda password_hash, password: check_password_hash(password_hash, password)

# Função para processar transações
payment_processing_flow = lambda user_id, transaction_id, amount, payment_type: [
    print(create_transaction(user_id, amount)[0]),
    print(cash_transaction(user_id, amount)[0]) if payment_type == 'cash' else print(credit_transaction(user_id, amount)[0]),
    print(print_payment_receipt(transaction_id)),
    print(return_payment_receipt(transaction_id)),
    print(complete_transaction(transaction_id)),
    print(close_transaction(transaction_id))
] if (payment_type == 'cash' and check_balance(user_id, amount)) or payment_type == 'credit' else [
    print(cancel_transaction(transaction_id))
]

# Verifica se o saldo é suficiente para a transação
check_balance = lambda user_id, amount: accounts()[user_id]['account_balance'] >= amount

# Rota para login
login = lambda data: (
    jsonify({'message': 'Login successful'}) if check_password(accounts_dict[data['username']]['password'], data['password']) else jsonify({'error': 'Invalid credentials'})
)

# Rota para processar transações
process_transaction = lambda data: (
    jsonify({'message': 'Transaction processed successfully'}) if payment_processing_flow(data['username'], data['transaction_id'], data['amount'], data['payment_type']) else jsonify({'error': 'Transaction processing failed'})
)

@app.route('/login', methods=['GET'])
def login_route():
    return login(request.get_json())

@app.route('/transaction', methods=['POST'])
def transaction_route():
    return process_transaction(request.get_json())

if __name__ == '__main__':
    app.run(debug=True)
