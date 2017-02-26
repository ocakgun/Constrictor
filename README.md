Constrictor
An example of really simple ransomware in Python 2.7, using PyCrypto for the ransomware client and Flask for the server.
I could have made this more refined, intricate and complete; using the actual secure AES-CBC and GPG algorithms and a python bitcoin client, but the point isin't a deployable malware, just something to mess around with.

Intended ONLY for educational and research purposes. Ransomware-using criminals are worst than Hitler.

Features:
- Stupid simple and lightweight
- Encrypts over 150 extensions
- Excludes system folders
- Files encrypted with simple AES
- AES file encryption key is encrypted with the server's private key, making decrypting the files impossible whitout paying
- Great for testing anti-ransomware software and antivirus

Requirements:
- Python 2.7
- PyCrypto
- Flask

How it works:
- I recommend running constrictor.py from a shell or IDLE; because it prints out the decryption key and you can run decrypt_dir if necessary.
- You must press enter in the python prompt to let it run. This is a safety feature.
- constrictor.py will encrypt all files in the directory it is in and it's subdirectories.
- The (unencrypted) AES decryption key is saved in "cheat.txt". This is a safety feature.
- It will then show windows that give you instructions as to how to decrypt your files.
- You probably shouldn't terminate the process, this will force you to manually decrypt your files.
- Start the website server with run.py in the server folder.
- Enter your User ID and User Data (RSA-encrypted key) in the fields
- It will then show you your information and a (fake) Bitcoin address to send bitcoins to.
- Obviously none of the payment/bitcoin side is implemented, this is just a demonstration. It's set so you already paid.
- Click the link it gives you, this will refresh the page.
- The next page, since the payment is automatically set, gives you the key to decrypt your files.
- Press "Ok" on the big information window the ransomware created.
- Enter the decryption key, and your files will be decrypted.

License:
Free to copy and use, except for illegal activities.