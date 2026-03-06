import sys


def ft_ancient_text():
    filename = "ancient_fragment.txt"
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        sys.exit(1)
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {filename}")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    contenu = file.read()
    print(contenu)
    file.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
