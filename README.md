# ♻️ RVM Status & Discovery API

This is a Django REST Framework API for managing Reverse Vending Machines (RVMs) across different locations. It allows users to list, create, filter, and view machine status and activity logs.

## 🚀 Features

- Create and list RVM entries with:
  - `location` (city/area)
  - `status` (active/inactive)
  - `last_usage` timestamp
- Filter RVMs by status (e.g., `?status=active`)
- Order results by recent usage (e.g., `?ordering=-last_usage`)
- Search RVMs by location name
- Fully RESTful with proper HTTP status codes
- Ready for token-based authentication (future enhancement)

---

## 🛠️ Setup Instructions
- install Django app 
- install Django framework
- Miagrates it to reach Database 

### 1. Clone the Repository

```bash
git clone https://github.com/rana7azem/rvm-status-api.git
cd rvm-status-api
