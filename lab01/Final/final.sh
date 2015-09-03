#!/bin/sh

python main.py
python FAR.py > FAR
python FRR.py > FRR
python CRR.py > CRR
bash g1.sh
