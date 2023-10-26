# Basic CUDA testing in Python

CUDA testing - Using Anaconda, numba and cudatoolkit


## Clone project

```sh
  git clone https://github.com/BrianMorillo/cuda-testing.git
```

## Install libraries

```sh
  conda install numba & conda install cudatoolkit
```
## Run basic CUDA test

```sh
  python run_test.py
```

## Personal Tests
CPU: Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz (8 CPUs), ~3.0GHz

GPU: NVIDIA GeForce RTX 2070 SUPER

Test creates an array of random values of size N and squares all values

```bash
Seconds:
without GPU: 27.630204699999922
with GPU: 0.3603206000002501
```

## Authors
- [Modified Version of GeeksForGeeks Python GPU test](https://www.geeksforgeeks.org/running-python-script-on-gpu/)
- [@BrianMorillo](https://www.github.com/BrianMorillo)