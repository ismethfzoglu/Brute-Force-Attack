import string
import hashlib
import time

def generate_possible_passwords():
    characters = list(string.digits + string.ascii_letters)
    

    base = len(characters)
    for length in range(4, 9):
        for i in range(base ** length):  
            result = ""
            temp_i = i
            for j in range(length):
                index = temp_i % base  
                result = characters[index] + result  
                temp_i //= base
            yield result

def generate_sha1_hash(plaintext):
    
    encoded_plaintext = plaintext.encode('utf-8')
    sha1_hash = hashlib.sha1()
    sha1_hash.update(encoded_plaintext)
    hashed_plaintext = sha1_hash.hexdigest()

    return hashed_plaintext 

def main():
    hashed_plaintext = input("\n\nEnter Your Hashed Text: ")
    attempts = 0
    start_time = time.time()
    for guess in generate_possible_passwords():
        attempts += 1
        hashed_guess = generate_sha1_hash(guess)
        print(f"Guess: {guess}, the hash of the guess: {hashed_guess},  number of Attempts {attempts}")
        if hashed_plaintext == hashed_guess:
            end_time = time.time()
            time_op = round((end_time - start_time), 4)
            print("\n\n--------------------------------------------------------------------------")
            print(f"Status --------: Cracked")
            print(f"Hashed password: {hashed_plaintext}")
            print(f"The password---: {guess}")
            print(f"Time spent-----: {time_op}sec")
            print(f"Attempts-------: {attempts}")
            print("--------------------------------------------------------------------------\n\n")
            return

main()

