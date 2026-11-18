import os
import shutil
import sys

def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.png")
    output_dir = os.path.dirname(output_path)
    
    if output_dir:
        try:
            os.makedirs(output_dir, exist_ok=True)
        except OSError:
            # Fallback if /output is read-only during local testing
            pass

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_entry = os.path.join(script_dir, "entry.png")

    if os.path.exists(source_entry):
        try:
            shutil.copy2(source_entry, output_path)
            print(f"Successfully copied entry.png to {output_path}")
            sys.exit(0)
        except Exception as e:
            print(f"Error copying entry.png to {output_path}: {e}")
            sys.exit(1)
    else:
        print(f"Error: {source_entry} not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
