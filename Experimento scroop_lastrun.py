#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.5),
    on noviembre 11, 2026, at 00:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.5'
expName = 'Experimento scroop'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = 'data/' + expInfo['participant'] + '_' + expName + '_' + expInfo['date']
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\Nueva carpeta\\Experimento scroop_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "trial" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='Bienvenido\n\nPresiona la barra espaciadora para comenzar',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_respWelcome = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "blank" ---
    textespacioblanco = visual.TextStim(win=win, name='textespacioblanco',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "fase_negro" ---
    textfaseNegro = visual.TextStim(win=win, name='textfaseNegro',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_respfaseNegro = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "blank" ---
    textespacioblanco = visual.TextStim(win=win, name='textespacioblanco',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "trial2" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='A continuación se le mostrará un ejemplo del experimento para que practique',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_respMensaje = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "practica" ---
    textPractica = visual.TextStim(win=win, name='textPractica',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='named', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_respPractica = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "blank" ---
    textespacioblanco = visual.TextStim(win=win, name='textespacioblanco',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "trial3" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Experimento.\nDebes decir el color de la tinta, no la palabra escrita\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "experimento" ---
    textExperimento = visual.TextStim(win=win, name='textExperimento',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='named', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_respExperimento = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "trial" ---
    # create an object to store info about Routine trial
    trial = data.Routine(
        name='trial',
        components=[textWelcome, key_respWelcome],
    )
    trial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_respWelcome
    key_respWelcome.keys = []
    key_respWelcome.rt = []
    _key_respWelcome_allKeys = []
    # store start times for trial
    trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    trial.tStart = globalClock.getTime(format='float')
    trial.status = STARTED
    thisExp.addData('trial.started', trial.tStart)
    trial.maxDuration = None
    # keep track of which components have finished
    trialComponents = trial.components
    for thisComponent in trial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    thisExp.currentRoutine = trial
    trial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *key_respWelcome* updates
        waitOnFlip = False
        
        # if key_respWelcome is starting this frame...
        if key_respWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_respWelcome.frameNStart = frameN  # exact frame index
            key_respWelcome.tStart = t  # local t and not account for scr refresh
            key_respWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_respWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_respWelcome.started')
            # update status
            key_respWelcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_respWelcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_respWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_respWelcome.status == STARTED and not waitOnFlip:
            theseKeys = key_respWelcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_respWelcome_allKeys.extend(theseKeys)
            if len(_key_respWelcome_allKeys):
                key_respWelcome.keys = _key_respWelcome_allKeys[-1].name  # just the last key pressed
                key_respWelcome.rt = _key_respWelcome_allKeys[-1].rt
                key_respWelcome.duration = _key_respWelcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=trial,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            trial.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if trial.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in trial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for trial
    trial.tStop = globalClock.getTime(format='float')
    trial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('trial.stopped', trial.tStop)
    # check responses
    if key_respWelcome.keys in ['', [], None]:  # No response was made
        key_respWelcome.keys = None
    thisExp.addData('key_respWelcome.keys',key_respWelcome.keys)
    if key_respWelcome.keys != None:  # we had a response
        thisExp.addData('key_respWelcome.rt', key_respWelcome.rt)
        thisExp.addData('key_respWelcome.duration', key_respWelcome.duration)
    thisExp.nextEntry()
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank" ---
    # create an object to store info about Routine blank
    blank = data.Routine(
        name='blank',
        components=[textespacioblanco],
    )
    blank.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for blank
    blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blank.tStart = globalClock.getTime(format='float')
    blank.status = STARTED
    thisExp.addData('blank.started', blank.tStart)
    blank.maxDuration = None
    # keep track of which components have finished
    blankComponents = blank.components
    for thisComponent in blank.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    thisExp.currentRoutine = blank
    blank.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textespacioblanco* updates
        
        # if textespacioblanco is starting this frame...
        if textespacioblanco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textespacioblanco.frameNStart = frameN  # exact frame index
            textespacioblanco.tStart = t  # local t and not account for scr refresh
            textespacioblanco.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textespacioblanco, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textespacioblanco.started')
            # update status
            textespacioblanco.status = STARTED
            textespacioblanco.setAutoDraw(True)
        
        # if textespacioblanco is active this frame...
        if textespacioblanco.status == STARTED:
            # update params
            pass
        
        # if textespacioblanco is stopping this frame...
        if textespacioblanco.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textespacioblanco.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textespacioblanco.tStop = t  # not accounting for scr refresh
                textespacioblanco.tStopRefresh = tThisFlipGlobal  # on global time
                textespacioblanco.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textespacioblanco.stopped')
                # update status
                textespacioblanco.status = FINISHED
                textespacioblanco.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blank,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blank.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blank.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blank.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blank.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blank
    blank.tStop = globalClock.getTime(format='float')
    blank.tStopRefresh = tThisFlipGlobal
    thisExp.addData('blank.stopped', blank.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if blank.maxDurationReached:
        routineTimer.addTime(-blank.maxDuration)
    elif blank.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    bucle_inicio = data.TrialHandler2(
        name='bucle_inicio',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('inicio.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(bucle_inicio)  # add the loop to the experiment
    thisBucle_inicio = bucle_inicio.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_inicio.rgb)
    if thisBucle_inicio != None:
        for paramName in thisBucle_inicio:
            globals()[paramName] = thisBucle_inicio[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBucle_inicio in bucle_inicio:
        bucle_inicio.status = STARTED
        if hasattr(thisBucle_inicio, 'status'):
            thisBucle_inicio.status = STARTED
        currentLoop = bucle_inicio
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBucle_inicio.rgb)
        if thisBucle_inicio != None:
            for paramName in thisBucle_inicio:
                globals()[paramName] = thisBucle_inicio[paramName]
        
        # --- Prepare to start Routine "fase_negro" ---
        # create an object to store info about Routine fase_negro
        fase_negro = data.Routine(
            name='fase_negro',
            components=[textfaseNegro, key_respfaseNegro],
        )
        fase_negro.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textfaseNegro.setText(word)
        # create starting attributes for key_respfaseNegro
        key_respfaseNegro.keys = []
        key_respfaseNegro.rt = []
        _key_respfaseNegro_allKeys = []
        # store start times for fase_negro
        fase_negro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fase_negro.tStart = globalClock.getTime(format='float')
        fase_negro.status = STARTED
        thisExp.addData('fase_negro.started', fase_negro.tStart)
        fase_negro.maxDuration = None
        # keep track of which components have finished
        fase_negroComponents = fase_negro.components
        for thisComponent in fase_negro.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fase_negro" ---
        thisExp.currentRoutine = fase_negro
        fase_negro.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBucle_inicio, 'status') and thisBucle_inicio.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textfaseNegro* updates
            
            # if textfaseNegro is starting this frame...
            if textfaseNegro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textfaseNegro.frameNStart = frameN  # exact frame index
                textfaseNegro.tStart = t  # local t and not account for scr refresh
                textfaseNegro.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textfaseNegro, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textfaseNegro.started')
                # update status
                textfaseNegro.status = STARTED
                textfaseNegro.setAutoDraw(True)
            
            # if textfaseNegro is active this frame...
            if textfaseNegro.status == STARTED:
                # update params
                pass
            
            # if textfaseNegro is stopping this frame...
            if textfaseNegro.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textfaseNegro.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textfaseNegro.tStop = t  # not accounting for scr refresh
                    textfaseNegro.tStopRefresh = tThisFlipGlobal  # on global time
                    textfaseNegro.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textfaseNegro.stopped')
                    # update status
                    textfaseNegro.status = FINISHED
                    textfaseNegro.setAutoDraw(False)
            
            # *key_respfaseNegro* updates
            waitOnFlip = False
            
            # if key_respfaseNegro is starting this frame...
            if key_respfaseNegro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respfaseNegro.frameNStart = frameN  # exact frame index
                key_respfaseNegro.tStart = t  # local t and not account for scr refresh
                key_respfaseNegro.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respfaseNegro, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_respfaseNegro.started')
                # update status
                key_respfaseNegro.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respfaseNegro.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respfaseNegro.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respfaseNegro.status == STARTED and not waitOnFlip:
                theseKeys = key_respfaseNegro.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_respfaseNegro_allKeys.extend(theseKeys)
                if len(_key_respfaseNegro_allKeys):
                    key_respfaseNegro.keys = _key_respfaseNegro_allKeys[-1].name  # just the last key pressed
                    key_respfaseNegro.rt = _key_respfaseNegro_allKeys[-1].rt
                    key_respfaseNegro.duration = _key_respfaseNegro_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fase_negro,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fase_negro.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fase_negro.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fase_negro.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fase_negro" ---
        for thisComponent in fase_negro.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fase_negro
        fase_negro.tStop = globalClock.getTime(format='float')
        fase_negro.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fase_negro.stopped', fase_negro.tStop)
        # check responses
        if key_respfaseNegro.keys in ['', [], None]:  # No response was made
            key_respfaseNegro.keys = None
        bucle_inicio.addData('key_respfaseNegro.keys',key_respfaseNegro.keys)
        if key_respfaseNegro.keys != None:  # we had a response
            bucle_inicio.addData('key_respfaseNegro.rt', key_respfaseNegro.rt)
            bucle_inicio.addData('key_respfaseNegro.duration', key_respfaseNegro.duration)
        # the Routine "fase_negro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisBucle_inicio as finished
        if hasattr(thisBucle_inicio, 'status'):
            thisBucle_inicio.status = FINISHED
        # if awaiting a pause, pause now
        if bucle_inicio.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            bucle_inicio.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'bucle_inicio'
    bucle_inicio.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if bucle_inicio.trialList in ([], [None], None):
        params = []
    else:
        params = bucle_inicio.trialList[0].keys()
    # save data for this loop
    bucle_inicio.saveAsExcel(filename + '.xlsx', sheetName='bucle_inicio',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "blank" ---
    # create an object to store info about Routine blank
    blank = data.Routine(
        name='blank',
        components=[textespacioblanco],
    )
    blank.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for blank
    blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blank.tStart = globalClock.getTime(format='float')
    blank.status = STARTED
    thisExp.addData('blank.started', blank.tStart)
    blank.maxDuration = None
    # keep track of which components have finished
    blankComponents = blank.components
    for thisComponent in blank.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    thisExp.currentRoutine = blank
    blank.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textespacioblanco* updates
        
        # if textespacioblanco is starting this frame...
        if textespacioblanco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textespacioblanco.frameNStart = frameN  # exact frame index
            textespacioblanco.tStart = t  # local t and not account for scr refresh
            textespacioblanco.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textespacioblanco, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textespacioblanco.started')
            # update status
            textespacioblanco.status = STARTED
            textespacioblanco.setAutoDraw(True)
        
        # if textespacioblanco is active this frame...
        if textespacioblanco.status == STARTED:
            # update params
            pass
        
        # if textespacioblanco is stopping this frame...
        if textespacioblanco.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textespacioblanco.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textespacioblanco.tStop = t  # not accounting for scr refresh
                textespacioblanco.tStopRefresh = tThisFlipGlobal  # on global time
                textespacioblanco.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textespacioblanco.stopped')
                # update status
                textespacioblanco.status = FINISHED
                textespacioblanco.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blank,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blank.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blank.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blank.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blank.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blank
    blank.tStop = globalClock.getTime(format='float')
    blank.tStopRefresh = tThisFlipGlobal
    thisExp.addData('blank.stopped', blank.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if blank.maxDurationReached:
        routineTimer.addTime(-blank.maxDuration)
    elif blank.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "trial2" ---
    # create an object to store info about Routine trial2
    trial2 = data.Routine(
        name='trial2',
        components=[text_2, key_respMensaje],
    )
    trial2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_respMensaje
    key_respMensaje.keys = []
    key_respMensaje.rt = []
    _key_respMensaje_allKeys = []
    # store start times for trial2
    trial2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    trial2.tStart = globalClock.getTime(format='float')
    trial2.status = STARTED
    thisExp.addData('trial2.started', trial2.tStart)
    trial2.maxDuration = None
    # keep track of which components have finished
    trial2Components = trial2.components
    for thisComponent in trial2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial2" ---
    thisExp.currentRoutine = trial2
    trial2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *key_respMensaje* updates
        waitOnFlip = False
        
        # if key_respMensaje is starting this frame...
        if key_respMensaje.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_respMensaje.frameNStart = frameN  # exact frame index
            key_respMensaje.tStart = t  # local t and not account for scr refresh
            key_respMensaje.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_respMensaje, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_respMensaje.started')
            # update status
            key_respMensaje.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_respMensaje.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_respMensaje.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_respMensaje.status == STARTED and not waitOnFlip:
            theseKeys = key_respMensaje.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_respMensaje_allKeys.extend(theseKeys)
            if len(_key_respMensaje_allKeys):
                key_respMensaje.keys = _key_respMensaje_allKeys[-1].name  # just the last key pressed
                key_respMensaje.rt = _key_respMensaje_allKeys[-1].rt
                key_respMensaje.duration = _key_respMensaje_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=trial2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            trial2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if trial2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in trial2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial2" ---
    for thisComponent in trial2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for trial2
    trial2.tStop = globalClock.getTime(format='float')
    trial2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('trial2.stopped', trial2.tStop)
    # check responses
    if key_respMensaje.keys in ['', [], None]:  # No response was made
        key_respMensaje.keys = None
    thisExp.addData('key_respMensaje.keys',key_respMensaje.keys)
    if key_respMensaje.keys != None:  # we had a response
        thisExp.addData('key_respMensaje.rt', key_respMensaje.rt)
        thisExp.addData('key_respMensaje.duration', key_respMensaje.duration)
    thisExp.nextEntry()
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    bucle_practica = data.TrialHandler2(
        name='bucle_practica',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('practica.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(bucle_practica)  # add the loop to the experiment
    thisBucle_practica = bucle_practica.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_practica.rgb)
    if thisBucle_practica != None:
        for paramName in thisBucle_practica:
            globals()[paramName] = thisBucle_practica[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBucle_practica in bucle_practica:
        bucle_practica.status = STARTED
        if hasattr(thisBucle_practica, 'status'):
            thisBucle_practica.status = STARTED
        currentLoop = bucle_practica
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBucle_practica.rgb)
        if thisBucle_practica != None:
            for paramName in thisBucle_practica:
                globals()[paramName] = thisBucle_practica[paramName]
        
        # --- Prepare to start Routine "practica" ---
        # create an object to store info about Routine practica
        practica = data.Routine(
            name='practica',
            components=[textPractica, key_respPractica],
        )
        practica.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textPractica.setColor(color, colorSpace='named')
        textPractica.setText(word
        )
        # create starting attributes for key_respPractica
        key_respPractica.keys = []
        key_respPractica.rt = []
        _key_respPractica_allKeys = []
        # store start times for practica
        practica.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practica.tStart = globalClock.getTime(format='float')
        practica.status = STARTED
        thisExp.addData('practica.started', practica.tStart)
        practica.maxDuration = None
        # keep track of which components have finished
        practicaComponents = practica.components
        for thisComponent in practica.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practica" ---
        thisExp.currentRoutine = practica
        practica.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBucle_practica, 'status') and thisBucle_practica.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textPractica* updates
            
            # if textPractica is starting this frame...
            if textPractica.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textPractica.frameNStart = frameN  # exact frame index
                textPractica.tStart = t  # local t and not account for scr refresh
                textPractica.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textPractica, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textPractica.started')
                # update status
                textPractica.status = STARTED
                textPractica.setAutoDraw(True)
            
            # if textPractica is active this frame...
            if textPractica.status == STARTED:
                # update params
                pass
            
            # *key_respPractica* updates
            waitOnFlip = False
            
            # if key_respPractica is starting this frame...
            if key_respPractica.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respPractica.frameNStart = frameN  # exact frame index
                key_respPractica.tStart = t  # local t and not account for scr refresh
                key_respPractica.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respPractica, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_respPractica.started')
                # update status
                key_respPractica.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respPractica.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respPractica.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respPractica.status == STARTED and not waitOnFlip:
                theseKeys = key_respPractica.getKeys(keyList=['v','a','a','n','r'], ignoreKeys=["escape"], waitRelease=False)
                _key_respPractica_allKeys.extend(theseKeys)
                if len(_key_respPractica_allKeys):
                    key_respPractica.keys = _key_respPractica_allKeys[-1].name  # just the last key pressed
                    key_respPractica.rt = _key_respPractica_allKeys[-1].rt
                    key_respPractica.duration = _key_respPractica_allKeys[-1].duration
                    # was this correct?
                    if (key_respPractica.keys == str(color)) or (key_respPractica.keys == color):
                        key_respPractica.corr = 1
                    else:
                        key_respPractica.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practica,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                practica.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if practica.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in practica.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practica" ---
        for thisComponent in practica.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practica
        practica.tStop = globalClock.getTime(format='float')
        practica.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practica.stopped', practica.tStop)
        # check responses
        if key_respPractica.keys in ['', [], None]:  # No response was made
            key_respPractica.keys = None
            # was no response the correct answer?!
            if str(color).lower() == 'none':
               key_respPractica.corr = 1;  # correct non-response
            else:
               key_respPractica.corr = 0;  # failed to respond (incorrectly)
        # store data for bucle_practica (TrialHandler)
        bucle_practica.addData('key_respPractica.keys',key_respPractica.keys)
        bucle_practica.addData('key_respPractica.corr', key_respPractica.corr)
        if key_respPractica.keys != None:  # we had a response
            bucle_practica.addData('key_respPractica.rt', key_respPractica.rt)
            bucle_practica.addData('key_respPractica.duration', key_respPractica.duration)
        # the Routine "practica" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisBucle_practica as finished
        if hasattr(thisBucle_practica, 'status'):
            thisBucle_practica.status = FINISHED
        # if awaiting a pause, pause now
        if bucle_practica.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            bucle_practica.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'bucle_practica'
    bucle_practica.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if bucle_practica.trialList in ([], [None], None):
        params = []
    else:
        params = bucle_practica.trialList[0].keys()
    # save data for this loop
    bucle_practica.saveAsExcel(filename + '.xlsx', sheetName='bucle_practica',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "blank" ---
    # create an object to store info about Routine blank
    blank = data.Routine(
        name='blank',
        components=[textespacioblanco],
    )
    blank.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for blank
    blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blank.tStart = globalClock.getTime(format='float')
    blank.status = STARTED
    thisExp.addData('blank.started', blank.tStart)
    blank.maxDuration = None
    # keep track of which components have finished
    blankComponents = blank.components
    for thisComponent in blank.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    thisExp.currentRoutine = blank
    blank.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textespacioblanco* updates
        
        # if textespacioblanco is starting this frame...
        if textespacioblanco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textespacioblanco.frameNStart = frameN  # exact frame index
            textespacioblanco.tStart = t  # local t and not account for scr refresh
            textespacioblanco.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textespacioblanco, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textespacioblanco.started')
            # update status
            textespacioblanco.status = STARTED
            textespacioblanco.setAutoDraw(True)
        
        # if textespacioblanco is active this frame...
        if textespacioblanco.status == STARTED:
            # update params
            pass
        
        # if textespacioblanco is stopping this frame...
        if textespacioblanco.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textespacioblanco.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textespacioblanco.tStop = t  # not accounting for scr refresh
                textespacioblanco.tStopRefresh = tThisFlipGlobal  # on global time
                textespacioblanco.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textespacioblanco.stopped')
                # update status
                textespacioblanco.status = FINISHED
                textespacioblanco.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blank,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blank.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blank.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blank.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blank.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blank
    blank.tStop = globalClock.getTime(format='float')
    blank.tStopRefresh = tThisFlipGlobal
    thisExp.addData('blank.stopped', blank.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if blank.maxDurationReached:
        routineTimer.addTime(-blank.maxDuration)
    elif blank.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "trial3" ---
    # create an object to store info about Routine trial3
    trial3 = data.Routine(
        name='trial3',
        components=[text_3, key_resp],
    )
    trial3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for trial3
    trial3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    trial3.tStart = globalClock.getTime(format='float')
    trial3.status = STARTED
    thisExp.addData('trial3.started', trial3.tStart)
    trial3.maxDuration = None
    # keep track of which components have finished
    trial3Components = trial3.components
    for thisComponent in trial3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial3" ---
    thisExp.currentRoutine = trial3
    trial3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=trial3,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            trial3.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if trial3.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in trial3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial3" ---
    for thisComponent in trial3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for trial3
    trial3.tStop = globalClock.getTime(format='float')
    trial3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('trial3.stopped', trial3.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    bucle_experimento = data.TrialHandler2(
        name='bucle_experimento',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('experimento scroop.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(bucle_experimento)  # add the loop to the experiment
    thisBucle_experimento = bucle_experimento.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_experimento.rgb)
    if thisBucle_experimento != None:
        for paramName in thisBucle_experimento:
            globals()[paramName] = thisBucle_experimento[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBucle_experimento in bucle_experimento:
        bucle_experimento.status = STARTED
        if hasattr(thisBucle_experimento, 'status'):
            thisBucle_experimento.status = STARTED
        currentLoop = bucle_experimento
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBucle_experimento.rgb)
        if thisBucle_experimento != None:
            for paramName in thisBucle_experimento:
                globals()[paramName] = thisBucle_experimento[paramName]
        
        # --- Prepare to start Routine "experimento" ---
        # create an object to store info about Routine experimento
        experimento = data.Routine(
            name='experimento',
            components=[textExperimento, key_respExperimento],
        )
        experimento.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textExperimento.setColor(color, colorSpace='named')
        textExperimento.setText(word
        )
        # create starting attributes for key_respExperimento
        key_respExperimento.keys = []
        key_respExperimento.rt = []
        _key_respExperimento_allKeys = []
        # store start times for experimento
        experimento.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        experimento.tStart = globalClock.getTime(format='float')
        experimento.status = STARTED
        thisExp.addData('experimento.started', experimento.tStart)
        experimento.maxDuration = None
        # keep track of which components have finished
        experimentoComponents = experimento.components
        for thisComponent in experimento.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "experimento" ---
        thisExp.currentRoutine = experimento
        experimento.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBucle_experimento, 'status') and thisBucle_experimento.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textExperimento* updates
            
            # if textExperimento is starting this frame...
            if textExperimento.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textExperimento.frameNStart = frameN  # exact frame index
                textExperimento.tStart = t  # local t and not account for scr refresh
                textExperimento.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textExperimento, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textExperimento.started')
                # update status
                textExperimento.status = STARTED
                textExperimento.setAutoDraw(True)
            
            # if textExperimento is active this frame...
            if textExperimento.status == STARTED:
                # update params
                pass
            
            # *key_respExperimento* updates
            waitOnFlip = False
            
            # if key_respExperimento is starting this frame...
            if key_respExperimento.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respExperimento.frameNStart = frameN  # exact frame index
                key_respExperimento.tStart = t  # local t and not account for scr refresh
                key_respExperimento.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respExperimento, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_respExperimento.started')
                # update status
                key_respExperimento.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respExperimento.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respExperimento.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respExperimento.status == STARTED and not waitOnFlip:
                theseKeys = key_respExperimento.getKeys(keyList=['a','n','v','r','m','g','b','c'], ignoreKeys=["escape"], waitRelease=False)
                _key_respExperimento_allKeys.extend(theseKeys)
                if len(_key_respExperimento_allKeys):
                    key_respExperimento.keys = _key_respExperimento_allKeys[-1].name  # just the last key pressed
                    key_respExperimento.rt = _key_respExperimento_allKeys[-1].rt
                    key_respExperimento.duration = _key_respExperimento_allKeys[-1].duration
                    # was this correct?
                    if (key_respExperimento.keys == str(color)) or (key_respExperimento.keys == color):
                        key_respExperimento.corr = 1
                    else:
                        key_respExperimento.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=experimento,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                experimento.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if experimento.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in experimento.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experimento" ---
        for thisComponent in experimento.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for experimento
        experimento.tStop = globalClock.getTime(format='float')
        experimento.tStopRefresh = tThisFlipGlobal
        thisExp.addData('experimento.stopped', experimento.tStop)
        # check responses
        if key_respExperimento.keys in ['', [], None]:  # No response was made
            key_respExperimento.keys = None
            # was no response the correct answer?!
            if str(color).lower() == 'none':
               key_respExperimento.corr = 1;  # correct non-response
            else:
               key_respExperimento.corr = 0;  # failed to respond (incorrectly)
        # store data for bucle_experimento (TrialHandler)
        bucle_experimento.addData('key_respExperimento.keys',key_respExperimento.keys)
        bucle_experimento.addData('key_respExperimento.corr', key_respExperimento.corr)
        if key_respExperimento.keys != None:  # we had a response
            bucle_experimento.addData('key_respExperimento.rt', key_respExperimento.rt)
            bucle_experimento.addData('key_respExperimento.duration', key_respExperimento.duration)
        # the Routine "experimento" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisBucle_experimento as finished
        if hasattr(thisBucle_experimento, 'status'):
            thisBucle_experimento.status = FINISHED
        # if awaiting a pause, pause now
        if bucle_experimento.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            bucle_experimento.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'bucle_experimento'
    bucle_experimento.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if bucle_experimento.trialList in ([], [None], None):
        params = []
    else:
        params = bucle_experimento.trialList[0].keys()
    # save data for this loop
    bucle_experimento.saveAsExcel(filename + '.xlsx', sheetName='bucle_experimento',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
