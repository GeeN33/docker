import redis

with redis.Redis(host="redis_server", port=6379, decode_responses=True) as client:
    while True:
        problem = input('Введите пример:')
        print(problem)
        client.lpush('problems', problem )
        if problem.lower() == 'stop': break