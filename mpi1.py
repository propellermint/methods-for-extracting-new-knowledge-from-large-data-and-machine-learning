#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from mpi4py import MPI

import numpy as np
import pandas as pd
from mpi4py import MPI


size = 100
pd.DataFrame(np.random.random(size=size),columns=['x']).to_csv('x0.csv')
pd.DataFrame(np.random.random(size=size),columns=['x']).to_csv('x1.csv')

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 1:
    data = pd.read_csv('x1.csv')
    res = data.x.sum()
    comm.send(res, dest=0)
elif rank == 0:
    data = pd.read_csv('x0.csv')
    x_0 = data.x.sum()
    x_1 = comm.recv(source=1)
    print("Сумма всех элементов X = ", x_0 + x_1)


