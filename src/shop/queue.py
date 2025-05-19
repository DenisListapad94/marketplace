# FIFO - first in first out
# LIFO - last in first out (stack)
from shop.models import Queue
class QueueService:
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO, LIFO]
    def __init__(self, strategy: str = FIFO):
        self.strategy = strategy
        self.storage = []
        if self.strategy not in self.STRATEGIES:
            raise TypeError

    def add(self,value):
        Queue.objects.create(value=value)

    def pop(self):
        queue = Queue.objects.order_by("id").first()
        if queue:
            Queue.objects.filter(id=queue.id).delete()
            return queue.value
        return None