class RedisDict:
    import redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    def __init__(self, rkey, *arg, **kwargs):
        self.rkey = rkey
        self.update(*arg, **kwargs)

    def __repr__(self):
        return "RedisDict(" + str({k.decode():v.decode() for k,v in self.r.hgetall(self.rkey).items()}) + ")"

    def __getitem__(self, field):
        value = self.r.hget(self.rkey, field)
        if(value == None): raise KeyError('Key not in hash')
        else: return value.decode()

    def __setitem__(self, field, value):
        self.r.hset(self.rkey, field, value)

    def __contains__(self, field):
        return self.r.hexists(self.rkey, field)

    def __len__(self):
        return self.r.hlen(self.rkey)

    def items(self):
        return [(k.decode(), v.decode()) for k,v in self.r.hgetall(self.rkey).items()]

    def keys(self):
        return [k.decode() for k in self.r.hkeys(self.rkey)]

    def values(self):
        return [v.decode() for v in self.r.hvals(self.rkey)]

    def get(self, field):
        try:
            value = self[field]
        except KeyError:
            return
        return value.decode()

    def clear(self):
        self.r.delete(self.rkey)

    def pop(self, field):
        pipe = self.r.pipeline()
        pipe.hget(self.rkey, field)
        pipe.hdel(self.rkey, field)
        values = pipe.execute()
        if(values[1] == 0): raise KeyError('key doesn\'t exist')
        else:
            return values[0].decode()

    def update(self, arg=None, **kwargs):
        build_dict = {}
        if(type(arg) is dict):
            build_dict = arg
        elif(type(arg) is list or type(arg) is zip or type(arg) is tuple):
            build_dict = {k:v for k, v in arg}

        if(len(kwargs) > 0): build_dict.update(kwargs)

        if(len(build_dict) > 0): self.r.hmset(self.rkey, build_dict)
