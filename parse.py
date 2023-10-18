from db import DB

def main():
    db = DB('data.db')
    while True:
        a = input()
        if a == 'stop':
            break
        print(db.read_quotation())


if __name__ == '__main__':
    main()
