from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

        setup(
                    name="sky_engine",
                    version="1.0.0",
                    author="Tarun Gupta",
                    author_email="tarungupta.iiserkol@gmail.com",
                    description="Synthetic Data Generation Engine for Computer Vision",
                    long_description=long_description,
                    long_description_content_type="text/markdown",
                    url="https://github.com/tarun-qc/sky-engine",
                    package_dir={"": "src"},
                    packages=find_packages(where="src"),
                    python_requires=">=3.8",
                    install_requires=[
                    "numpy>=1.21.0",
                    "torch>=1.9.0",
                    "PyYAML>=5.4.1",
                             ],
                          extras_require={
                         "dev": [
                                 "pytest>=6.2.5",
                                 "black>=21.9b0",
                                 "flake8>=4.0.1",
                                 ],
                                 },
                                 classifiers=[
                                            "Development Status :: 3 - Alpha",
                                            "Intended Audience :: Developers",
                                            "Intended Audience :: Science/Research",
                                            "License :: OSI Approved :: MIT License",
                                            "Programming Language :: Python :: 3",
                                            "Programming Language :: Python :: 3.8",
                                            "Programming Language :: Python :: 3.9",
                                            "Topic :: Scientific/Engineering :: Artificial Intelligence",
                                            ],  )
