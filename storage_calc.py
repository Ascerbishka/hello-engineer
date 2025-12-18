def main():

    bytes_input = input("Введите количество байт: ").strip()
    
    try:

        bytes_value = int(bytes_input)
        
 
        if bytes_value < 0:
            bytes_value = abs(bytes_value)
            print(" Используется абсолютное значение")
        
        kilobytes = bytes_value / 1024
        megabytes = bytes_value / (1024 ** 2)
    
        dec_value = bytes_value
        bin_value = bin(bytes_value)[2:]
        hex_value = hex(bytes_value)[2:].upper() 

        print(f"\nРезультаты для {bytes_value:,} байт:")
        print(f"КБ: {kilobytes:,.3f}")
        print(f"МБ: {megabytes:,.6f}")
        print(f"DEC: {dec_value:,}")
        print(f"BIN: {bin_value}")
        print(f"HEX: {hex_value}")
        

        print(f"Биты: {bytes_value * 8:,}")
    
    
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()