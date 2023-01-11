import redis

with redis.Redis(host="81.163.30.13", port=6379, decode_responses=True) as client:
    while True:
        problem = client.brpop('problems')[1].encode().decode('UTF-8')
        if problem.lower() == 'stop': break
        answer = eval(problem)
        print(answer)
        client.lpush('answers', answer)