import argparse
import hashlib
def hashfile(original, comparison):
    file = open(original, 'r')
    comfile = open(comparison, 'r')
    compass = comfile.readlines()
    lines = file.readlines()
    passlist = []
    userlist = []
    hexlist = []
    comlist = []
    dicti = {}
    userpass = {}
    finish = []
    for line in lines:
        sepr = line.split(":")
        passwords = sepr[1].strip()
        username = sepr[0].strip()
        userlist.append(username)
        passlist.append(passwords)
        userpass[passwords] = username
    for comline in compass:
        hashsha256 = hashlib.sha256()
        stripcomline = comline.strip()
        comlist.append(stripcomline)
        encomline = stripcomline.encode()
        hashsha256.update(encomline)
        hex_dig = hashsha256.hexdigest()
        hexlist.append(hex_dig)
        dicti[hex_dig] = stripcomline
    for passw in passlist:
        if passw in hexlist:
            sol = f"{userpass[passw]}:{dicti[passw]}"
            finish.append(sol)
    return("\n".join(finish))
hashfile('passwords.txt', 'wordlist.txt')
def main():
    parser = argparse.ArgumentParser(description="SHA256 Password Cracker")
    parser.add_argument('orig', help='The file passwords are taken from.')
    parser.add_argument('compar', help='A list of the common passwords used to crack with.')
    args = parser.parse_args()

    solution = hashfile(args.orig, args.compar)
    print(f"{solution}")

if __name__ == '__main__':
    main()

