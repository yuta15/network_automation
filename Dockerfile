FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /src
RUN pip install poetry
COPY pyproject.toml* poetry.lock* ./
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi
RUN apt update & \
apt upgrade -y
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]