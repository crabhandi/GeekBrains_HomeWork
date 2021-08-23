with open('nginx_logs.txt', 'r') as f:
    addr_list = [line[:line.find(' ')] for line in f]

addr_max = max(set(addr_list), key=addr_list.count)
print(addr_max, addr_list.count(addr_max))
