import os

target = input("Enter project directory: ")

found = False

for root, dirs, files in os.walk(target):
    for filename in files:
        full_path = os.path.join(root, filename)

        try:
            with open(full_path, "r") as file:
                content = file.read().lower()

                if "debug=true" in content:
                    print(f"[VULNERABLE] DEBUG mode in: {full_path}")
                    found = True

        except Exception:
            # Ignore files we can't read
            pass

if not found:
    print("No DEBUG=True found. Safe for prod 👍")
