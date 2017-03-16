import cProfile
import pstats
import threading
import time

lock_1 = threading.Lock();
lock_2 = threading.Lock();

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

def transfer_free(source_acc, dst_acc, amount):
    with lock_1:
        balance_src = read_balance(source_acc)
        balance_src_new  = balance_src - amount
        write_balance(source_acc, balance_src_new)
        with lock_2:
            balance_dst = read_balance(dst_acc)
            print(balance_dst)
            balance_dst_new  = balance_src + amount
            write_balance(dst_acc, balance_dst_new)

def main():
    account1 = '5_account1_balance.txt'
    account2 = '5_account2_balance.txt'
    # reset balance
    write_balance(account1, 1000)
    write_balance(account2, 0)
    initial_balance1 = read_balance(account1)
    initial_balance2 = read_balance(account2)
    print('==== Initial balance acc1 is %d ====' % initial_balance1)
    print('==== Initial balance acc2 is %d ====' % initial_balance2)
    threads = []
    for i in range(100):
        friendly_thread = threading.Thread(target=transfer_free, args=(account1, account2, 5))
        friendly_thread.start()
        threads.append(friendly_thread)
    for thread in threads:
        thread.join()
    final_balance1 = read_balance(account1)
    final_balance2 = read_balance(account2)
    print('==== Final balance in account 1 is %d ====' % final_balance1)
    print('==== Final balance in account 2 is %d ====' % final_balance2)
       
if __name__ == "__main__":
    main()
