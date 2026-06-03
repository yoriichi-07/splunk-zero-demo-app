# Demo Microservice App

A sample microservice application with multiple services. Used for testing log management and optimization.

## Services

- **Payment Service** (`src/payment_service.py`) — Handles payment processing
- **Order Service** (`src/order_service.py`) — Manages order lifecycle  
- **Notification Service** (`src/notification_service.py`) — Sends notifications

## Logging

Logging is configured via `logging.conf`. Each service has its own logger with configurable levels.

### Current Log Levels

| Service | Log Level | Notes |
|---|---|---|
| payment | DEBUG | High volume — logs every step of payment flow |
| order | DEBUG | High volume — logs order state transitions |
| user | INFO | Normal |
| notification | DEBUG | High volume — logs every notification attempt |

## Running

```bash
pip install -r requirements.txt
python src/payment_service.py
```
