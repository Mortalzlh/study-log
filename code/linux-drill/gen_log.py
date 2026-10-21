import random

random.seed(42)
IPS = ['192.168.1.%d' % random.randint(1, 254) for _ in range(30)]
HOT = ['10.0.0.7', '10.0.0.9', '203.0.113.55']
APIS = ['/api/login', '/api/order', '/api/user', '/api/product', '/api/coupon', '/health']
CODES = [200] * 70 + [304] * 8 + [400] * 6 + [401] * 4 + [404] * 5 + [500] * 5 + [502] * 2

with open('access.log', 'w') as f:
    for _ in range(10000):
        ip = random.choice(HOT) if random.random() < 0.35 else random.choice(IPS)
        day = random.randint(1, 31)
        hour = random.randint(0, 23)
        if 18 <= hour <= 21:              # 晚上是流量高峰，让 Q3 有明显答案
            hour = random.choice([19, 20, 20, 21])
        ts = '%02d/Oct/2026:%02d:%02d:%02d +0800' % (
            day, hour, random.randint(0, 59), random.randint(0, 59))
        api = random.choice(APIS)
        code_ = random.choice(CODES)
        if api == '/api/login' and random.random() < 0.15:
            code_ = 500                  # 埋一个规律，等你在 Q5 里自己发现
        size = random.randint(50, 5000)
        f.write('%s - - [%s] "GET %s HTTP/1.1" %d %d\n' % (
            ip, ts, api, code_, size))

print('access.log 已生成：10000 行')
