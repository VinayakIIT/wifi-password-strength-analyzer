from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

COMMON_PASSWORDS = {
    'password', '123456', '12345678', '1234', 'qwerty',
    '12345', 'letmein', 'welcome', 'admin', 'wifi'
}

SEQUENTIAL_PATTERNS = [
    '123', '234', '345', '456', '567', '678', '789',
    'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij',
    '321', '432', '543', '654', '765', '876', '987',
    'cba', 'dcb', 'edc', 'fed', 'gfe', 'hgf', 'ihg', 'jih'
]

def has_upper(password):
    return any(c.isupper() for c in password)

def has_lower(password):
    return any(c.islower() for c in password)

def has_number(password):
    return any(c.isdigit() for c in password)

def has_special(password):
    return any(not c.isalnum() for c in password)

def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def check_sequential_chars(password):
    lowered = password.lower()
    return any(pattern in lowered for pattern in SEQUENTIAL_PATTERNS)

def check_repeated_chars(password):
    length = len(password)
    for i in range(length - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    return False

def get_char_set_size(password):
    size = 0
    if any(c.islower() for c in password):
        size += 26
    if any(c.isupper() for c in password):
        size += 26
    if any(c.isdigit() for c in password):
        size += 10
    if any(not c.isalnum() for c in password):
        size += 32  # Approximate count of symbols
    return size

def calculate_entropy(password):
    size = get_char_set_size(password)
    if size == 0:
        return 0
    return len(password) * math.log2(size)

def calculate_strength_score(analysis):
    score = 0
    length = analysis['length']
    entropy = analysis['entropy']
    is_common = analysis['isCommon']
    has_sequential = analysis['hasSequential']
    has_repeated = analysis['hasRepeated']
    has_upper = analysis['hasUpper']
    has_lower = analysis['hasLower']
    has_number = analysis['hasNumber']
    has_special = analysis['hasSpecial']

    score += min(30, length * 2.5)

    variety_score = 0
    variety_score += 7.5 if has_upper else 0
    variety_score += 7.5 if has_lower else 0
    variety_score += 7.5 if has_number else 0
    variety_score += 7.5 if has_special else 0
    score += variety_score

    score += min(20, entropy / 2)

    deduction = 0
    deduction += 10 if is_common else 0
    deduction += 6 if has_sequential else 0
    deduction += 4 if has_repeated else 0

    score = max(0, score - deduction)
    return min(100, score)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')
    if not password:
        return jsonify({'error': 'No password provided'}), 400

    analysis = {
        'length': len(password),
        'hasUpper': has_upper(password),
        'hasLower': has_lower(password),
        'hasNumber': has_number(password),
        'hasSpecial': has_special(password),
        'isCommon': check_common_password(password),
        'hasSequential': check_sequential_chars(password),
        'hasRepeated': check_repeated_chars(password),
    }
    analysis['entropy'] = calculate_entropy(password)
    analysis['score'] = calculate_strength_score(analysis)

    return jsonify(analysis)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
