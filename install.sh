#!/bin/bash

# Install torch-scatter
pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.10.0+cpu.html

# Install torch-sparse
pip install torch-sparse -f https://pytorch-geometric.com/whl/torch-1.10.0+cpu.html

# Install torch-cluster
pip install torch-cluster -f https://pytorch-geometric.com/whl/torch-1.10.0+cpu.html

# Install torch-spline-conv (optional)
pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.10.0+cpu.html

# Install torch-geometric
pip install torch-geometric