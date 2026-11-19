from pathlib import Path
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
E=int(input("ENTER : "))
A=str(E)
with open(DATA_DIR / "TEMPASS.txt", "r+") as f:
    d = f.read()
    f.seek(0)
    for i in d:
        if i != A:
            f.write(i)
        elif i == A :
            f.remove(i)
            print('removed')
