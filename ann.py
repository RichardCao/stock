#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright(C) 2015 [Ruichaung Cao]

from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer

fnn = buildNetwork(2, 6, 1, bias=True, hiddenclass=TanhLayer)

from pybrain.datasets import SupervisedDataSet

ds = SupervisedDataSet(2, 1)
ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

from pybrain.supervised.trainers import BackpropTrainer
trainer = BackpropTrainer(fnn, ds)
trainer.trainEpochs(500)
trainer.trainUntilConvergence()

output = fnn.activate((0, 0))
print output
output = fnn.activate((1, 0))
print output
output = fnn.activate((0, 1))
print output
output = fnn.activate((1, 1))
print output
