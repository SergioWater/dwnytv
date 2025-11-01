# 1. Use a Conda-based image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the environment definition file
COPY environment.yml ./

# 2. Create the Conda environment from the YML file
#    This reads 'environment.yml' and creates the 'media-tools' env
RUN conda env create -f environment.yml && \
    conda clean -a -f -y

# 3. Add the new environment's 'bin' to the system PATH
#    This is the line that uses your specific name
ENV PATH=/opt/conda/envs/media-tools/bin:$PATH

# Copy all your project code into the container
COPY . .

# 4. Run the 'main.py' file using the 'media-tools' env python
CMD ["python", "main.py"]