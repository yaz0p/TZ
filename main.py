import random
import math

class FastFourierTransform:
    def __init__(self, n):
        if n < 2 or n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            raise ValueError("Число должно быть кратным 2, 3 или 5")
        self.n = n

    def dft(self, x):
        # Определяем длинну входного сигнала
        N = len(x)
        # Создаем пустой список который будет содержать результат преобразования фурье
        X = []
        # Создаем цикл
        for n in range(N):
            # Вещественная часть амплитуды
            real_part = 0
            # Мнимая часть амплитуды
            imag_part = 0
            for k in range(N):
                # Вычисление угла для текущей частоты
                angle = 2 * math.pi * k * n / N
                # Вещественная часть амплитуды
                real_part += x[k] * math.cos(angle)
                # Мнимая часть амплитуды
                imag_part -= x[k] * math.sin(angle)
            #   Создание комплексного числа на основе мнимой и реальной части
            X.append(complex(real_part, imag_part))
        return X

    def idft(self, X):
        # Определяем длинну входного сигнала
        N = len(X)
        # Создаем пустой список который будет содержать результат обратного преобразования фурье
        x = []
        for n in range(N):
            # Вещественная часть амплитуды
            real_part = 0
            # Мнимая часть амплитуды
            imag_part = 0
            for k in range(N):
                # Вычисление угла
                angle = 2 * math.pi * k * n / N
                # Вычисление вещественной части
                real_part += X[k].real * math.cos(angle) - X[k].imag * math.sin(angle)
                # Вычисление вещественной части
                imag_part += X[k].real * math.sin(angle) + X[k].imag * math.cos(angle)
            #     Вычисление чисел обратное преобразование
            x.append(real_part / N)
        return x

    def calculate_mse(self, input_signal, reconstructed_signal):
        # Определение длины входного сигнала
        N = len(input_signal)
        squared_error = 0
        # Создание цикла
        for i in range(N):
            # Вычисление квадратичной ошибки
            squared_error += (input_signal[i] - reconstructed_signal[i]) ** 2
        mse = squared_error / N
        return mse


# Создание объекта класса ( число внутрь ставим сами, если число не кратно указаным числам, то выходит ошибка и ничего не работает :( )
# (число внутри должно быть кратным 2, 3 или 5)
fft = FastFourierTransform(10)

# Генерация случайных целых чисел от 1 до 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Сгенерированные скриптом числа:", random_numbers)

# Прямое преобразование Фурье
input_signal = random_numbers
transformed_signal = fft.dft(input_signal)
print("Прямое преобразование Фурье:", transformed_signal)

# Обратное преобразование Фурье
reconstructed_signal = fft.idft(transformed_signal)
print("Обратное преобразование Фурье:", reconstructed_signal)

# Вычисление ошибки MSE
error = fft.calculate_mse(input_signal, reconstructed_signal)
print("Ошибка при прямом и обратном преобразовании Фурье:", error)