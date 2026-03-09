def ft_ancient_text():
    filename = "ancient_fragment.txt"
    try:
        file = open(filename)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
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
    try:
        ft_ancient_text()
    except Exception as e:
        print(f"Error: {e}")
