# eCommerce Recommendation App
This repo contains an eCommerce Recommendation App built using FastAPI, NextJS, and a SingleStore database. In this app, we simulate a dashboard for an online store owner. The dashboard displays a card for each incoming order, showing details about the user and the purchased product. Additionally, each card includes a button that, when clicked, recommends a new product for that user. 





## Getting Started
1. Navigate to the root of the project directory and create a virtual environment: ```python -m venv venv```
2. Activate this virtual environment: ```source venv/bin/activate```
3. Install the necessary packages: ```pip install -r requirements.txt```
4. Export your OpenAI key: ```export OPENAI_API_KEY={your_api_key}```
5. Export your SingleStore connection string: ```export ENGINE_LINK={your_engine_link}```

## Starting up the Backend
Navigate to the backend folder and run the following command:

```uvicorn main:app --reload```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the root endpoint.


## Starting up the Frontend
Navigate to the frontend folder and run the following command to set up a development server:

```npm run dev```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.


