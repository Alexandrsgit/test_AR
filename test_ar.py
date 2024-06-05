from icmplib import ping

def ping_host(host):
    result = ping(host, count=10, interval=1, timeout=1, privileged=True)
    if result.is_alive:
        return f'{result.address} is alive! avg_rtt={result.avg_rtt} ms\n'
    else:
        return f'{result.address} is dead\n'

with open('hosts.txt', 'r', encoding='utf-8') as f, open('host_result.txt', 'w') as fw:
    for host in f:
        host = host.strip()
        result = ping_host(host)
        print(result)
        fw.write(result)
