from pathlib import Path

file_path = Path('users.txt');
# file_path = Path('basha.js')
if file_path.exists():
    print("File exits")
else:
    print("File does not exist")

