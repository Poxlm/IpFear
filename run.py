import requests
import sys
import threading
import time
import json
import emoji
from colorama import init, Fore

# Initialize colorama for colored output
init(autoreset=True)

menu_options = {
    1: "Get IP information",
    2: "Exit"
}

def print_menu():
    print_colored_text("╔════════════════════════════════╗", Fore.CYAN)
    print_colored_text("║    🌐 PoxlM Dtool - IpSpy 🕵️    ║", Fore.CYAN)
    print_colored_text("╚════════════════════════════════╝", Fore.CYAN)
    for key in menu_options.keys():
        print(f"{key} -- {menu_options[key]}")

def get_ip_info(ip):
    url = f'http://api.ipapi.com/{ip}?access_key=257f87ecd464099ce0faa6db1cde5516&format=1'
    response = requests.get(url)
    data = response.json()
    return data

def print_colored_text(text, color):
    print(f"{color}{text}")

def print_ip_info(ip_address):
    location_data = get_ip_info(ip_address)
    print_colored_text("🌐 IP Information:", Fore.CYAN)
    print_colored_text(f"IP: {location_data['ip']}", Fore.YELLOW)
    print_colored_text(f"🏰 Capital: {location_data['location']['capital']}", Fore.GREEN)
    print_colored_text(f"🌍 Region: {location_data['region_name']}", Fore.GREEN)
    print_colored_text(f"🌎 Country: {location_data['country_name']}", Fore.GREEN)
    print_colored_text(f"📬 Postal Code: {location_data['zip']}", Fore.GREEN)
    print_colored_text(f"🌐 Latitude: {location_data['latitude']}", Fore.GREEN)
    print_colored_text(f"🌐 Longitude: {location_data['longitude']}", Fore.GREEN)
    print_colored_text(f"🚩 Country Flag Emoji: {location_data['location']['country_flag_emoji']}", Fore.BLUE)
    print_colored_text(f"🗣️ Language: {', '.join([lang['name'] for lang in location_data['location']['languages']])}", Fore.BLUE)
    print_colored_text(f"📞 Calling Code: {location_data['location']['calling_code']}", Fore.BLUE)
    print_colored_text(f"📍 Zip Code: {location_data['region_code']}", Fore.BLUE)
    print_colored_text(f"🌏 Continent Code: {location_data['continent_code']}", Fore.BLUE)
    print_colored_text(f"🌍 Continent Name: {location_data['continent_name']}", Fore.BLUE)

    save_choice = input("Do you want to save these details in a JSON file? (yes/no): ").lower()
    if save_choice == 'yes':
        t = threading.Thread(target=animate_loading)
        t.start()
        save_to_json(location_data)
        t.join()

def save_to_json(data):
    with open('ip_info.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print_colored_text("IP information saved to ip_info.json 📁", Fore.GREEN)

def exit_program():
    print_colored_text("Goodbye 👋", Fore.YELLOW)
    sys.exit()

def animate_loading():
    chars = ["|", "/", "-", "\\"]
    i = 0
    while True:
        print_colored_text("Loading " + chars[i], Fore.YELLOW)
        i = (i + 1) % len(chars)
        time.sleep(0.1)
        print("\033[F", end="")  # Move cursor up one line
        if i == 0:  # Stop loading animation after one cycle
            break

while True:
    print_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ip_address = input("Enter the IP address: ")
        t = threading.Thread(target=animate_loading)
        t.start()
        print_ip_info(ip_address)
        t.join()
    elif choice == 2:
        exit_program()
    else:
        print_colored_text("Invalid choice. Please enter a number between 1 and 2. 🤨", Fore.RED)
 
