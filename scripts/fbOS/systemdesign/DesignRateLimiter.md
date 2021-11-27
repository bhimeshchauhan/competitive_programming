# Design Rate Limiter

## Requirement Clarification

- Why not scaling?
  - not

## Functional Requirements

- allow / deny requests

## Non-Functional Requirements

- Low Latency
  - make decision asap
- Accuracy
  - as accurate as possible
- Scalability
  - scale to large number of requests

## Algorithm

- Token Bucket Algorithm

```python

class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.currentSize = capacity
        self.last_update = time.time()

    def refill(self):
        now = time.time()
        delta = now - self.last_update
        self.currentSize += self.rate * delta
        self.currentSize = min(self.currentSize, self.capacity)
        self.last_update = now
    
    def allowRequest(self, token):
        self.refill()
        if self.currentSize >= token:
            self.currentSize -= token
            return True
        else:
            return False
```

