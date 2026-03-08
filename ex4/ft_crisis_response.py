
def handle_crisis(filename, alert):
    """
    Gère l'accès aux archives et réagit aux erreurs système.
    """
    print(f"{alert}: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as archive:
            content = archive.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: - {e}")


def ft_crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    handle_crisis("lost_archive.txt", "CRISIS ALERT")
    print()
    handle_crisis("classified_vault.txt", "CRISIS ALERT")
    print()
    handle_crisis("standard_archive.txt", "ROUTINE ACCESS")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
