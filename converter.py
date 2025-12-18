def convert_number(number_str, from_base):
    """
    Конвертирует число из заданной системы счисления в другие
    """
    try:
        # Преобразуем строку в число в зависимости от исходной системы
        if from_base == 'dec':
            num = int(number_str)
        elif from_base == 'bin':
            num = int(number_str, 2)
        elif from_base == 'hex':
            num = int(number_str, 16)
        else:
            print("❌ Ошибка: Неизвестная система счисления!")
            print("Доступные системы: dec, bin, hex")
            return None
        
        # Конвертируем в другие системы
        results = {
            'dec': str(num),
            'bin': bin(num),
            'hex': hex(num)
        }
        
        return results
        
    except ValueError as e:
        print(f"❌ Ошибка ввода: {e}")
        print("Проверьте правильность введенного числа")
        return None
    except Exception as e:
        print(f"❌ Неизвестная ошибка: {e}")
        return None

def print_conversion_results(results, original_base):
    """
    Выводит результаты конвертации в красивом формате
    """
    print("\n" + "="*50)
    print("📊 РЕЗУЛЬТАТЫ КОНВЕРТАЦИИ:")
    print("="*50)
    
    # Убираем префиксы для более чистого вывода
    dec_value = results['dec']
    bin_value = results['bin'][2:]  # Убираем '0b'
    hex_value = results['hex'][2:]  # Убираем '0x'
    hex_value = hex_value.upper()   # Делаем буквы заглавными
    
    if original_base != 'dec':
        print(f"Десятичная (DEC): {dec_value}")
    
    if original_base != 'bin':
        print(f"Двоичная (BIN): {bin_value}")
    
    if original_base != 'hex':
        print(f"Шестнадцатеричная (HEX): {hex_value}")
    
    print("="*50)

def get_valid_input(prompt, validation_func=None):
    """
    Получает валидный ввод от пользователя
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("⚠️  Ввод не может быть пустым!")
            continue
        
        if validation_func and not validation_func(user_input):
            continue
            
        return user_input

def is_valid_base(base):
    """
    Проверяет, является ли введенная система счисления допустимой
    """
    valid_bases = ['dec', 'bin', 'hex']
    if base.lower() not in valid_bases:
        print(f"❌ Неверная система счисления! Используйте: {', '.join(valid_bases)}")
        return False
    return True

def main():
    """
    Основная функция программы
    """
    print("🔄 КОНВЕРТЕР СИСТЕМ СЧИСЛЕНИЯ")
    print("="*50)
    print("Доступные системы счисления:")
    print("- DEC (десятичная) - пример: 42")
    print("- BIN (двоичная)   - пример: 101010")
    print("- HEX (шестнадцатеричная) - пример: 2A или 2a")
    print("="*50)
    
    while True:
        try:
            # Запрашиваем число
            number_str = get_valid_input("\nВведите число: ")
            
            # Запрашиваем исходную систему счисления
            base_prompt = "Введите исходную систему (dec/bin/hex): "
            from_base = get_valid_input(base_prompt, is_valid_base).lower()
            
            # Конвертируем число
            results = convert_number(number_str, from_base)
            
            if results:
                # Выводим результаты
                print_conversion_results(results, from_base)
            
            # Спрашиваем, хочет ли пользователь продолжить
            print("\n" + "-"*30)
            choice = input("Продолжить? (да/нет): ").strip().lower()
            if choice not in ['да', 'д', 'yes', 'y']:
                print("\n👋 До свидания! Спасибо за использование конвертера!")
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Программа прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"\n❌ Произошла непредвиденная ошибка: {e}")
            print("Попробуйте еще раз...")

def run_tests():
    """
    Функция для тестирования на числах из Части 1
    """
    test_cases = [
        # (число, система, описание)
        ('42', 'dec', 'Задание 1.1: 42 из DEC'),
        ('101010', 'bin', 'Задание 1.2: 101010 из BIN'),
        ('2A', 'hex', 'Задание 1.2: 2A из HEX'),
        ('127', 'dec', 'Задание 1.1: 127 из DEC'),
        ('11111111', 'bin', 'Задание 1.2: 11111111 из BIN'),
        ('7F', 'hex', 'Задание 1.1: 7F из HEX'),
        ('256', 'dec', 'Задание 1.1: 256 из DEC'),
        ('A9', 'hex', 'Задание 1.2: A9 из HEX'),
        ('1F', 'hex', 'Задание 1.2: 1F из HEX'),
    ]
    
    print("\n🧪 ТЕСТИРОВАНИЕ НА ЧИСЛАХ ИЗ ЧАСТИ 1")
    print("="*50)
    
    for number, base, description in test_cases:
        print(f"\n{description}:")
        print(f"Входные данные: {number} ({base.upper()})")
        results = convert_number(number, base)
        if results:
            print_conversion_results(results, base)
    
    print("\n✅ Тестирование завершено!")
    print("="*50)

if __name__ == "__main__":
    # Можно запустить тесты или основной интерфейс
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        run_tests()
    else:
        main()