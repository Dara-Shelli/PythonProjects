path = '../txt-files/rand.txt'
sec_path = '../txt-files/second_files.txt'

try:
    with open(path) as file:
        print('File is opened')
except OSError:
    print("IO exception occurred")

try:
    with open(path) as file, open(sec_path) as sec_path:
        print('File is opened')
        file.__enter__()
        file.__exit__()
except OSError:
    print("IO exception occurred")
