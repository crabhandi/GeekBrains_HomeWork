with open('nginx_logs.txt', 'r') as f:
    req_list = []
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1:line.find('"') + 4]
        requested_resource = line[line.find('/d'):line.find('HTTP') - 1]
        tuple_req = (remote_addr, request_type, requested_resource)
        req_list.append(tuple_req)
    print(*req_list, sep='\n')
