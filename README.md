# Apache Airflow Tutorial Project <img src="https://go-skill-icons.vercel.app/api/icons?i=airflow" height="30"/>

This repository contains my practice and implementation of the concepts learned from the Apache Airflow beginner tutorial.

📺 Tutorial link: [YouTube Tutorial](https://youtu.be/K9AnJ9_ZAXE?si=McyhwpzrcMUWMXcq)

The goal of this project is to understand the fundamentals of Airflow, including DAGs, Operators, TaskFlow API, scheduling, hooks, and working with external systems like PostgreSQL.

---

## 📌 Topics Covered

- **Airflow Basics**
  - Installing Airflow using Docker & WSL on Windows
  - DAG structure & best practices
  - Scheduling, start dates, and catchup
- **Operators & TaskFlow**
  - PythonOperator vs BashOperator
  - `@task` decorator & TaskFlow API
  - Passing data between tasks with XComs
  - Multiple outputs from tasks
- **Hooks & Connections**
  - Using PostgresHook for database interactions
  - Setting up Airflow connections via UI
- **ETL Workflow Examples**
  - Extracting data from PostgreSQL
  - Writing CSV files to Docker-mounted folders
  - Logging & debugging tasks
- **Docker & Airflow Setup Tips**
  - Extending Airflow Docker images
  - `requirements.txt` for dependencies
  - Volumes for persistent data storage
  - Backfill vs Catchup

---

## 🚀 Why TaskFlow API?

- Simplifies task communication (built on XComs)
- Automatically handles returned data
- Easier to maintain and test than individual Operators
- Best practice for modern ETL workflows

---

## 🛠️ Requirements

To test and run the Airflow DAGs, ensure you have the following installed:

- **Docker & WSL**
- **Python 3.10+**
- Airflow version: `apache/airflow:3.1.6`
- VSCode
- DBeaver (optional, for testing DB queries)

**Tips for setup:**

- Add volume for persistent data in `docker-compose.yaml`:

```yaml
volumes:
  - ./data:/opt/airflow/data
```

## 📝 Best Practices Learned
  - Use @task over operators when data needs to pass between tasks
  - Use hooks when dealing with external systems (like databases or APIs)
  - Prefer extending Docker images for additional Python packages rather than customizing base images
  - Avoid pushing large data to XComs — use files or DB instead

## 📂 Project Structure
```bash
airflow-test/
│
├─ config/                # Configuration files for Airflow
├─ dags/                  # DAG definitions
├─ data/                  # Output CSVs / data files
├─ logs/                  # Airflow task logs
├─ plugins/               # Custom operators, sensors, or plugins
├─ .env                   # Environment variables for Docker/Airflow
├─ docker-compose.yaml    # Airflow services setup
├─ Dockerfile             # Custom Airflow Docker image
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation
```

## 📸 Some Screenshots
### Dags
<img width="1899" height="1034" alt="DAGs" src="https://github.com/user-attachments/assets/7286fb87-b274-45d9-8b56-4eb85d6b3551" />

### Dag Runs
<img width="1919" height="1031" alt="DAG Runs" src="https://github.com/user-attachments/assets/9465487e-b5fb-44bf-bdcf-ff390ad2f008" />

### Dag Graph View
<img width="801" height="469" alt="Dag Graph View" src="https://github.com/user-attachments/assets/ae7f08e4-4c8c-4092-9558-62627a6beb50" />

### Dag Log
<img width="1919" height="1035" alt="Dag Log" src="https://github.com/user-attachments/assets/99baed41-f780-4b8f-8d37-94cd783a4b95" />
