def calculate(operators, numbers):
    while '*' in operators or '/' in operators:
        for i in range(len(operators)):
            if operators[i] == '*':
                numbers[i] = numbers[i] * numbers.pop(i + 1)
                operators.pop(i)
                break
            elif operators[i] == '/':
                numbers[i] = numbers[i] / numbers.pop(i + 1)
                operators.pop(i)
                break

    while '+' in operators or '-' in operators:
        for i in range(len(operators)):
            if operators[i] == '+':
                numbers[i] = numbers[i] + numbers.pop(i + 1)
                operators.pop(i)
                break
            elif operators[i] == '-':
                numbers[i] = numbers[i] - numbers.pop(i + 1)
                operators.pop(i)
                break

    return numbers[0]


def main():
    numbers = []
    operators = []

    while True:
        user_input = input("Masukkan angka atau ketik 'done' jika selesai: ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.")

    while len(operators) < len(numbers) - 1:
        operator = input("Masukkan operasi aritmatika (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            operators.append(operator)
        else:
            print("Operasi tidak valid, masukkan operasi yang benar.")

    result = calculate(operators, numbers)
    print(f"Hasil dari perhitungan adalah: {result}")


if __name__ == "__main__":
    main()
