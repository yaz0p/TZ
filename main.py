import random
import numpy as np

class FastFourierTransform:
    def __init__(self, n):
        if n < 2 or n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            raise ValueError("Число должно быть кратным 2, 3 или 5")
        self.n = n

    def forward_transform(self, signal):
        transformed_signal = np.fft.fft(signal, self.n)
        return transformed_signal

    def inverse_transform(self, signal):
        reconstructed_signal = np.fft.ifft(signal, self.n)
        return np.real(reconstructed_signal)

# Создание объекта класса ( число внутрь ставим сами, если число не кратно указаным числам, то выходит ошибка и ничего не работает :( )
# (число внутри должно быть кратным 2, 3 или 5)
fft = FastFourierTransform(10)

# Генерация случайных целых чисел от 1 до 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Сгенерированные скриптом числа",random_numbers)

# Прямое преобразование Фурье
input_signal = random_numbers
transformed_signal = fft.forward_transform(input_signal)
print("Прямое преобразование Фурье:", transformed_signal)

# Обратное преобразование Фурье
reconstructed_signal = fft.inverse_transform(transformed_signal)
print("Обратное преобразование Фурье:", reconstructed_signal)

# Вычисление ошибки (MSE)
error = np.mean(np.abs(np.array(input_signal) - np.array(reconstructed_signal))**2)
print("Ошибка при прямом и обратном преобразовании Фурье:", error)