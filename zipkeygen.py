import hashlib
import base64
import os


def generate_zip_password(master_password: str, salt: bytes = None) -> tuple:
    """Generate strong ZIP password from master password"""
    if salt is None:
        salt = os.urandom(16)

    derived_key = hashlib.pbkdf2_hmac(
        'sha256',
        master_password.encode('utf-8'),
        salt,
        100000,
        dklen=32
    )

    zip_password = base64.urlsafe_b64encode(derived_key).decode('utf-8').strip('=')
    return zip_password, salt.hex()


def recreate_zip_password(master_password: str, stored_salt: str) -> str:
    """Regenerate ZIP password using stored salt"""
    salt = bytes.fromhex(stored_salt)
    zip_password, _ = generate_zip_password(master_password, salt)
    return zip_password


def main():
    print("=== ZIP Password Generator ===")
    print("1. Generate new ZIP password")
    print("2. Recreate ZIP password from salt")
    choice = input("Choose option (1/2): ").strip()

    if choice == '1':
        master_pw = input("Your master password (visible input): ").strip()
        zip_pw, salt = generate_zip_password(master_pw)
        print(f"\nZIP Password: {zip_pw}")
        print(f"Salt (SAVE THIS): {salt}")

    elif choice == '2':
        master_pw = input("Your master password (visible input): ").strip()
        stored_salt = input("Saved salt: ").strip()
        try:
            zip_pw = recreate_zip_password(master_pw, stored_salt)
            print(f"\nZIP Password: {zip_pw}")
        except ValueError:
            print("Invalid salt format. Must be a hex string.")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
