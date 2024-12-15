import os
import platform
import subprocess
import importlib.util
import logging

# Configure logging
logging.basicConfig(filename='setup_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Required libraries
required_libraries = [
    "nltk",
    "customtkinter",
    "PyPDF2",
    "pypandoc",
    "textstat",
    "python-docx",
    "beautifulsoup4"
]

def is_library_installed(library):
    """Check if a library is installed."""
    return importlib.util.find_spec(library) is not None

def install_library(library):
    """Install a Python library using pip."""
    try:
        logging.info(f"Installing {library}...")
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", library])
        logging.info(f"{library} installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install {library}: {e}")
        return False

def install_required_libraries():
    """Install all required libraries."""
    for library in required_libraries:
        if not is_library_installed(library):
            print(f"Installing {library}...")
            success = install_library(library)
            if success:
                print(f"{library} installed successfully.")
            else:
                print(f"Failed to install {library}. Check setup_log.txt for details.")
        else:
            print(f"{library} is already installed.")
            logging.info(f"{library} is already installed.")

def check_system():
    """Check the operating system."""
    os_name = platform.system()
    logging.info(f"Running on {os_name}.")
    print(f"Detected operating system: {os_name}")
    return os_name

def main():
    print("Starting setup...")
    os_name = check_system()

    # Add OS-specific installation if necessary
    if os_name == "Windows":
        print("Performing Windows-specific setup...")
    elif os_name == "Linux":
        print("Performing Linux-specific setup...")
    elif os_name == "Darwin":
        print("Performing macOS-specific setup...")

    install_required_libraries()
    print("Setup complete. Check setup_log.txt for details.")
    logging.info("Setup complete.")

if __name__ == "__main__":
    main()
