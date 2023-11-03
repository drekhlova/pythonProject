N = 10
sum = 0
for i in range(1, N + 1):
    sum += i
print("Сумма чисел от 1 до", N, "равна", sum)

numbers = [4, 2, 7, 1, 9, 3]
sorted_numbers = []
while numbers:
    min_num = min(numbers)
    sorted_numbers.append(min_num)
    numbers.remove(min_num)
print("Отсортированный список:", sorted_numbers)

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    # Создаем двумерный массив для хранения длин НОП для подстрок str1 и str2.
    lcs_lengths = [[0] * (n + 1) for _ in range(m + 1)]

    # Заполняем массив lcs_lengths в соответствии с алгоритмом динамического программирования.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])

    # Теперь восстанавливаем саму НОП, начиная с конца массива lcs_lengths.
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif lcs_lengths[i - 1][j] > lcs_lengths[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Инвертируем список, чтобы получить НОП в правильном порядке.
    lcs = lcs[::-1]
    return "".join(lcs)

# Пример использования:
str1 = "AGGTAB"
str2 = "GXTXAYB"
result = longest_common_subsequence(str1, str2)
print("Наибольшая общая подпоследовательность:", result)


























# Задание 2
def test_find_average_typeerror():
    with pytest.raises(TypeError):
        Tasks.find_average("Not a list")

























# Задание 3
def test_person_bank_interaction():
    person = Tasks.Person(1000)
    bank = Tasks.Bank()
    person.transfer_money(500, bank)
    assert person.balance == 500
    assert bank.balance == 500

def test_person_bank_valueerror():
    with pytest.raises(ValueError):
        person = Tasks.Person(0)
        bank = Tasks.Bank()
        person.transfer_money(500, bank)




















# Задание 4
def test_transfer_with_mock():
    person = Tasks.Person(1000)
    bank_mock = Mock()  # Создаём мок-объект для банка

    person.transfer_money(500, bank_mock)
    bank_mock.receive_money.assert_called_with(500)  # Проверяем, был ли вызван метод receive_money с аргументом 500





















# Задание 5
def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        Tasks.divide(10, 0)






























# Задание 6
@pytest.mark.parametrize("a, b, expected", [
    (10, 0, 0),  # Умножение на 0
    (-1, 5, -5),  # Умножение отрицательного числа на положительное
    (3, 3, 9),  # Умножение двух положительных чисел
    (-2, -2, 4),  # Умножение двух отрицательных чисел
    (0, 0, 0)  # Умножение двух нулей
])
def test_multiply(a, b, expected):
    assert Tasks.multiply(a, b) == expected

























# Задание 7
def test_len_string():
    assert len("Geek") == 4  # Строка из 6 символов
    assert len("") == 0  # Пустая строка
    assert len(" ") == 1  # Строка из одного пробельного символа
    assert len("Hello, World!") == 13  # Строка с пробелами и знаками препинания



























# Задание 9
@pytest.mark.parametrize("test_input,expected", [(2, True), (3, True), (4, False), (16, False), (17, True), (18, False)])
def test_is_prime(test_input, expected):
    assert Tasks.is_prime(test_input) == expected
