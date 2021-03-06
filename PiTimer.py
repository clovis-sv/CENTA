#!/usr/bin/python




import time
import datetime
import curses
import SystemTime
import Schedule
import ScheduleItem
import Relays
import UserInterface


#/**************************/
#/* Application constants. */
#/**************************/

GPIO_PINS = [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0 ]
MAX_RELAYS = 11
KEY_ESC = 27
MAIN_LOOP_PERIOD = 250
CHECK_SCHEDULE_COUNT = 4


#/**************************************************************************/
#/* Main application procedure.                                            */
#/**************************************************************************/
# Instance of the system time class to handle system time and clock module.
ThisSystemTime = SystemTime.SystemTime()
# Instance of schedule class to store and process timer schedules.
ThisSchedule = Schedule.Schedule()
# Instnace of relays class to store current relay states.
ThisRelays = Relays.Relays()

#  /*********************************************************/
# /* Configure the console so key presses can be captured. */
#/*********************************************************/
curses.initscr()
curses.noecho()
window = curses.newwin(80, 25)
window.nodelay(1)
window.timeout(0)

# Instance of user interface class to manage user interactions.
ThisUserInterface = UserInterface.UserInterface(window, ThisSchedule, ThisRelays)
time.sleep(1)

#   /*******************************************************************/
#  /* Get the time from the timer module, and set the system time to  */
# /* ensure the system time is correct at the start.                 */
#/*******************************************************************/
# BOOKMARK: THIS IS A PLACEHOLDER FOR WHEN THE CLOCK MODLUE IS IMPLEMENTED.
ThisSystemTime.SetSystemTime("2015-06-18 19:40:00")

#    /*********************************************************/
#   /* Create an initial state for each realy in the system. */
#  /* Adding an extra item, as item 0 will be ignored so    */
# /* relay numbers start at a more user freindly 1.        */
#/*********************************************************/
for Count in range(MAX_RELAYS):
   if len(GPIO_PINS) > Count and GPIO_PINS[Count]:
      ThisRelays.AddRelay(Count + 1, Relays.RELAY_OFF, GPIO_PINS[Count])

#  /*********************************************************/
# /* Load schedule items from previous run of application. */
#/*********************************************************/
ThisSchedule.Load()

#   /********************************************/
#  /* Main application loop, this continues    */
# /* forever or until the ESC key is pressed. */
#/********************************************/
CheckScheduleCount = CHECK_SCHEDULE_COUNT
ExitFlag = False
while ExitFlag == False:

#  /*************************/
# /* Get a user key press. */
#/*************************/
   ThisKey = window.getch()

#  /******************************************************/
# /* Pass user key presses to the user interface class. */
#/******************************************************/
   if ThisKey != -1:
      ThisKey = ThisUserInterface.KeyPress(ThisKey)

#  /**********************************************************/
# /* If the ESC key has been pressed, exit the application. */
#/**********************************************************/
   if ThisKey == KEY_ESC:
      ExitFlag = True

#  /**********************************************/
# /* Process main application loop every 250ms. */
#/**********************************************/
   curses.napms(MAIN_LOOP_PERIOD)

#  /********************************************/
# /* Process the schedule loop once a second. */
#/********************************************/
   CheckScheduleCount -= 1
   if CheckScheduleCount <= 0:
      CheckScheduleCount = CHECK_SCHEDULE_COUNT

#  /********************************************/
# /* Process all events which have triggered. */
#/********************************************/
      ThisItemID = True
      while ThisItemID:
#     /**************************************************************/
#    /* Check for a scheduled item which has moved into the past.  */
#   /* If an item is found process it and then remove it from the */
#  /* schedule. The item will automatically be rescheduled if    */
# /* required.                                                  */
#/**************************************************************/
         ThisItemID = ThisSchedule.ScheduleTrigger()
         if ThisItemID:
            ThisScheduleItem = ThisSchedule.FindItem(ThisItemID)
            ThisRelayAction = ThisScheduleItem.GetRelayState()
            ThisRelayNumber = ThisScheduleItem.GetRelayNumber()
            if ThisRelayAction == ScheduleItem.RELAY_OFF:
               ThisRelays.SetRelayState(ThisRelayNumber, Relays.RELAY_OFF)
            elif ThisRelayAction == ScheduleItem.RELAY_ON:
               ThisRelays.SetRelayState(ThisRelayNumber, Relays.RELAY_ON)
            else:
               ThisRelays.ToggleRelayState(ThisRelayNumber)
            ThisSchedule.SetNextScheduleDate(ThisItemID)

#  /****************************************************************/
# /* Certain user interface displays need to update every second. */
#/****************************************************************/
      ThisUserInterface.DisplayRefresh()

#  /*****************************************/
# /* Save application state before ending. */
#/*****************************************/
ThisSchedule.Save(True)

#  /*********************/
# /* Exit application. */
#/*********************/
curses.endwin()

#  /*********************************************/
# /* Close Raspberry Pi GPIO before finishing. */
#/*********************************************/
ThisRelays.CloseGPIO()

