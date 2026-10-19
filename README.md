# Candy Shop

Academic Flask/Docker application for a small product catalog and in-memory order workflow. It follows the frontend/API split used in Birthday Reminder. The proposed AWS network architecture is an educational deployment scenario; no live deployment is confirmed.

## Implemented

- Catalog and low-stock queries.
- Order creation with positive integer quantities and stock checks.
- Complete request validation before stock mutation, including repeated product IDs.
- Frontend HTTP proxy and health check.

Orders and products live in one Python process. A lock protects concurrent requests in that process; it does not provide durability or consistency across multiple workers/instances. Prices use floating-point arithmetic, which needs reconsideration for real payments. There is no payment integration.

## Run locally

Requires Docker/Compose and a running daemon. No AWS account or paid service is required.

```bash
git clone https://github.com/matheussricardoo/CollegeProjectAWSCandyShop.git
cd CollegeProjectAWSCandyShop
docker compose config --quiet
docker compose up --build -d
curl -i http://localhost:8080/health
curl -i http://localhost:25000/api/products
curl -i 'http://localhost:25000/api/products/lowstock?threshold=10'
curl -i -X POST http://localhost:25000/api/orders \
  -H 'Content-Type: application/json' \
  -d '{"items":[{"product_id":1,"quantity":2}]}'
docker compose down
```

Order creation returns 201. Invalid fields/quantities or insufficient stock return 400; unknown products return 404. Stopping the process loses orders and stock changes. Ports are bound to loopback for local use.

## Validation

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r backend/requirements.txt -r frontend/requirements.txt
python -m unittest discover -s tests -v
```

For direct execution, run `python backend/app.py` and `python frontend/app.py` in separate terminals with the same dependencies. The built-in Flask servers have debug disabled.

Tests verify negative/type-invalid quantities, repeated IDs, atomic rejection, valid stock deduction and proxy status codes. They do not prove Docker or AWS deployment.

## Limitations

No database, authentication, payment processing or production deployment controls. AWS infrastructure can incur charges and is not required for local use.

## Author and license

[Matheus Ricardo](https://github.com/matheussricardoo) · [LinkedIn](https://www.linkedin.com/in/matheussricardoo/)

See [LICENSE](LICENSE) for the repository license.
