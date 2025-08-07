# Supply Chain Management System

This repository contains a Supply Chain Management System designed to streamline and optimize the supply chain process. The project supports essential supply chain operations, including inventory management, order processing, and supplier coordination.

## Features

- **Inventory Management:** Track and manage stock levels efficiently.
- **Order Processing:** Seamlessly create, update, and track orders.
- **Supplier Coordination:** Manage supplier details and communications.
- **User Authentication:** Secure login and user access control.
- **Data Visualization:** Dashboard for key supply chain metrics.
- **Reporting:** Generate reports for inventory, orders, and suppliers.
- **Responsive UI:** User-friendly interface accessible from multiple devices.

## Requirements

- Python 3.8+
- pip (Python package manager)
- [Optional] Docker

### Python Packages

- Flask (or Django, if used in your project)
- SQLAlchemy (if using a database)
- pandas
- matplotlib or plotly (for visualization)
- requests
- Any other dependencies as per your codebase

Install requirements using:
```bash
pip install -r requirements.txt
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Rishika03-03/Supply_Chain.git
cd Supply_Chain
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the project root and add necessary configuration, such as:
```
DATABASE_URL=sqlite:///supply_chain.db
SECRET_KEY=your_secret_key
```

### 4. Initialize the Database (if required)

```bash
python scripts/init_db.py
```
*(Replace with the actual script/command used in your project)*

### 5. Run the Application

For Flask:
```bash
python app.py
```

For Django:
```bash
python manage.py runserver
```

The application will run at `http://127.0.0.1:5000/` (or the port specified in your configuration).

### 6. Access the Dashboard

Open your browser and go to `http://127.0.0.1:5000/` to use the Supply Chain Management System.

---
