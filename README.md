# Public and Private Keypairs: A Secure SSH Key Setup Guide

This guide provides 10 steps to set up SSH key authentication using an ed25519 public and private key pair. It is helpful for end-users who favor reading the work instructions in plain text instead of running the Python3 program.

---

**Announcement:**

This guide assumes that the remote machine uses the username `local_account_name` and the IP address `192.168.4.11`. Please adjust these values to match your user account name and IP address so the steps work.

---

**Startup Requirements:**

If you are running Ubuntu linux please install these packages:
```bash
sudo apt update && sudo apt install git vim openssh-server
```



## Step 1: REMOTE TEST MACHINE = Enable SSH with Password Authentication
Allow SSH access using a password on the REMOTE TEST MACHINE.

---
Edit the SSH configuration file:
```bash
sudo vim /etc/ssh/sshd_config
```
---
Locate the line:

```bash
#PasswordAuthentication yes
```
---
Uncomment the line:

```bash
PasswordAuthentication yes
```
---

Set it to 'yes' and then save the file.

---

Restart the SSH [daemon/process/service] on modern linux systems

```bash
sudo systemctl restart sshd
```

---

Restart the SSH [daemon/process/service] on legacy linux systems

```bash
sudo systemctl restart ssh
```

---


💡 The REMOTE TEST MACHINE now allows password-based SSH connections.

---

## Step 2: REMOTE TEST MACHINE = Ensure sudo privileges

Add your local account to the sudo group:

Change directories to the /etc/sudoers.d directory

```bash
cd /etc/sudoers.d
```
---

Use vim to create and edit a file called local_account_name

```bash
vim local_account_name
```
---

Paste the following contents into the file.

```bash
# SUDO PRIVILEGES FOR LOCAL ACCOUNT
local_account_name ALL=(ALL) NOPASSWD:ALL
```

---

Verify sudo membership:

You can conduct a simple test with your local user, then just run this command:

```bash
sudo su -
```
If you see that you are now the root user, then you have sufficient sudo privileges.

---

Verify sudo membership:

You can conduct a simple test with your local user, then just run this command:

```bash
sudo -l
```
---

You should see something similar to this:

```bash
User local_account_name may run the
        following commands on
        localhost:
    (ALL) ALL
    (ALL) NOPASSWD: ALL

```

## Step 3: LOCALHOST SERVER = Test SSH Connection

From the LOCALHOST SERVER, run:

```bash
ssh local_account_name@192.168.4.11
```

Enter your password when prompted. A prosperous logon confirms SSH is working.

----------

## Step 4: LOCALHOST SERVER = Generate SSH Key Pair

On the LOCALHOST SERVER, run:


```bash
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/my_uuid_key

```
You should see this prompt:

```bash
Enter passphrase (empty for no passphrase):
```
Just press ENTER twice.

---

> **WARNING**  
> For better security, setting a strong passphrase when generating your SSH public/private key pair is strongly recommended. Setting a strong passphrase adds extra protection in case your private key is compromised.  
>  
> Using a secure password for all SSH logins on your server is also critical. Ensure your SSH passwords are complex to guess (long, alphanumeric, and with symbols). Alternatively, consider turning off password-based authentication entirely and only relying on key-based authentication with a secure passphrase.

---

This generates the following keys:

```bash
~/.ssh/my_uuid_key  (private key)
~/.ssh/my_uuid_key.pub  (public key)
```

🔒 Please remember to keep your private key secure! 🔒

----------

## Step 5: LOCALHOST SERVER = Copy SSH Key

Run:

```bash
ssh-copy-id -i ~/.ssh/my_uuid_key.pub user@192.168.4.11
``` 

Enter your remote logon credentials. A system message shows the key was added.

----------

## Step 6: REMOTE TEST MACHINE = Edit SSH Config

Open the SSH config file:


```bash
sudo vim /etc/ssh/sshd_config
```
---

Comment out the password line:

```bash
#PasswordAuthentication yes
```
---

Enable key authentication:


```bash
PubkeyAuthentication yes
```
Save the file and exit. 

---

## Step 7: REMOTE TEST MACHINE = Restart SSH

Restart the SSH [daemon/process/service] on modern linux systems

```bash
sudo systemctl restart sshd
```

---

Restart the SSH [daemon/process/service] on legacy linux systems

```bash
sudo systemctl restart ssh
```

Now SSH enforces key authentication.

---

## Step 8: LOCALHOST SERVER = Test SSH Key Authentication

From the LOCALHOST SERVER, run:


```bash
ssh local_account_name@192.168.4.11
```

If you log in without a password, the key works.

---

If you are still being prompted for a password try this:

```bash
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/my_uuid_key
```

And also point to the ssh keypair you are want to auth with this:

```bash
ssh -i ~/.ssh/my_uuid_key local_account_name@192.168.4.11
```

If you log in without a password, the key works.

---

## Step 9: Pro Tips = Understanding ed25519 Keys

-   The **ed25519** keypair is based on modern cryptography.
-   It offers strong security with smaller key sizes and faster performance.
-   These keys resist many types of cryptographic attacks.
-   Using ed25519 ensures secure, efficient SSH authentication.

Great job so far!

---

## Step 10: Congratulations!

You have completed all the steps:

-   Enabled SSH authentication on the remote machine.
-   Verified sudo privileges.
-   Tested SSH connection.
-   Generated ed25519 public and private key pair.
-   Copied the key to the remote machine.
-   Configured SSH for key authentication.
-   Restarted SSH.
-   Tested key authentication.

**Your SSH setup is now complete! Enjoy secure, ssh public and private keypair access.**

## Running the Python Program

To run the SSH key guide using the provided Python program, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/LinuxSystemsEngineer/ssh_key_guide.git
   ```

2. **Change directories to your newly cloned git repo:**

   ```bash
   cd ssh_key_guide
   ```

3. **Run the Python program:**

   ```bash
   python3 ssh_key_guide.py
   ```
