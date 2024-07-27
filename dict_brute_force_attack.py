import hashlib
import time

def generate_sha1_hash(plaintext):
    encoded_plaintext = plaintext.encode('utf-8')
    sha1_hash = hashlib.sha1()
    sha1_hash.update(encoded_plaintext)
    hashed_plaintext = sha1_hash.hexdigest()
    return hashed_plaintext 

def read_passwords(file_path):
    with open(file_path, 'r') as file:
        dict_pass = file.readlines()
    return dict_pass

def main():
    hashed_text = input("\n\nEnter the Hashed Password: ")
    file_path = input("Enter the file path: ") 
    try:
        password_list = read_passwords(file_path)
    except FileNotFoundError:
        print("File not found or path is incorrect.")
        return

    attempts = 0 
    start_time = time.time()
    for guess in password_list:
        hashed_guess = generate_sha1_hash(guess.strip())
        attempts += 1
        if hashed_text == hashed_guess:
            end_time = time.time()
            time_op = round((end_time - start_time), 4)
            print(f"\n\nStatus --------: Cracked")
            print(f"Hashed password: {hashed_text}")
            print(f"The password---: {guess.strip()}", end ='\n')
            print(f"Time spent-----: {time_op}sec")
            print(f"Attempts-------: {attempts}\n\n")
            return

    print("Password not found in the provided list.")

main()
