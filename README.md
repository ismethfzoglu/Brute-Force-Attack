Password Hash Cracking Scripts
This repository contains three Python scripts for cracking SHA-1 hashed passwords using different methods. Each script demonstrates a different approach to attempt to recover the original password from its hash.

Table of Contents
  * Getting Started
  * Script 1: Dictionary Attack
  * Script 2: Brute Force Attack with Alphanumeric Characters
  * Script 3: Brute Force Attack with Numeric Characters
  * Requirements
  * Usage
  * 
Getting Started
To run these scripts, ensure you have Python 3 installed on your machine. You can download Python from python.org.

Script 1: Dictionary Attack
This script attempts to crack a SHA-1 hashed password using a dictionary attack. It reads a list of possible passwords from a file and hashes each one to check against the target hash.

How it works
  1. The user is prompted to input the hashed password.
  2. The user provides the file path to a dictionary file containing potential passwords.
  3. The script reads the file and hashes each password.
  4. If a hash matches the input hash, the script outputs the original password.

Script 2: Brute Force Attack with Alphanumeric Characters
This script attempts to crack a SHA-1 hashed password using a brute force attack with all possible alphanumeric characters.

How it works
  1. The user is prompted to input the hashed password.
  2. The script generates all possible alphanumeric passwords of lengths 4 to 8.
  3. Each generated password is hashed and compared to the input hash.
  4. If a hash matches, the script outputs the original password.

Script 3: Brute Force Attack with Numeric Characters
This script attempts to crack a SHA-1 hashed password using a brute force attack with numeric characters only.

How it works
  1. The user is prompted to input the hashed password.
  2. The script generates all possible numeric passwords of lengths 4 to 8.
  3. Each generated password is hashed and compared to the input hash.
  4. If a hash matches, the script outputs the original password.


Requirements
  * Python 3.x

Usage
  * Clone this repository to your local machine.
  * Run the desired script using Python:
    * python script_name.py
  * Follow the prompts to input the hashed password and, if required, the path to a dictionary file.
