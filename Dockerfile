FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
COPY requirements.lock ./
COPY team_c ./team_c
RUN pip install --no-cache-dir -r requirements.lock && pip install --no-cache-dir --no-deps .
EXPOSE 8000
CMD ["uvicorn", "wisp_team_c.api:app", "--host", "0.0.0.0", "--port", "8000"]
