import time
import random
import sys

def type(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start(username):
    print(f"Initializing HackTerminal v1.0 for {username}...\n")
    time.sleep(1)
    
    commands = [
        "Scanning for open ports for...",
        "Bypassing firewall...",
        "Injecting payload...",
        f"Ping 127.0.0.1 — success for {username}",
        "Elevating privileges...",
        "Compiling exploit...",
        f"Access granted. Welcome, Agent {username}."
    ]
    
    for command in commands:
        type(command)
        time.sleep(random.uniform(0.5, 1.2))

def main():
    username = input("Enter your name: ")
    start(username)

if __name__ == "__main__":
    main()