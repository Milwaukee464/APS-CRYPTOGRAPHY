from cryptography.fernet import Fernet
import base64
import os


def generate_key():
    """Gera uma chave AES aleatória."""
    return Fernet.generate_key()

def encrypt_message(message, key):
    """Criptografa uma mensagem usando uma chave."""
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    """Descriptografa uma mensagem usando uma chave."""
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()

def save_key(key, filename="key.key"):
    """Salva a chave em um arquivo."""
    with open(filename, "wb") as f:
        f.write(key)

def load_key(filename="key.key"):
    """Carrega a chave de um arquivo."""
    with open(filename, "rb") as f:
        return f.read()

def clear_screen():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    print("Bem-vindo ao Crypto App!")
    
    key_filename = "key.key"

    # Verifica se a chave já existe
    if os.path.exists(key_filename):
        print("Chave encontrada.")
        key = load_key(key_filename)
    else:
        print("Chave não encontrada. Uma nova chave será gerada.")
        key = generate_key()
        save_key(key, key_filename)
        print("Nova chave gerada e salva.")

    # Menu de opções
    while True:
        print("\nSelecione uma opção:")
        print("1. Criptografar mensagem")
        print("2. Descriptografar mensagem")
        print("3. Exibir chave")
        print("4. Gerar nova chave")
        print("5. Sair")
        
        choice = input("Opção: ").strip()

        if choice == "1":
            message = input("Digite a mensagem para criptografar: ").strip()
            encrypted_message = encrypt_message(message, key)
            print("Mensagem criptografada:", base64.urlsafe_b64encode(encrypted_message).decode())
        elif choice == "2":
            encrypted_message = input("Digite a mensagem criptografada: ").strip()
            decrypted_message = decrypt_message(base64.urlsafe_b64decode(encrypted_message.encode()), key)
            print("Mensagem descriptografada:", decrypted_message)
        elif choice == "3":
            print("Chave:", key.decode())
        elif choice == "4":
            print("Gerando nova chave...")
            key = generate_key()
            save_key(key, key_filename)
            print("Nova chave gerada e salva.")
        elif choice == "5":
            print("Obrigado por usar o Crypto App!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    """Gera uma chave AES aleatória."""
    return Fernet.generate_key()

def encrypt_message(message, key):
    """Criptografa uma mensagem usando uma chave."""
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    """Descriptografa uma mensagem usando uma chave."""
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()

def save_key(key, filename="key.key"):
    """Salva a chave em um arquivo."""
    with open(filename, "wb") as f:
        f.write(key)

def load_key(filename="key.key"):
    """Carrega a chave de um arquivo."""
    with open(filename, "rb") as f:
        return f.read()

def clear_screen():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    print("Bem-vindo ao Crypto App!")
    
    key_filename = "key.key"

    # Verifica se a chave já existe
    if os.path.exists(key_filename):
        print("Chave encontrada.")
        key = load_key(key_filename)
    else:
        print("Chave não encontrada. Uma nova chave será gerada.")
        key = generate_key()
        save_key(key, key_filename)
        print("Nova chave gerada e salva.")

    # Menu de opções
    while True:
        print("\nSelecione uma opção:")
        print("1. Criptografar mensagem")
        print("2. Descriptografar mensagem")
        print("3. Exibir chave")
        print("4. Gerar nova chave")
        print("5. Sair")
        
        choice = input("Opção: ").strip()

        if choice == "1":
            message = input("Digite a mensagem para criptografar: ").strip()
            encrypted_message = encrypt_message(message, key)
            print("Mensagem criptografada:", base64.urlsafe_b64encode(encrypted_message).decode())
        elif choice == "2":
            encrypted_message = input("Digite a mensagem criptografada: ").strip()
            decrypted_message = decrypt_message(base64.urlsafe_b64decode(encrypted_message.encode()), key)
            print("Mensagem descriptografada:", decrypted_message)
        elif choice == "3":
            print("Chave:", key.decode())
        elif choice == "4":
            print("Gerando nova chave...")
            key = generate_key()
            save_key(key, key_filename)
            print("Nova chave gerada e salva.")
        elif choice == "5":
            print("Obrigado por usar o Crypto App!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
