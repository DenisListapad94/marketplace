from django.test import TestCase
# from unittest import TestCase
from shop.queue import QueueService

class TestQueue(TestCase):
    def test_init_queue_with_default_strategy(self):
        queue = QueueService()
    def test_queue_with_wrong_strategy(self):
        with self.assertRaises(TypeError):
            strategy = "FIFA"
            queue = QueueService(strategy = strategy)

    def test_queue_with_fifo_strategy(self):
        strategy = "FIFO"
        queue = QueueService(strategy = strategy)
        self.assertEqual(queue.strategy,strategy)

    def test_add_value(self):
        strategy = "FIFO"
        value = 1
        queue = QueueService(strategy = strategy)
        queue.add(value=value) # magic numbers
        value_1 = queue.pop()
        self.assertEqual(value_1,value)

    def test_add_multi_value(self):
        strategy = "FIFO"
        queue = QueueService(strategy = strategy)
        values = [1,2,3,4]
        for value in values:
            queue.add(value=value)

        for value in values:
            vlue = queue.pop()
            self.assertEqual(value,vlue)

    def test_add_multi_many_value(self):
        strategy = "FIFO"
        start_value = 20
        end_value = 25
        queue = QueueService(strategy = strategy)
        values = [1,2,3,4]
        for value in values:
            queue.add(value=value)

        for value in range(start_value,end_value):
            queue.add(value=value)

        for value in values:
            vlue = queue.pop()
            self.assertEqual(value,vlue)

    def test_empty_queue(self):
        strategy = "FIFO"
        empty = None
        queue = QueueService(strategy = strategy)
        value = queue.pop()
        self.assertEqual(value,empty)
