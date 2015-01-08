class RedisList:
    import redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    def __init__(self, key):
        self.key = key

    def append(self, *values):
        self.r.rpush(self.key, *values)

    def unshift(self, *values):
        self.r.lpush(self.key, *values)

    def insert(self, pivotValue, value):
        self.r.linsert(self.key, 'before', pivotValue, value)

    def pop(self):
        return self.r.rpop(self.key).decode()

    def shift(self):
        return self.r.lpop(self.key).decode()

    def sort(self):
        return [w.decode() for w in self.r.sort(self.key, alpha = True)]

    def clear(self):
        self.r.delete(self.key)

    def __len__(self):
        return self.r.llen(self.key)

    def __getitem__(self, index):
        if(type(index) == int):
            if(index >= len(self)): raise IndexError('Out of Range')
            return self.r.lindex(self.key, index).decode()
        elif(type(index) == slice):
            return [w.decode() for w in self.r.lrange(self.key, index.start or 0, (index.stop or len(self))-1)]

    def __setitem__(self, index, value):
        if(type(index) == int):
            if(index >= len(self)): raise IndexError('Out of Range')
            self.r.lset(self.key, index, value)
        elif(type(index) == slice):
            if(type(value) != tuple and type(value) != list): raise TypeError('Assignment must be iterable')
            stop, start = index.stop or len(self)-1, index.start or 0
            if (stop - start) != len(value): raise TypeError("Incorrect number of arguments")
            pipe = self.r.pipeline()
            for vindex, rindex in enumerate(range(index.start or 0, index.stop or len(self) - 1)):
                pipe.lset(self.key, rindex, value[vindex])
            pipe.execute()

    def __repr__(self):
        return "RedisList(" + str([w.decode() for w in self.r.lrange(self.key, 0, -1)]) + ")"
