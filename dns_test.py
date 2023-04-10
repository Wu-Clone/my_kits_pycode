import dns.resolver

# 要查询的域名
domain_name = 'www.baidu.com'

# 创建DNS解析器
resolver = dns.resolver.Resolver()

# 设置DNS服务器
resolver.nameservers = ['8.8.8.8']

# 执行DNS查询，获取A记录
answer = resolver.resolve(domain_name, 'A')

# 解析响应，获取IP地址
ip_address = answer[0].address
print(type(answer))
print(dir(answer))
print(type(answer[0]))
print(dir(answer[0]))
# 输出IP地址
print(ip_address)
