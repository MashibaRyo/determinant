import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis

# Путь к файлу
file_path = 'C:\\Users\\User\\Downloads\\Science Hub Aurell and Gullett Drones 2024.xlsx'

# Загрузка данных из файла
data = pd.read_excel(file_path, sheet_name='Figure 8')  # Указываем лист 'Figure 8'

# Проверяем, что данные загружены корректно
print(data.head())

# Удаляем строку с единицами измерения (если она есть)
data = data.drop(data.index[0])  # Удаляем первую строку

# Выбираем данные из столбца 'Figure B and D' (начиная с 4-й строки)
signal_values = data['Figure B and D'][3:].astype(float).values  # Преобразуем в числовой формат

# Проверяем, что данные корректны
if np.isnan(signal_values).any():
    print("Ошибка: Данные содержат пропуски. Заполните их или удалите.")
else:
    # Построение графика сигнала во временной области
    plt.figure(figsize=(10, 6))
    plt.plot(signal_values, label='Сигнал во временной области', color='blue', linestyle='-')
    plt.title('График сигнала во временной области', fontsize=16)
    plt.xlabel('Отсчеты', fontsize=12)
    plt.ylabel('Значение сигнала', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Преобразование Фурье
    fft_values = np.fft.fft(signal_values)  # Быстрое преобразование Фурье
    freq = np.fft.fftfreq(len(signal_values))  # Частоты

    # Амплитудный спектр
    amplitude_spectrum = np.abs(fft_values)

    # Построение графика спектра
    plt.figure(figsize=(10, 6))
    plt.plot(freq, amplitude_spectrum, label='Спектр сигнала', color='red', linestyle='-')
    plt.title('Спектр сигнала (преобразование Фурье)', fontsize=16)
    plt.xlabel('Частота (Гц)', fontsize=12)
    plt.ylabel('Амплитуда', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Отображение графиков
    plt.tight_layout()
    plt.show()

    # Функция для извлечения признаков
    def extract_features(signal):
        # Статистические признаки
        mean_val = np.mean(signal)
        median_val = np.median(signal)
        std_val = np.std(signal)
        skewness = skew(signal)
        kurt = kurtosis(signal)

        # Частотные признаки
        freq_domain = np.fft.fft(signal)
        dominant_freq = np.argmax(np.abs(freq_domain))
        freq_variance = np.var(np.abs(freq_domain))

        # Возвращаем признаки в виде словаря
        features = {
            'mean': mean_val,
            'median': median_val,
            'std': std_val,
            'skewness': skewness,
            'kurtosis': kurt,
            'dominant_freq': dominant_freq,
            'freq_variance': freq_variance
        }
        return features

    # Извлечение признаков из сигнала
    features = extract_features(signal_values)

    # Вывод признаков
    print("Извлеченные признаки:")
    for key, value in features.items():
        print(f"{key}: {value}")