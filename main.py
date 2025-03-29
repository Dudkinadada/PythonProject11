import re
import requests

# Регулярное выражение для IPv4
IPV4_REGEX = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'


def is_valid_ipv4(ip: str) -> bool:
    """Проверяет, является ли строка корректным IPv4-адресом."""
    if re.fullmatch(IPV4_REGEX, ip):
        parts = list(map(int, ip.split('.')))
        return all(0 <= part <= 255 for part in parts)
    return False



def find_ips_in_text(text: str) -> list:
    """Находит все корректные IPv4-адреса в тексте."""
    return [ip for ip in re.findall(IPV4_REGEX, text) if is_valid_ipv4(ip)]



def find_ips_in_file(file_path: str) -> list:
    """Находит IPv4-адреса в файле."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return find_ips_in_text(text)
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь и попробуйте снова.")
        return []


def find_ips_in_url(url: str) -> list:
    """Находит IPv4-адреса на веб-странице."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return find_ips_in_text(response.text)
    except requests.RequestException:
        print("Ошибка при запросе URL. Проверьте адрес и интернет-соединение.")
        return []


def main():
    """Главное меню программы."""
    while True:
        print("\nПоиск IP-адресов")
        print("1. Ввести текст вручную")
        print("2. Загрузить файл")
        print("3. Ввести URL веб-страницы")
        print("0. Выход")

        choice = input("Выберите действие (0-3): ")

        if choice == "1":
            text = input("Введите текст: ")
            ips = find_ips_in_text(text)
            print(f"Найденные IP-адреса: {ips}" if ips else "IP-адреса не найдены.")

        elif choice == "2":
            file_path = input("Введите путь к файлу: ")
            ips = find_ips_in_file(file_path)
            print(f"Найденные IP-адреса в файле: {ips}" if ips else "В файле нет IP-адресов.")

        elif choice == "3":
            url = input("Введите URL веб-страницы: ")
            ips = find_ips_in_url(url)
            print(f"Найденные IP-адреса на странице: {ips}" if ips else "На странице нет IP-адресов.")

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
