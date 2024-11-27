from setuptools import setup, find_packages

setup(
    name='Sales-Prediction-with-Deep-Learning',
    version='1.0',
    author='Ilyes DJERFAF',
    author_email='idjerfaf@gmail.com',
    description='Sales Prediction with Deep Learning',
    url='https://github.com/ilyesdjerfaf/Sales-Prediction-with-Deep-Learning',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy==1.26.4',
        'pandas==2.2.2',
        'matplotlib==3.8',
        'tqdm==4.66.1',
        'dash==2.8.1',
        'plotly==5.24.1',
        'flake8==4.0.1',
    ],
    python_requires='>=3.10',
)
