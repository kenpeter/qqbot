# -*- coding: utf-8 -*-

# We need to use utf-8
# dot means local???
# 
from .qqbotcls import QQBot, QQBotSlot, QQBotSched, RunBot, _bot
from .qterm import QTerm
from .common import AutoTest
from .mainloop import MainLoop, Put, PutTo, AddWorkerTo
from .qconf import version
Main = RunBot
qqbotslot = QQBotSlot
qqbotsched = QQBotSched
