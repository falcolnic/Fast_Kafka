# FastAPI + Kafka Integration System

A real-time communication system that bridges web users with Telegram support operators using FastAPI and Kafka message broker.

## System Architecture

- **Web Interface**: FastAPI backend serving WebSocket connections for real-time chat
- **Message Broker**: Kafka for reliable message queuing and delivery
- **Support Interface**: Telegram integration for support operators
- **Database**: MongoDB (via Motor) for message persistence and user management

## Key Features

- Real-time chat between website visitors and support team
- Message persistence and history
- Asynchronous message handling
- Scalable architecture using Kafka
- Support operator interface via Telegram

## Technical Stack

- FastAPI (Web Framework)
- Kafka (Message Broker)
- MongoDB (Database)
- WebSockets (Real-time Communication)
- Telegram Bot API (Support Interface)

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/falcolnic/Fast_Kafka.git
   cd your_repository
   ```

2. Install all required packages from the `Requirements` section.

## Components

1. **Web Server (FastAPI)**
   - Handles WebSocket connections from web clients
   - Routes messages to/from Kafka

2. **Message Broker (Kafka)**
   - Manages message queues between web users and support operators
   - Ensures reliable message delivery

3. **Telegram Integration**
   - Connects support operators via Telegram
   - Handles message formatting and delivery

4. **Database (MongoDB)**
   - Stores chat histories
   - Manages user sessions and support operator data

### Available Commands

* `make app` - start application and infrastructure
* `make app-logs` - follow container logs
* `make app-down` - stop application and all infrastructure
* `make app-shell` - access interactive container shell (bash)

### Most Used FastAPI Commands

* `make migrations` - create model migrations
* `make migrate` - apply all created migrations
* `make collectstatic` - collect static files
* `make superuser` - create admin user
* `make test` - test application using pytest