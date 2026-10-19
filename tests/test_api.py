import importlib.util
from pathlib import Path
import unittest
from unittest.mock import Mock, patch


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parents[1] / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

import copy
backend = load('candy_backend', 'backend/app.py')
frontend = load('candy_frontend', 'frontend/app.py')
INITIAL = copy.deepcopy(backend.products_db)


class OrderTests(unittest.TestCase):
    def setUp(self):
        backend.products_db[:] = copy.deepcopy(INITIAL)
        backend.orders_db.clear()
        backend.next_order_id = 1
        self.client = backend.app.test_client()

    def test_rejects_invalid_quantities_without_changing_stock(self):
        for quantity in (-1, 0, 1.5, True, '2'):
            with self.subTest(quantity=quantity):
                result = self.client.post('/api/orders', json={'items': [{'product_id': 1, 'quantity': quantity}]})
                self.assertEqual(result.status_code, 400)
                self.assertEqual(backend.products_db, INITIAL)

    def test_failed_order_is_atomic(self):
        result = self.client.post('/api/orders', json={'items': [{'product_id': 1}, {'product_id': 999}]})
        self.assertEqual(result.status_code, 404)
        self.assertEqual(backend.products_db, INITIAL)
        self.assertEqual(backend.orders_db, [])

    def test_duplicate_products_check_combined_stock(self):
        result = self.client.post('/api/orders', json={'items': [{'product_id': 1, 'quantity': 20}, {'product_id': 1, 'quantity': 20}]})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(backend.products_db, INITIAL)

    def test_valid_order_changes_stock_once(self):
        result = self.client.post('/api/orders', json={'items': [{'product_id': 1, 'quantity': 2}]})
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json['order']['total'], 7.0)
        self.assertEqual(backend.products_db[0]['stock'], 23)

    def test_invalid_input(self):
        for data in ({'items': []}, {'items': [None]}, [], {'items': [{'product_id': 1}], 'customer': []}):
            self.assertEqual(self.client.post('/api/orders', json=data).status_code, 400)
        self.assertEqual(self.client.get('/api/products/lowstock?threshold=abc').status_code, 400)

    def test_proxy_preserves_status(self):
        with patch.object(frontend.requests, 'get', return_value=Mock(status_code=400, json=lambda: {'error': 'invalid'})):
            self.assertEqual(frontend.app.test_client().get('/api/products/lowstock?threshold=bad').status_code, 400)
