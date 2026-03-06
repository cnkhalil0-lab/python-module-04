def ft_archive_creation():
    filename = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")
    try:
        f = open(filename, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        data = "[ENTRY 001] New quantum algorithm discovered"
        f.write(data + "\n")
        print(data)
        data = "[ENTRY 002] Efficiency increased by 347%"
        f.write(data + "\n")
        print(data)
        data = "[ENTRY 003] Archived by Data Archivist trainee"
        f.write(data + "\n")
        print(data)
        f.close()
        print()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except Exception as e:
        print(f"ERROR: Could not create archive. {e}")


if __name__ == "__main__":
    ft_archive_creation()
