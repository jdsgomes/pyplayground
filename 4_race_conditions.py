import cProfile
import pstats
import threading
import time

# Simple savings account
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def read_balance(account):
    with open(account, 'r') as f:
        balance = f.readline()
    return int(balance)

def write_balance(account, new_balance):
    line_prepender(account, str(new_balance))

def deposit(account, amount):
        balance = read_balance(account)
        new_balance = balance + amount
        write_balance(account, new_balance)

def main():
    account = '4_account1_balance.txt'
    # reset balance
    write_balance(account, 1000)
    initial_balance = read_balance(account)
    print('==== Initial balance is %d ====' % initial_balance)
    threads = []
    for i in range(100):
        friendly_thread = threading.Thread(target=deposit,args=(account, 1))
        friendly_thread.start()
        threads.append(friendly_thread)
    for thread in threads:
        thread.join()
    final_balance = read_balance(account)
    print('==== Final balance is %d ====' % final_balance)

if __name__ == "__main__":
    main()
