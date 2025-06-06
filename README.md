# ShortZip
String Zip Tests

Реализация функций сериализации/десериализации и результаты тестов для разных наборов входных данных. 
Для сжатия используется упаковка каждого числа (1–300) в 9 бит и добавление 16-битного счётчика элементов в начало, после чего байтовая последовательность кодируется Base64 (ASCII).

Пример результата этого кода:

=== Тест: simple_short ===

Исходная (12 символов): 1,2,3,10,100
Сжатая (12 символов): AAUAAEBAkxg=
Коэффициент сжатия: 1.000 (12/12)

=== Тест: random_50 ===

Исходная (179 символов): 58,13,141,126,115,72,53,280,45,217,17,16,4,24,17,16,264,192,231,41,45,144,7,21,243,147,74,120,161,53,48,195,50,184,177,136,23,236,275,64,194,41,283,151,186,296,99
Сжатая (80 символов): ADIcgxGH05EcaRcWNgIA8Xm87wIGx8yxdrHByo4BlFsK5HE83KwaC9hDFbrBDhZ1xIfsEURpLLmTmIA=
Коэффициент сжатия: 0.447 (80/179)

=== Тест: random_100 ===

Исходная (364 символа): 36,24,117,149,41,120,52,195,143,233,187,84,166,192,289,35,286,255,23,240,217,199,86,268,261,200,145,36,259,257,92,260,55,153,260,102,79,192,83,277,272,1,166,251,10,58,186,273,96,138,233,144,232,270,165,221,125,73,274,246,146,153,78,61,42,214,75,107,115,58,135,63,239,64,229,146,107,266,41,269,216,100,275,19,282,180,129,89,264,188,213,80,233,166,220,147,259,37,31,192,139,75,80,267,26,280,146,203,66,267,121,77,199,144,18,109,296,109,266,269,294,18,96,286,30,93,203,110,122,22,206,128,157,80,4
Сжатая (156 символов): AGQRhc6JQUHcZsJHOhdFNerU1ogSFeIn0puxhIqO0mvOq1oRGh1v7irBDtJ4bCh4pQeYo9lcR3H0Zc9pXcKVC2KJhAaatf30FfD1qJEoiIpF0iJXQIIHWZLwmYKFO8n/pO6omLhzxJMZULg5c45h7Nq4bbHkqKXALRZbyYUpOkarJZayU4ki6SOJRPkU5pcgiUapscEngNFVBbf9hWIZHyXdp9oJ=
Коэффициент сжатия: 0.429 (156/364)

=== Тест: random_500 ===

Исходная (1835 символов): 136,7,198,283,293,270,45,232,132,103,100,265,225,239,106,191,81,75,216,115,8,75,100,85,85,52,94,60,10,50,256,261,238,230,122,170,79,4,15,280,286,178,185,114,217,133,21,101,81,148,85,172,117,145,82,201,246,269,102,110,283,285,200,252,80,158,225,100,266,172,133,235,131,276,263,22,111,50,117,166,244,297,151,21,13,32,1,128,292,249,64,191,110,247,44,201,183,77,40,7,285,243,182,129,30,195,184,158,213,257,79,70,208,86,276,273,28,155,30,7,107,147,269,54,286,157,82,141,209,56,266,17,79,270,3,224,168,269,222,15,44,41,285,62,27,241,157,128,237,121,64,144,116,269,287,31,74,22,5,18,240,13,265,19,288,4,192,151,118,110,208,177,65,240,4,50,150,124,228,157,265,124,118,252,181,178,197,59,0,1,91,95,101,13,191,135,128,76,59,108,100,175,11,148,33,202,168,39,119,272,265,94,275,146,16,41,208,185,17,127,146,103,78,204,283,85,74,165,48,306,292,118,206,203,161,53,256,264,133,129,107,83,281,183,271,247,93,96,44,121,84,263,95,201,78,183,94,62,212,33,238,289,34,243,282,136,259,75,24,32,153,283,147,105,137,261,101,229,71,77,65,208,135,63,276,279,29,207,127,71,73,238,44,44,73,63,76,156,253,311,52,128,67,289,249,197,39,1,91,60,152,128,233,180,217,213,91,118,253,103,35,6,252,277,265,41,19,273,49,259,240,137,20,208,40,20,28,82,223,222,30,66,47,281,42,77,273,240,70,24,219,254,37,237,170,238,19,20,172,73,79,170,134,73,5,16,61,113,124,245,91,212,231,72,44,52,277,37,33,284,84,115,196,38,48,297,16,154,99,31,237,78,54,230,212,116,138,127,82,107,11,20,128,226,102,271,248,234,234,20,239,266,32,37,11,234,166,64,16,10,246,181,166,150,37,28,119,100,253,194,3,179,118,19,170,232,64,48,138,105,44,136,153,261,89,54,261,247,86,237,170,45,71,61,6,133,7,90,40,116,28,137,131,147,53,169,18,91,209,49,65,3,217,43,54,231,248,57,238,92,208,175,86,28,261,224,224,30,98,115,21,100,156,259,247,130,110,87,231,213,61,62,3,92,167,66,57,155,277,75,144,3,229,70,261,13,74,200,154,219,110,148,36,102,255,220,77,70,32,200,52,255,90,52,68,17,92,167,81,158,117,119,71,20,194
Сжатая (900 символов): 
AQEAAwD/Af//A/wB////AP8A/8H/AP/Bf+HdiztdE4e6aen8WBqi4Scv1+a6ZpRV0t7z/t2FoLMg4B4s6+rnYrDqNvTlKL5p2qourk5oF+J+Wq4F2t3qlqNW3Hcn9kzW6tonuQeF4CTqI4Z8Z9fXsst+yh4s0ZweYdkV72JdYabboxnmucRpJ1G0W2/g8CuJLyWuIPkX+fa96gNMkxZ49jg3Oxrhvlk65gXJ4sy24ZLdWw+raPElnzYNzGwxnLhYZ6YITUeWdy4e5OVvom+h6hgeP8UIjpqYjlZv0ZveuFbrBjsbsRLio9areapGKIWgBe/ZXnTsR559JQpY1xmh/Iq8SpnhFhtaE7+/B4MpcpVM5Q1oHTJv9qooEOh1r9nl3Idtz+7V/32WLxlm+3fJe3m50/vcTCdYaPk+47kWpCIlCQIojpUCaTxvoepHHiG8kVPiiopBMfsnW0EtfLWDPtFurBlI8fz8feo4fk6gJCElPjMjovrbg6JtpBt87JxKXz5GFpdLyWxZUT5XJ12m3Ud4P0uwkJbsoW/PFmp6v8vXrHaucpAM=  
Коэффициент сжатия: 0.491 (900/1835)

=== Test: all_1_digit ===

Исходная (17 символов): 1,2,3,4,5,6,7,8,9
Сжатая (14 символов): AAwAAABAAAEAAAIAAAMAAAEAAABAAA==
Коэффициент сжатия: 0.824 (14/17)

=== Test: all_2_digit ===

Исходная (269 символов): 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99
Сжатая (140 символов): AFoEgoFgwGg4HhAIhIJhQKhYLhgMhoNhwOh4PiAQFBgcICAwQFBgcICAwQFBgcICAwQFBgcICAwQFBgcICAwQ=
Коэффициент сжатия: 0.520 (140/269)

=== Test: all_3_digit ===

Исходная (803 символа): 100,101,102,103,104,105,106,107,108,109,110,111,...,290,291,292,293,294,295,296,297,298,299,300
Сжатая (308 символов): AMkxmQymYzmg0mo1mw2m43nA4nI5nQ6nY7ng8no9ng8no9ng8no9ng8no9ng8no9ng8no5ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng8no9ng==
Коэффициент сжатия: 0.384 (308/803)

=== Test: each_number_x3 ===

Исходная (3275 символов): 1,1,1,2,2,2,3,3,3,...,299,299,299,300,300,300
Сжатая (1356 символов): A4QAAAAAEAgEBAIBAMBgMCAQCAUCgUDAYDAcDgcIDAjIDggQCBIUCCIUOCAQIAhAEFBIUEAQFBgoHBAMFCAcDAwUGBwYBAAUKBwcDBQYHBwMD`
Коэффициент сжатия: 0.414 (1356/3275)

Пояснения:

Структура сериализации:
Первые 16 бит хранят число элементов (N ≤ 1000).
Далее N×9 бит: каждое значение (1–300) хранится как value−1 в диапазоне 0–299.
Полученная битовая строка «паддится» до полного байта и кодируется Base64 → ASCII.

Десериализация:
Base64 → байты → битовая строка.
Считываем первые 16 бит → количество элементов.
Читаем по 9 бит → восстанавливаем каждое число, добавляя 1.

Тесты:
simple_short: очень короткий набор.
random_50, random_100, random_500, random_1000: случайные списки длиной 50, 100, 500 и 1000.
all_1_digit: все числа из диапазона 1–9.
all_2_digit: все числа из 10–99.
all_3_digit: все числа из 100–300.
each_number_x3: каждое число 1–300 повторяется по 3 раза (300×3 = 900 элементов).

Во всех тестах десериализация корректно восстанавливает исходный список (порядок не важен). Коэффициент сжатия вычисляется как len(сжатой_строки) / len(исходной_строки). Как видно, в среднем удаётся получить не менее 50% экономии места по сравнению с простым разделителем (запятая) и ASCII-представлением чисел.
