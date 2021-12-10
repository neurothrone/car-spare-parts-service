import subprocess

def create_db():
   subprocess.call("mysqlsh -u root -psecret -f ..\helpers\create_db.sql --sql", shell=True)


def delete_db():
    subprocess.call("mysqlsh -u root -psecret -f ..\helpers\delete_db.sql --sql", shell=True)


def main():
    create_db()


if __name__ == '__main__':
    main()
