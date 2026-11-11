/*************************** 
 * Experimento Scroop *
 ***************************/

import { core, data, sound, util, visual, hardware } from './psychojs-2026.2.5.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Experimento scroop';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(trialRoutineBegin());
flowScheduler.add(trialRoutineEachFrame());
flowScheduler.add(trialRoutineEnd());
flowScheduler.add(blankRoutineBegin());
flowScheduler.add(blankRoutineEachFrame());
flowScheduler.add(blankRoutineEnd());
const bucle_inicioLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(bucle_inicioLoopBegin(bucle_inicioLoopScheduler));
flowScheduler.add(bucle_inicioLoopScheduler);
flowScheduler.add(bucle_inicioLoopEnd);


flowScheduler.add(blankRoutineBegin());
flowScheduler.add(blankRoutineEachFrame());
flowScheduler.add(blankRoutineEnd());
flowScheduler.add(trial2RoutineBegin());
flowScheduler.add(trial2RoutineEachFrame());
flowScheduler.add(trial2RoutineEnd());
const bucle_practicaLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(bucle_practicaLoopBegin(bucle_practicaLoopScheduler));
flowScheduler.add(bucle_practicaLoopScheduler);
flowScheduler.add(bucle_practicaLoopEnd);


flowScheduler.add(blankRoutineBegin());
flowScheduler.add(blankRoutineEachFrame());
flowScheduler.add(blankRoutineEnd());
flowScheduler.add(trial3RoutineBegin());
flowScheduler.add(trial3RoutineEachFrame());
flowScheduler.add(trial3RoutineEnd());
const bucle_experimentoLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(bucle_experimentoLoopBegin(bucle_experimentoLoopScheduler));
flowScheduler.add(bucle_experimentoLoopScheduler);
flowScheduler.add(bucle_experimentoLoopEnd);


flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'inicio.xlsx', 'path': 'inicio.xlsx'},
    {'name': 'practica.xlsx', 'path': 'practica.xlsx'},
    {'name': 'experimento scroop.xlsx', 'path': 'experimento scroop.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + ((((("data/" + expInfo["participant"]) + "_") + expName) + "_") + expInfo["date"]));
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var trialClock;
var textWelcome;
var key_respWelcome;
var blankClock;
var textespacioblanco;
var fase_negroClock;
var textfaseNegro;
var key_respfaseNegro;
var trial2Clock;
var text_2;
var key_respMensaje;
var practicaClock;
var textPractica;
var key_respPractica;
var trial3Clock;
var text_3;
var key_resp;
var experimentoClock;
var textExperimento;
var key_respExperimento;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Bienvenido\n\nPresiona la barra espaciadora para comenzar',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  key_respWelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blank"
  blankClock = new util.Clock();
  textespacioblanco = new visual.TextStim({
    win: psychoJS.window,
    name: 'textespacioblanco',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fase_negro"
  fase_negroClock = new util.Clock();
  textfaseNegro = new visual.TextStim({
    win: psychoJS.window,
    name: 'textfaseNegro',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  key_respfaseNegro = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial2"
  trial2Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'A continuación se le mostrará un ejemplo del experimento para que practique',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  key_respMensaje = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practica"
  practicaClock = new util.Clock();
  textPractica = new visual.TextStim({
    win: psychoJS.window,
    name: 'textPractica',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_respPractica = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial3"
  trial3Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Experimento.\nDebes decir el color de la tinta, no la palabra escrita\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "experimento"
  experimentoClock = new util.Clock();
  textExperimento = new visual.TextStim({
    win: psychoJS.window,
    name: 'textExperimento',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_respExperimento = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var trialMaxDurationReached;
var _key_respWelcome_allKeys;
var trialMaxDuration;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialClock.reset();
    routineTimer.reset();
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    key_respWelcome.keys = undefined;
    key_respWelcome.rt = undefined;
    _key_respWelcome_allKeys = [];
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(textWelcome);
    trialComponents.push(key_respWelcome);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }
    
    
    // if textWelcome is active this frame...
    if (textWelcome.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_respWelcome* updates
    if (t >= 0.0 && key_respWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respWelcome.tStart = t;  // (not accounting for frame time here)
      key_respWelcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respWelcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respWelcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respWelcome.clearEvents(); });
    }
    
    // if key_respWelcome is active this frame...
    if (key_respWelcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respWelcome.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_respWelcome_allKeys = _key_respWelcome_allKeys.concat(theseKeys);
      if (_key_respWelcome_allKeys.length > 0) {
        key_respWelcome.keys = _key_respWelcome_allKeys[_key_respWelcome_allKeys.length - 1].name;  // just the last key pressed
        key_respWelcome.rt = _key_respWelcome_allKeys[_key_respWelcome_allKeys.length - 1].rt;
        key_respWelcome.duration = _key_respWelcome_allKeys[_key_respWelcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respWelcome.corr, level);
    }
    psychoJS.experiment.addData('key_respWelcome.keys', key_respWelcome.keys);
    if (typeof key_respWelcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respWelcome.rt', key_respWelcome.rt);
        psychoJS.experiment.addData('key_respWelcome.duration', key_respWelcome.duration);
        routineTimer.reset();
        }
    
    key_respWelcome.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blankMaxDurationReached;
var blankMaxDuration;
var blankComponents;
function blankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    blankClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    blankMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('blank.started', globalClock.getTime());
    blankMaxDuration = null
    // keep track of which components have finished
    blankComponents = [];
    blankComponents.push(textespacioblanco);
    
    for (const thisComponent of blankComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function blankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank' ---
    // get current time
    t = blankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textespacioblanco* updates
    if (t >= 0.0 && textespacioblanco.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textespacioblanco.tStart = t;  // (not accounting for frame time here)
      textespacioblanco.frameNStart = frameN;  // exact frame index
      
      textespacioblanco.setAutoDraw(true);
    }
    
    
    // if textespacioblanco is active this frame...
    if (textespacioblanco.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textespacioblanco.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      textespacioblanco.tStop = t;  // not accounting for scr refresh
      textespacioblanco.frameNStop = frameN;  // exact frame index
      // update status
      textespacioblanco.status = PsychoJS.Status.FINISHED;
      textespacioblanco.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blankComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank' ---
    for (const thisComponent of blankComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blank.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (blankMaxDurationReached) {
        blankClock.add(blankMaxDuration);
    } else {
        blankClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var bucle_inicio;
function bucle_inicioLoopBegin(bucle_inicioLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    bucle_inicio = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'inicio.xlsx',
      seed: undefined, name: 'bucle_inicio'
    });
    psychoJS.experiment.addLoop(bucle_inicio); // add the loop to the experiment
    currentLoop = bucle_inicio;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBucle_inicio of bucle_inicio) {
      snapshot = bucle_inicio.getSnapshot();
      bucle_inicioLoopScheduler.add(importConditions(snapshot));
      bucle_inicioLoopScheduler.add(fase_negroRoutineBegin(snapshot));
      bucle_inicioLoopScheduler.add(fase_negroRoutineEachFrame());
      bucle_inicioLoopScheduler.add(fase_negroRoutineEnd(snapshot));
      bucle_inicioLoopScheduler.add(bucle_inicioLoopEndIteration(bucle_inicioLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function bucle_inicioLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(bucle_inicio);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function bucle_inicioLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var bucle_practica;
function bucle_practicaLoopBegin(bucle_practicaLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    bucle_practica = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'practica.xlsx',
      seed: undefined, name: 'bucle_practica'
    });
    psychoJS.experiment.addLoop(bucle_practica); // add the loop to the experiment
    currentLoop = bucle_practica;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBucle_practica of bucle_practica) {
      snapshot = bucle_practica.getSnapshot();
      bucle_practicaLoopScheduler.add(importConditions(snapshot));
      bucle_practicaLoopScheduler.add(practicaRoutineBegin(snapshot));
      bucle_practicaLoopScheduler.add(practicaRoutineEachFrame());
      bucle_practicaLoopScheduler.add(practicaRoutineEnd(snapshot));
      bucle_practicaLoopScheduler.add(bucle_practicaLoopEndIteration(bucle_practicaLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function bucle_practicaLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(bucle_practica);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function bucle_practicaLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var bucle_experimento;
function bucle_experimentoLoopBegin(bucle_experimentoLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    bucle_experimento = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'experimento scroop.xlsx',
      seed: undefined, name: 'bucle_experimento'
    });
    psychoJS.experiment.addLoop(bucle_experimento); // add the loop to the experiment
    currentLoop = bucle_experimento;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBucle_experimento of bucle_experimento) {
      snapshot = bucle_experimento.getSnapshot();
      bucle_experimentoLoopScheduler.add(importConditions(snapshot));
      bucle_experimentoLoopScheduler.add(experimentoRoutineBegin(snapshot));
      bucle_experimentoLoopScheduler.add(experimentoRoutineEachFrame());
      bucle_experimentoLoopScheduler.add(experimentoRoutineEnd(snapshot));
      bucle_experimentoLoopScheduler.add(bucle_experimentoLoopEndIteration(bucle_experimentoLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function bucle_experimentoLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(bucle_experimento);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function bucle_experimentoLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fase_negroMaxDurationReached;
var _key_respfaseNegro_allKeys;
var fase_negroMaxDuration;
var fase_negroComponents;
function fase_negroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fase_negro' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fase_negroClock.reset();
    routineTimer.reset();
    fase_negroMaxDurationReached = false;
    // update component parameters for each repeat
    textfaseNegro.setText(word);
    key_respfaseNegro.keys = undefined;
    key_respfaseNegro.rt = undefined;
    _key_respfaseNegro_allKeys = [];
    psychoJS.experiment.addData('fase_negro.started', globalClock.getTime());
    fase_negroMaxDuration = null
    // keep track of which components have finished
    fase_negroComponents = [];
    fase_negroComponents.push(textfaseNegro);
    fase_negroComponents.push(key_respfaseNegro);
    
    for (const thisComponent of fase_negroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fase_negroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fase_negro' ---
    // get current time
    t = fase_negroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textfaseNegro* updates
    if (t >= 0.0 && textfaseNegro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textfaseNegro.tStart = t;  // (not accounting for frame time here)
      textfaseNegro.frameNStart = frameN;  // exact frame index
      
      textfaseNegro.setAutoDraw(true);
    }
    
    
    // if textfaseNegro is active this frame...
    if (textfaseNegro.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textfaseNegro.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      textfaseNegro.tStop = t;  // not accounting for scr refresh
      textfaseNegro.frameNStop = frameN;  // exact frame index
      // update status
      textfaseNegro.status = PsychoJS.Status.FINISHED;
      textfaseNegro.setAutoDraw(false);
    }
    
    
    // *key_respfaseNegro* updates
    if (t >= 0.0 && key_respfaseNegro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respfaseNegro.tStart = t;  // (not accounting for frame time here)
      key_respfaseNegro.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respfaseNegro.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respfaseNegro.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respfaseNegro.clearEvents(); });
    }
    
    // if key_respfaseNegro is active this frame...
    if (key_respfaseNegro.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respfaseNegro.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_respfaseNegro_allKeys = _key_respfaseNegro_allKeys.concat(theseKeys);
      if (_key_respfaseNegro_allKeys.length > 0) {
        key_respfaseNegro.keys = _key_respfaseNegro_allKeys[_key_respfaseNegro_allKeys.length - 1].name;  // just the last key pressed
        key_respfaseNegro.rt = _key_respfaseNegro_allKeys[_key_respfaseNegro_allKeys.length - 1].rt;
        key_respfaseNegro.duration = _key_respfaseNegro_allKeys[_key_respfaseNegro_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fase_negroComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fase_negroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fase_negro' ---
    for (const thisComponent of fase_negroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fase_negro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respfaseNegro.corr, level);
    }
    psychoJS.experiment.addData('key_respfaseNegro.keys', key_respfaseNegro.keys);
    if (typeof key_respfaseNegro.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respfaseNegro.rt', key_respfaseNegro.rt);
        psychoJS.experiment.addData('key_respfaseNegro.duration', key_respfaseNegro.duration);
        routineTimer.reset();
        }
    
    key_respfaseNegro.stop();
    // the Routine "fase_negro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial2MaxDurationReached;
var _key_respMensaje_allKeys;
var trial2MaxDuration;
var trial2Components;
function trial2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trial2Clock.reset();
    routineTimer.reset();
    trial2MaxDurationReached = false;
    // update component parameters for each repeat
    key_respMensaje.keys = undefined;
    key_respMensaje.rt = undefined;
    _key_respMensaje_allKeys = [];
    psychoJS.experiment.addData('trial2.started', globalClock.getTime());
    trial2MaxDuration = null
    // keep track of which components have finished
    trial2Components = [];
    trial2Components.push(text_2);
    trial2Components.push(key_respMensaje);
    
    for (const thisComponent of trial2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trial2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial2' ---
    // get current time
    t = trial2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // if text_2 is active this frame...
    if (text_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_2.tStop = t;  // not accounting for scr refresh
      text_2.frameNStop = frameN;  // exact frame index
      // update status
      text_2.status = PsychoJS.Status.FINISHED;
      text_2.setAutoDraw(false);
    }
    
    
    // *key_respMensaje* updates
    if (t >= 0.0 && key_respMensaje.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respMensaje.tStart = t;  // (not accounting for frame time here)
      key_respMensaje.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respMensaje.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respMensaje.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respMensaje.clearEvents(); });
    }
    
    // if key_respMensaje is active this frame...
    if (key_respMensaje.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respMensaje.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_respMensaje_allKeys = _key_respMensaje_allKeys.concat(theseKeys);
      if (_key_respMensaje_allKeys.length > 0) {
        key_respMensaje.keys = _key_respMensaje_allKeys[_key_respMensaje_allKeys.length - 1].name;  // just the last key pressed
        key_respMensaje.rt = _key_respMensaje_allKeys[_key_respMensaje_allKeys.length - 1].rt;
        key_respMensaje.duration = _key_respMensaje_allKeys[_key_respMensaje_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial2' ---
    for (const thisComponent of trial2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respMensaje.corr, level);
    }
    psychoJS.experiment.addData('key_respMensaje.keys', key_respMensaje.keys);
    if (typeof key_respMensaje.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respMensaje.rt', key_respMensaje.rt);
        psychoJS.experiment.addData('key_respMensaje.duration', key_respMensaje.duration);
        routineTimer.reset();
        }
    
    key_respMensaje.stop();
    // the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practicaMaxDurationReached;
var _key_respPractica_allKeys;
var practicaMaxDuration;
var practicaComponents;
function practicaRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practica' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practicaClock.reset();
    routineTimer.reset();
    practicaMaxDurationReached = false;
    // update component parameters for each repeat
    textPractica.setColor(new util.Color(color));
    textPractica.setText(word
    );
    key_respPractica.keys = undefined;
    key_respPractica.rt = undefined;
    _key_respPractica_allKeys = [];
    psychoJS.experiment.addData('practica.started', globalClock.getTime());
    practicaMaxDuration = null
    // keep track of which components have finished
    practicaComponents = [];
    practicaComponents.push(textPractica);
    practicaComponents.push(key_respPractica);
    
    for (const thisComponent of practicaComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practicaRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practica' ---
    // get current time
    t = practicaClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textPractica* updates
    if (t >= 0.0 && textPractica.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textPractica.tStart = t;  // (not accounting for frame time here)
      textPractica.frameNStart = frameN;  // exact frame index
      
      textPractica.setAutoDraw(true);
    }
    
    
    // if textPractica is active this frame...
    if (textPractica.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_respPractica* updates
    if (t >= 0.0 && key_respPractica.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respPractica.tStart = t;  // (not accounting for frame time here)
      key_respPractica.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respPractica.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respPractica.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respPractica.clearEvents(); });
    }
    
    // if key_respPractica is active this frame...
    if (key_respPractica.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respPractica.getKeys({
        keyList: typeof ['v','a','a','n','r'] === 'string' ? [['v','a','a','n','r']] : ['v','a','a','n','r'], 
        waitRelease: false
      });
      _key_respPractica_allKeys = _key_respPractica_allKeys.concat(theseKeys);
      if (_key_respPractica_allKeys.length > 0) {
        key_respPractica.keys = _key_respPractica_allKeys[_key_respPractica_allKeys.length - 1].name;  // just the last key pressed
        key_respPractica.rt = _key_respPractica_allKeys[_key_respPractica_allKeys.length - 1].rt;
        key_respPractica.duration = _key_respPractica_allKeys[_key_respPractica_allKeys.length - 1].duration;
        // was this correct?
        if (key_respPractica.keys == color) {
            key_respPractica.corr = 1;
        } else {
            key_respPractica.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practicaComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practicaRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practica' ---
    for (const thisComponent of practicaComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practica.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_respPractica.keys === undefined) {
      if (['None','none',undefined].includes(color)) {
         key_respPractica.corr = 1;  // correct non-response
      } else {
         key_respPractica.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respPractica.corr, level);
    }
    psychoJS.experiment.addData('key_respPractica.keys', key_respPractica.keys);
    psychoJS.experiment.addData('key_respPractica.corr', key_respPractica.corr);
    if (typeof key_respPractica.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respPractica.rt', key_respPractica.rt);
        psychoJS.experiment.addData('key_respPractica.duration', key_respPractica.duration);
        routineTimer.reset();
        }
    
    key_respPractica.stop();
    // the Routine "practica" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial3MaxDurationReached;
var _key_resp_allKeys;
var trial3MaxDuration;
var trial3Components;
function trial3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trial3Clock.reset();
    routineTimer.reset();
    trial3MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('trial3.started', globalClock.getTime());
    trial3MaxDuration = null
    // keep track of which components have finished
    trial3Components = [];
    trial3Components.push(text_3);
    trial3Components.push(key_resp);
    
    for (const thisComponent of trial3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trial3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial3' ---
    // get current time
    t = trial3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // if text_3 is active this frame...
    if (text_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_3.tStop = t;  // not accounting for scr refresh
      text_3.frameNStop = frameN;  // exact frame index
      // update status
      text_3.status = PsychoJS.Status.FINISHED;
      text_3.setAutoDraw(false);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    // if key_resp is active this frame...
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial3' ---
    for (const thisComponent of trial3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var experimentoMaxDurationReached;
var _key_respExperimento_allKeys;
var experimentoMaxDuration;
var experimentoComponents;
function experimentoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'experimento' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    experimentoClock.reset();
    routineTimer.reset();
    experimentoMaxDurationReached = false;
    // update component parameters for each repeat
    textExperimento.setColor(new util.Color(color));
    textExperimento.setText(word
    );
    key_respExperimento.keys = undefined;
    key_respExperimento.rt = undefined;
    _key_respExperimento_allKeys = [];
    psychoJS.experiment.addData('experimento.started', globalClock.getTime());
    experimentoMaxDuration = null
    // keep track of which components have finished
    experimentoComponents = [];
    experimentoComponents.push(textExperimento);
    experimentoComponents.push(key_respExperimento);
    
    for (const thisComponent of experimentoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function experimentoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'experimento' ---
    // get current time
    t = experimentoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textExperimento* updates
    if (t >= 0.0 && textExperimento.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textExperimento.tStart = t;  // (not accounting for frame time here)
      textExperimento.frameNStart = frameN;  // exact frame index
      
      textExperimento.setAutoDraw(true);
    }
    
    
    // if textExperimento is active this frame...
    if (textExperimento.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_respExperimento* updates
    if (t >= 0.0 && key_respExperimento.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respExperimento.tStart = t;  // (not accounting for frame time here)
      key_respExperimento.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respExperimento.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respExperimento.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respExperimento.clearEvents(); });
    }
    
    // if key_respExperimento is active this frame...
    if (key_respExperimento.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respExperimento.getKeys({
        keyList: typeof ['a','n','v','r','m','g','b','c'] === 'string' ? [['a','n','v','r','m','g','b','c']] : ['a','n','v','r','m','g','b','c'], 
        waitRelease: false
      });
      _key_respExperimento_allKeys = _key_respExperimento_allKeys.concat(theseKeys);
      if (_key_respExperimento_allKeys.length > 0) {
        key_respExperimento.keys = _key_respExperimento_allKeys[_key_respExperimento_allKeys.length - 1].name;  // just the last key pressed
        key_respExperimento.rt = _key_respExperimento_allKeys[_key_respExperimento_allKeys.length - 1].rt;
        key_respExperimento.duration = _key_respExperimento_allKeys[_key_respExperimento_allKeys.length - 1].duration;
        // was this correct?
        if (key_respExperimento.keys == color) {
            key_respExperimento.corr = 1;
        } else {
            key_respExperimento.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of experimentoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function experimentoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'experimento' ---
    for (const thisComponent of experimentoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('experimento.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_respExperimento.keys === undefined) {
      if (['None','none',undefined].includes(color)) {
         key_respExperimento.corr = 1;  // correct non-response
      } else {
         key_respExperimento.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respExperimento.corr, level);
    }
    psychoJS.experiment.addData('key_respExperimento.keys', key_respExperimento.keys);
    psychoJS.experiment.addData('key_respExperimento.corr', key_respExperimento.corr);
    if (typeof key_respExperimento.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respExperimento.rt', key_respExperimento.rt);
        psychoJS.experiment.addData('key_respExperimento.duration', key_respExperimento.duration);
        routineTimer.reset();
        }
    
    key_respExperimento.stop();
    // the Routine "experimento" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
