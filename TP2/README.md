# TP 2: Algoritmos genéticos

## Dependencias

- Python 3+
- pip

# Ejecución

```
pip install -r requirements.txt
python number_puzzle_solver.py
```

# Config.json file

In order to fill the config file, if a certain parameter is not needed for the current specifications, please fill it anyways either with a random value or with '0'.

### Parent selection method valid names:

- random
- sorted
- balanced

### Break criteria valid names:

- generation_count
- time
- acceptable_solution
- constant_solution

### Cross method valid names:

- uniform
- multiple
- simple

### Mutation method valid names:

- uniform
- normal

### Selection method valid names:

- stochastic
- elite
- roulette
- rank
- tournament
- boltzmann
- truncated
