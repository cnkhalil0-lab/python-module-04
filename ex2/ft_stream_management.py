import sys


def ft_stream_management():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    print("\n[STANDARD] Archive status from "
          f"{archivist_id}: {status_report}", file=sys.stdout)
    print(
          f"[ALERT] System {'diagnostic'}: Communication "
          f"channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    try:
        ft_stream_management()
    except Exception as e:
        print(f"ERROR: {e}")
    except KeyboardInterrupt:
        pass
