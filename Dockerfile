FROM quay.io/astronomer/astro-runtime:11.1.0

# install soda into a virtual environment
RUN python -m venv soda_venv && source soda_venv/bin/activate && \
    pip install --no-cache-dir soda-core-bigquery==3.3.1 &&\
    pip install --no-cache-dir soda-core-scientific==3.3.1 && deactivate