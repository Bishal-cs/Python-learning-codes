import time
import random
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Clear the screen to make it look fresh
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fake Data ID generator (just random numbers with some characters)
def generate_data_id():
    return f"{random.randint(1000, 9999)}-{random.choice(['A', 'B', 'C', 'D', 'E'])}{random.randint(1000, 9999)}"

# Fake encrypted data (random alphanumeric strings)
def generate_encrypted_data():
    return ''.join(random.choices('0123456789ABCDEF', k=16))

# Simulate hacking with random data streams and errors
def simulate_hack():
    clear_screen()
    for _ in range(100):
        data_id = generate_data_id()
        encrypted_data = generate_encrypted_data()
        
        # Random colors for the "hacked" effect
        color = random.choice([Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA])
        
        # Random choice for displaying normal data or "CRASHING" data
        if random.random() > 0.7:
            print(Back.RED + color + f"ERROR! Data ID {data_id} compromised!" + Style.RESET_ALL)
        else:
            print(color + f"Data ID: {data_id} | Encrypted Data: {encrypted_data}")
        
        # Random sleep for hacking effect
        time.sleep(random.uniform(0.01, 0.05))
        
        # Random screen flashes
        if random.random() > 0.95:
            clear_screen()

    # At the end, simulate a system crash
    for _ in range(10):
        print(Back.RED + Fore.WHITE + "SYSTEM CRASHING... DATA LOSS IMMINENT!" + Style.RESET_ALL)
        time.sleep(0.5)
        clear_screen()
        time.sleep(0.5)

# Run the hacking simulation
simulate_hack()