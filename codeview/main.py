from cryptography.fernet import Fernet
import base64
import getpass
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

def save_key(key, filename):
    """Salva a chave em um arquivo."""
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename):
    """Carrega a chave de um arquivo."""
    with open(filename, "rb") as key_file:
        key = key_file.read()
    return key

def main():
    print("Bem-vindo ao Crypto App!")
    
    # Gera ou obtém a chave do usuário
    use_existing_key = input("Você já tem uma chave? (S/N): ").strip().upper()
    if use_existing_key == "S":
        key_option = input("Deseja carregar a chave de um arquivo? (S/N): ").strip().upper()
        if key_option == "S":
            key_file = input("Digite o nome do arquivo de chave: ").strip()
            if os.path.exists(key_file):
                key = load_key(key_file)
            else:
                print("Arquivo de chave não encontrado.")
                return
        else:
            key = input(getpass.getpass("Digite sua chave: ", stream=None).encode())
    else:
        key = generate_key()
        print("Sua chave gerada:", key.decode())
        save_option = input("Deseja salvar esta chave em um arquivo? (S/N): ").strip().upper()
        if save_option == "S":
            key_file = input("Digite o nome do arquivo de chave: ").strip()
            save_key(key, key_file)
            print("Chave salva com sucesso!")

    # Menu de opções
    while True:
        print("\nSelecione uma opção:")
        print("1. Criptografar mensagem")
        print("2. Descriptografar mensagem")
        print("3. Sair")
        
        choice = input("Opção: ").strip()
        
        if choice == "1":
            message = input("Digite a mensagem para criptografar: ").strip()
            encrypted_message = encrypt_message(message, key)
            print("Mensagem criptografada:", base64.urlsafe_b64encode(encrypted_message).decode())
        elif choice == "2":
            encrypted_message = input("Digite a mensagem criptografada: ").strip()
            try:
                decrypted_message = decrypt_message(base64.urlsafe_b64decode(encrypted_message.encode()), key)
                print("Mensagem descriptografada:", decrypted_message)
            except Exception as e:
                print("Erro ao descriptografar a mensagem:", e)
        elif choice == "3":
            print("Obrigado por usar o Crypto App!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()

