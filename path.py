from pathlib import Path

path = Path() # current diectory

#path = Path('directoryName')

for item in path.glob('*'):
    print(item)
   