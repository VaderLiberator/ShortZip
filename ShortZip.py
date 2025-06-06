import base64
import random
import math

def serialize(numbers):
    """
    Сериализует список целых чисел (1 ≤ num ≤ 300) в компактную ASCII-строку.
    """
    # Проверка диапазона
    for num in numbers:
        if num < 1 or num > 300:
            raise ValueError(f"Число вне диапазона (1–300): {num}")

    count = len(numbers)
    # Начинаем с 16-битного представления количества элементов
    bit_string = f"{count:016b}"
    # Записываем каждое число как 9-битное (от 0 до 299)
    for num in numbers:
        bit_string += f"{num - 1:09b}"

    # Добиваем до полного байта нулями справа
    extra_bits = (8 - len(bit_string) % 8) % 8
    bit_string += "0" * extra_bits

    # Собираем байты из битов
    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte_array.append(int(bit_string[i : i + 8], 2))

    # Кодируем полученную бинарную строку в Base64 (ASCII)
    return base64.b64encode(bytes(byte_array)).decode("ascii")

def deserialize(serialized_str):
    """
    Восстанавливает список целых чисел из ASCII-строки, полученной serialize().
    """
    # Base64 → байты
    byte_data = base64.b64decode(serialized_str)
    # Преобразуем байты в битовую строку
    bit_string = "".join(f"{byte:08b}" for byte in byte_data)

    # Первые 16 бит — количество элементов
    count = int(bit_string[:16], 2)
    numbers = []
    index = 16
    for _ in range(count):
        num_bits = bit_string[index : index + 9]
        num = int(num_bits, 2) + 1
        numbers.append(num)
        index += 9

    return numbers

# =======================
# Набор тестов
# =======================
random.seed(42)
tests = {
    "simple_short": [1, 2, 3, 10, 100],
    "random_50": [random.randint(1, 300) for _ in range(50)],
    "random_100": [random.randint(1, 300) for _ in range(100)],
    "random_500": [random.randint(1, 300) for _ in range(500)],
    "random_1000": [random.randint(1, 300) for _ in range(1000)],
    "all_1_digit": list(range(1, 10)),             # 1..9
    "all_2_digit": list(range(10, 100)),           # 10..99
    "all_3_digit": list(range(100, 301)),          # 100..300
    "each_number_x3": [num for num in range(1, 301) for _ in range(3)],  # 1..300 каждый ×3
}

# Запуск тестов и печать результатов
for name, data in tests.items():
    original_str = ",".join(str(n) for n in data)
    compressed_str = serialize(data)
    decompressed = deserialize(compressed_str)

    # Проверяем целостность (мульти-множество без учёта порядка)
    if sorted(decompressed) != sorted(data):
        status = "ОШИБКА: восстановленные данные не совпадают с исходными!"
    else:
        ratio = len(compressed_str) / len(original_str)
        status = f"Коэффициент сжатия: {ratio:.3f} ({len(compressed_str)}/{len(original_str)})"

    print(f"=== Тест: {name} ===")
    print(f"Исходная ({len(original_str)} символов): {original_str}")
    print(f"Сжатая ({len(compressed_str)} символов): {compressed_str}")
    print(status)
    print()
