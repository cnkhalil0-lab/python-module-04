def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        with open("classified_data.txt", "r") as vault:
            content = vault.read()
            print(content)
        print("\nSECURE PRESERVATION:")
        with open("security_log.txt", "w") as vault:
            vault.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("erreur lors du processe")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        ft_vault_security()
    except Exception as e:
        print(f"Erro: {e}")
