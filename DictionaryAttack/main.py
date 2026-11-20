import hashlib
import time
import os

PASSWORD_FILE = "passwords.txt"

ALGORITHMS = {
    "1": "md5",
    "2": "sha1",
    "3": "sha256",
    "4": "sha384",
    "5": "sha512"
}


def load_passwords():

    if not os.path.exists(PASSWORD_FILE):
        print("\n[!] Файлът passwords.txt не е намерен!")
        return []

    with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
        passwords = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return passwords


def calculate_hash(password, algorithm):


    password_bytes = password.encode("utf-8")
    return hashlib.new(algorithm, password_bytes).hexdigest()


def dictionary_attack(passwords, target_hash, algorithm):


    start_time = time.perf_counter()

    for password in passwords:
        calculated_hash = calculate_hash(password, algorithm)

        if calculated_hash.lower() == target_hash.lower():
            elapsed_time = time.perf_counter() - start_time

            print("\n[+] УСПЕШНО СЪВПАДЕНИЕ!")
            print(f"Намерена парола: {password}")
            print(f"Използван алгоритъм: {algorithm.upper()}")
            print(f"Време за търсене: {elapsed_time:.8f} секунди")
            print(f"Проверени пароли: {passwords.index(password) + 1}")

            return

    elapsed_time = time.perf_counter() - start_time

    print("\n[-] Не е открито съвпадение.")
    print(f"Използван алгоритъм: {algorithm.upper()}")
    print(f"Проверени пароли: {len(passwords)}")
    print(f"Време за търсене: {elapsed_time:.8f} секунди")


def main():

    print("=" * 45)
    print("       DICTIONARY ATTACK SIMULATOR")
    print("=" * 45)

    passwords = load_passwords()

    if not passwords:
        print("Речникът е празен или не може да бъде зареден.")
        return

    print(f"\nЗаредени пароли: {len(passwords)}")

    while True:
        print("\nИзбери хеш алгоритъм:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. SHA-384")
        print("5. SHA-512")

        choice = input("\nТвоят избор: ").strip()


        if choice not in ALGORITHMS:
            print("\n[!] Невалиден избор!")
            continue

        algorithm = ALGORITHMS[choice]

        print(f"\nИзбран алгоритъм: {algorithm.upper()}")

        target_hash = input(
            "Въведи хеш стойността за проверка: "
        ).strip()

        if not target_hash:
            print("[!] Не е въведена хеш стойност!")
            continue

        dictionary_attack(passwords, target_hash, algorithm)
        break


if __name__ == "__main__":
    main()
