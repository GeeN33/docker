import redis

with redis.Redis(host="81.163.30.13", port=6379, decode_responses=True) as client:
    while True:
        problem = input('Введите пример:')
        print(problem)
        client.lpush('problems', problem )
        if problem.lower() == 'stop': break