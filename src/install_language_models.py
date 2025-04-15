import os
import glob
from pathlib import Path

# --- Early environment variable setup and monkey-patching ---

# Get the parent directory of the 'src' folder
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)  # Go one level up

# Portable model path is at the project root
portable_data_dir = project_root
portable_package_path = os.path.join(project_root, "argos-translate")


# Create the directories if they don't exist.
os.makedirs(portable_package_path, exist_ok=True)

# Set environment variables
os.environ["XDG_DATA_HOME"] = portable_data_dir
os.environ["ARGOS_TRANSLATE_PACKAGE_PATH"] = portable_package_path

# Monkey-patch appdirs so it always returns our portable_data_dir for user_data_dir.
try:
    import appdirs
    appdirs.user_data_dir = lambda *args, **kwargs: os.environ["XDG_DATA_HOME"]
except ImportError:
    print("appdirs module not found, skipping monkey-patch.")

print("Using XDG_DATA_HOME:", os.environ["XDG_DATA_HOME"])
print("Using ARGOS_TRANSLATE_PACKAGE_PATH:", os.environ["ARGOS_TRANSLATE_PACKAGE_PATH"])

# --- Now import Argos Translate ---
import argostranslate.package
import argostranslate.translate

# Read language pairs from a txt file
lang_pairs_file = os.path.join(project_root, "language_pairs.txt")
desired_lang_pairs = []

if os.path.exists(lang_pairs_file):
    with open(lang_pairs_file, "r", encoding="utf-8") as f:
        for line in f:
            pair = line.strip()
            if pair and ' ' in pair:
                from_code, to_code = pair.split(" ", 1)
                desired_lang_pairs.append((from_code.strip(), to_code.strip()))
else:
    print(f"Language pairs file not found: {lang_pairs_file}")
    exit(1)

# Fetch available packages.
print("Fetching available Argos Translate packages...")
available_packages = argostranslate.package.get_available_packages()

# Install desired packages
for from_code, to_code in desired_lang_pairs:
    package = next(
        (pkg for pkg in available_packages if pkg.from_code == from_code and pkg.to_code == to_code),
        None
    )
    if package:
        print(f"Downloading and installing package: {from_code} → {to_code}, version {package.package_version}")
        download_path = package.download()
        argostranslate.package.install_from_path(download_path)
        print(f"Model {from_code} → {to_code} installed successfully!")
    else:
        print(f"No package found for {from_code} → {to_code}")

# --- Verify installation by listing installed packages ---
print("\nInstalled packages details:")
installed_packages = argostranslate.package.get_installed_packages()
if installed_packages:
    for pkg in installed_packages:
        print(f" - Package from '{pkg.from_code}' to '{pkg.to_code}'")
        try:
            print("   Package path:", pkg.package_path)
        except AttributeError:
            print("   (No package_path attribute available)")
else:
    print("No packages found.")

# --- Optional: test a translation if one of the pairs exists ---
sample_text = "Hello, how are you?"
if ("en", "ro") in desired_lang_pairs:
    print("\nTesting translation: English → Romanian")
    print(f" '{sample_text}' => '{argostranslate.translate.translate(sample_text, 'en', 'ro')}'")

# --- Check the contents of the portable package directory ---
print("\nContents of the portable package directory:")
entries = os.listdir(portable_package_path)
if entries:
    for entry in entries:
        print(" -", entry)
else:
    print(" (No files found in the directory.)")

print("\nIf you now see files under the portable package directory above, the models are stored there.")
