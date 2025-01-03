# Food and the City API

## Project Overview
This project is a Flask application designed to query and manage a PostgreSQL/PostGIS database. It allows users to retrieve information about movies, filming locations, and nearby restaurants to build customized tourism itineraries based on their favorite movies.

---

## Features
- **PostgreSQL/PostGIS Database**: Stores data related to movies, filming locations, and restaurants.
- **Data Ingestion Pipeline**: Extract, transform, and load (ETL) pipeline to populate the database from datasets.
- **Flask Application**: REST API to query and manage data.

---

## Prerequisites
To set up and run this project, ensure you have the following installed:

- **Docker and Docker Compose**: For database containerization.
- **Python 3.10+**: For running the API and scripts.
- **PostGIS**: Spatial database extension for PostgreSQL (handled via Docker).
- **Jupyter Notebook** (optional): For running the data-ingestion-pipeline.ipynb.

---

## Setup Instructions

run the craete table script
create a .env in the root folder 
run the jupyter notebok
run the update for  geography
open the postmancollection

### 1. Clone the Repository
```bash
git clone <repository-url>
cd food-and-the-city
```

### 2. Set Up the Database

1. **Run Docker Compose**:
   Navigate to the `db` folder and run the following command:
   ```bash
   cd db
   docker-compose up -d
   ```
   This will spin up a PostgreSQL database with the PostGIS extension enabled.

2. **Initialize the Database**:
   Automate the execution of `db/scripts/create_db.sql` by following one of these methods:

   - **Option 1: Manual Execution** (recommended during development):
     Connect to the database container:
     ```bash
     docker exec -it <container_name> psql -U <username> -d <database_name>
     \i /scripts/create_db.sql
     ```

   - **Option 2: Automated Execution**:
     Add the script execution in the `docker-compose.yml` file using a command:
     ```yaml
     command: ["sh", "-c", "psql -U $POSTGRES_USER -d $POSTGRES_DB -f /scripts/create_db.sql"]
     ```
     Ensure that the `scripts` folder is mounted as a volume in the container.

### 3. Ingest Data

1. **Run the Data-Ingestion Pipeline**:
   If you prefer running the pipeline as a script, convert `data-ingestion-pipeline.ipynb` to a Python script:
   ```bash
   jupyter nbconvert --to script data-ingestion-pipeline.ipynb
   python data-ingestion-pipeline.py
   ```
   Alternatively, you can run the notebook directly using Jupyter Notebook.

2. **Input Datasets**:
   Place all datasets in the `/datasets` folder. The pipeline will extract, transform, and load them into the database.

### 4. Run the API

1. **Run Flask Application**:
   Navigate to the `api` folder and start the application:
   ```bash
   python app.py
   ```

2. **Optional: Add Flask to Docker Compose**:
   Integrate the API service into `docker-compose.yml`:
   ```yaml
   services:
     api:
       build: ./api
       ports:
         - "5000:5000"
       depends_on:
         - db
       environment:
         DATABASE_URL: postgresql://<username>:<password>@db/<database>
   ```
   Start the entire stack:
   ```bash
   docker-compose up -d
   ```

### 5. Test the API

1. Use tools like Postman or cURL to test the endpoints. Example:
   ```bash
   curl http://127.0.0.1:5000/movies/
   ```

---

## Questions & Suggestions

### **1. Automating `create_db.sql` Execution**
- **Option 1 (preferred)**: Run manually during setup to avoid unexpected overwrites.
- **Option 2**: Automate using `docker-compose.yml`.

### **2. Running the Data Pipeline**
- Convert the Jupyter Notebook to a Python script for automation (`data-ingestion-pipeline.py`).

### **3. Running the API in Docker**
- Adding the API service to `docker-compose.yml` is highly recommended for consistency and ease of deployment.

---

## File Structure

```
food-and-the-city/
|-- api/
|   |-- app.py          # Flask application
|   |-- database.py     # Database connection
|   |-- models.py       # SQLAlchemy models
|   |-- routes/         # API endpoints
|-- datasets/           # Input datasets
|-- db/
|   |-- docker-compose.yml # Docker setup for PostGIS
|   |-- scripts/        # Database scripts
|-- .env                # Environment variables
|-- .gitignore          # Ignored files and folders
|-- data-ingestion-pipeline.ipynb  # Data ingestion pipeline
```

---

## Example API Calls

### **Get All Movies**
Endpoint:
```bash
GET /movies/
```
Response:
```json
[
  {
    "mov_imdb_id": "tt1234567",
    "mov_title": "Inception",
    "mov_year": 2010,
    "mov_director": "Christopher Nolan",
    "mov_writer": "Christopher Nolan",
    "mov_overview": "A mind-bending thriller.",
    "mov_rating": 8.8,
    "mov_nb_users_ratings": "2M"
  }
]
```

### **Search Movies by Name**
Endpoint:
```bash
GET /movies/?name=Inception
```

---

## Troubleshooting

- **Database Connection Issues**: Ensure the database container is running.
- **Data Pipeline Errors**: Check the dataset format and paths.
- **API Issues**: Inspect logs and verify dependencies.

---

## Next Steps

1. **Enhance the API**: Add endpoints for filming locations and restaurants.
2. **Improve Automation**: Convert all manual processes into Dockerized workflows.
3. **Testing**: Add unit and integration tests for better reliability.

---

Enjoy building your custom tourism itineraries!

