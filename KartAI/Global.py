# -*- coding: utf-8 -*-
# KartAI https://github.com/eritzyg/KartAI/
# Copyright (c) 2017 Eritz Yerga Gutierrez and Iker García Ferrero
# MIT License https://github.com/eritzyg/KartAI/blob/master/LICENSE

def init():
    #Engine global
    global eventDelta
    global renderer
    
    #Control vars
    global press
    global disableScaling
    global HUDEnabled
    global EnableTrackmap
    global renderTrackmap
    global renderCollisionLines
    global ForceReset
    
    #Q-Learning control vars
    global BlockLearning
    global Try
    global FLC
    
    #### Init engine globals ####
    eventDelta = 0.0
    renderer = 1
    
    #### Init control vars ####
    press = 0
    disableScaling = False
    HUDEnabled = True
    EnableTrackmap = True
    renderTrackmap = False
    renderCollisionLines = True
    ForceReset = False
    
    #### Init Q-Learning control vars ####
    BlockLearning = False
    Try = 1
    FLC = False
