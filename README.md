# Chartd - Energy Data Visualization Dashboard

A full-stack web application that visualizes Japan's electricity generation and consumption data across different regions and time periods.

## Features

- **Interactive Visualizations**: Stacked area charts and line charts showing energy generation by source
- **Time Range Selection**: Interactive slider to select custom date ranges (2022-2024)
- **Regional Data**: View data for different regions of Japan
- **Bilingual Support**: Toggle between Japanese and English
- **Data Export**: Download data as CSV files
- **Energy Source Tracking**: Monitor renewable and non-renewable energy sources

## Quick Start

### Option 1: Docker (Recommended)

The easiest way to run the application is using Docker:

```bash
# Make sure Docker Desktop is running
docker compose up --build
```

Then open your browser to:
- Frontend: `http://localhost`
- Backend API: `http://localhost:3000`

For detailed Docker instructions, see [DOCKER.md](DOCKER.md)

### Option 2: Local Development

#### Backend: Flask

1. Navigate to the server folder and create a Python virtual environment:
```bash
cd server
python3 -m venv venv
```

2. Activate the environment and install dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the server:
```bash
python3 app.py
```

The backend will be available at `http://localhost:3000`

#### Frontend: Svelte

1. Open a new terminal tab and navigate to the client folder:
```bash
cd client
npm install
```

2. Run the development server:
```bash
npm run dev
```

3. View the app at `http://localhost:5173`

## Project Structure

```
chartd/
├── client/                 # Frontend Svelte application
│   ├── src/
│   │   ├── App.svelte     # Main application component
│   │   └── lib/           # Chart components
│   ├── Dockerfile         # Frontend container configuration
│   └── nginx.conf         # Nginx configuration for production
├── server/                # Backend Flask API
│   ├── app.py            # Main Flask application
│   ├── data/             # Energy data files (2022-2024)
│   ├── Dockerfile        # Backend container configuration
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Docker orchestration
└── DOCKER.md            # Detailed Docker documentation
```

## Technology Stack

**Frontend:**
- Svelte
- Vite
- D3.js (for visualizations)

**Backend:**
- Flask
- Pandas (for data processing)
- Flask-CORS

**Deployment:**
- Docker
- Nginx (for serving frontend in production)

## API Endpoints

### GET `/api/data`

Fetch energy data with the following query parameters:

- `start_date`: Start date (YYYY-MM-DD)
- `end_date`: End date (YYYY-MM-DD)
- `region`: Region name (e.g., "japan")
- `aggregation`: Data aggregation level ("hourly", "daily", "weekly", "monthly")

Example:
```bash
curl "http://localhost:3000/api/data?start_date=2024-04-01&end_date=2024-04-15&region=japan&aggregation=hourly"
```

## Environment Variables

### Client

Create a `.env` file in the `client/` directory:

```env
VITE_API_BASE_URL=http://localhost:3000
```

### Server

The server uses environment variables set in the Docker configuration or can be set locally:

```env
FLASK_APP=app.py
PYTHONUNBUFFERED=1
```

## Development

### Running Tests

```bash
# Backend tests (if available)
cd server
pytest

# Frontend tests (if available)
cd client
npm test
```

### Building for Production

#### Using Docker
```bash
docker compose up --build
```

#### Manual Build
```bash
# Build frontend
cd client
npm run build

# The built files will be in client/dist/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions, please open an issue on the GitHub repository.
