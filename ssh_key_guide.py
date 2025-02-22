import os
import sys
import time
import shutil

# ANSI escape codes for formatting
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"

# Code block style: dark gray background with white text for contrast
CODE_BG = "\033[48;5;240m"
CODE_FG = "\033[38;5;15m"
CODE_STYLE = f"{CODE_BG}{CODE_FG}"

# Steps are formatted to be no more than 10 lines each.
steps = [
    f"""{BOLD}{CYAN}Step 1: REMOTE TEST MACHINE - Enable SSH with Password Authentication{RESET}
On the REMOTE TEST MACHINE, you need to allow SSH access using a password.
Edit the SSH configuration file:
    {CODE_STYLE}sudo nano /etc/ssh/sshd_config{RESET}
Locate the line:
    {CODE_STYLE}PasswordAuthentication yes{RESET}
Ensure it's uncommented and set to 'yes', save the file and restart SSH:
    {CODE_STYLE}sudo systemctl restart sshd{RESET}
💡 The REMOTE TEST MACHINE now allows password-based SSH connections.""",
    
    f"""{BOLD}{CYAN}Step 2: REMOTE TEST MACHINE - Ensure Sudo Rights{RESET}
Add your user to the sudo group:
    {CODE_STYLE}cd /etc/sudoers.d{RESET}
Verify sudo membership:
    {CODE_STYLE}# SUDO RULES FOR LOCAL USER{RESET}
    {CODE_STYLE}local_account_name ALL=(ALL) NOPASSWD:ALL{RESET}
Ensure the /etc/sudoers.d/local_account_name file looks like this.""",
    
    f"""{BOLD}{CYAN}Step 3: LOCALHOST SERVER - Test SSH Connection{RESET}
From the LOCALHOST SERVER, run:
    {CODE_STYLE}ssh local_account_name@192.168.4.11{RESET}
Enter your password when prompted.
A successful login confirms SSH is working.""",
    
    f"""{BOLD}{CYAN}Step 4: LOCALHOST SERVER - Generate SSH Key Pair{RESET}
On the LOCALHOST SERVER, run:
    {CODE_STYLE}ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/my_uuid_key{RESET}
This creates:
    {CODE_STYLE}~/.ssh/my_uuid_key{RESET} (private key)
    {CODE_STYLE}~/.ssh/my_uuid_key.pub{RESET} (public key)
Keep your private key secure.""",
    
    f"""{BOLD}{CYAN}Step 5: LOCALHOST SERVER - Copy SSH Key{RESET}
Run:
    {CODE_STYLE}ssh-copy-id -i ~/.ssh/my_uuid_key.pub user@remote-test-machine{RESET}
Enter your remote password.
A confirmation message indicates the key was added.""",
    
    f"""{BOLD}{CYAN}Step 6: REMOTE TEST MACHINE - Edit SSH Config{RESET}
Open the SSH config file:
    {CODE_STYLE}sudo nano /etc/ssh/sshd_config{RESET}
Comment out the password line:
    {CODE_STYLE}#PasswordAuthentication yes{RESET}
Uncomment PubkeyAuthentication:
    {CODE_STYLE}PubkeyAuthentication yes{RESET}""",
    
    f"""{BOLD}{CYAN}Step 7: REMOTE TEST MACHINE - Save & Restart SSH{RESET}
Save the file and exit.
Then run:
    {CODE_STYLE}sudo systemctl restart sshd{RESET}
Now SSH enforces key authentication.""",
    
    f"""{BOLD}{CYAN}Step 8: LOCALHOST SERVER - Test SSH Key Authentication{RESET}
From the LOCALHOST SERVER, run:
    {CODE_STYLE}ssh local_account_name@192.168.4.11{RESET}
If you log in without a password, the key is working.""",
    
    f"""{BOLD}{CYAN}Step 9: Pro Tips - Understanding ed25519 Keys{RESET}
The ed25519 public and private keypair is based on modern cryptography.
It offers strong security with smaller key sizes and faster performance.
These keys resist many types of cryptographic attacks.
Using ed25519 ensures secure, efficient SSH authentication.
You're almost done with all the steps great job so far!""",
    
    f"""{BOLD}{CYAN}Step 10: Congratulations!{RESET}
You have completed all the steps:
- Enabled SSH with password authentication on the remote machine.
- Verified sudo rights.
- Tested SSH connection using a password.
- Generated an ed25519 public and private key pair.
- Copied the key to the remote machine.
- Configured SSH for key authentication.
- Restarted SSH.
- Tested key authentication.
{GREEN}Your SSH public and private kepair is now complete! Happy Security! 🔒{RESET}"""
]

# Header function: clears the screen and prints the header at the very top.
def print_header():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""{BOLD}{CYAN}=========================================
   SSH Key Setup & OpenSSH Configuration  
========================================={RESET}
""")

# Pager function: displays the step text page by page, always starting at the top.
def pager(text):
    lines = text.splitlines()
    term_height = shutil.get_terminal_size((80, 24)).lines
    # Reserve 2 lines for header and 2 for prompt
    page_height = max(term_height - 4, 1)
    pages = [lines[i:i+page_height] for i in range(0, len(lines), page_height)]
    page_index = 0

    while page_index < len(pages):
        print_header()
        for line in pages[page_index]:
            print(line)
        if page_index < len(pages) - 1:
            prompt = f"\n{BOLD}{GREEN}Press [Enter] to scroll down: {RESET}"
            key = input(prompt)
            if key == "" or key == " ":
                page_index += 1
            else:
                page_index += 1
        else:
            prompt = f"\n{BOLD}{GREEN}Press [Enter] to go to the main menu: {RESET}"
            input(prompt)
            break

# Function to show the main menu after paging is done.
def show_menu(step):
    pager(steps[step])
    os.system("clear" if os.name == "posix" else "cls")
    print_header()
    print(f"""{BOLD}{CYAN}
-----------------------------------------
 Menu:
-----------------------------------------{RESET}
1️⃣  {BOLD}Start from the Beginning{RESET}
2️⃣  {BOLD}Next Step{RESET}
3️⃣  {BOLD}Previous Step{RESET}
4️⃣  {BOLD}Exit Program{RESET}
""")

# Main loop to handle user interaction.
def main():
    step = 0
    while True:
        show_menu(step)
        choice = input(f"{BOLD}{GREEN}Select an option (1-4): {RESET}").strip()
        if choice == "1":
            step = 0
        elif choice == "2":
            if step < len(steps) - 1:
                step += 1
            else:
                print(f"{YELLOW}⚠️  You are already at the last step.{RESET}")
                time.sleep(1.5)
        elif choice == "3":
            if step > 0:
                step -= 1
            else:
                print(f"{YELLOW}⚠️  You are already at the first step.{RESET}")
                time.sleep(1.5)
        elif choice == "4":
            print(f"\n{BOLD}{GREEN}✅ Exiting the program. Happy Security! 🔒{RESET}\n")
            sys.exit()
        else:
            print(f"{YELLOW}⚠️  Invalid selection. Please choose 1-4.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
