# PiTimer - Python Hardware Programming Education Project For Raspberry Pi
# Copyright (C) 2015 Jason Birch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#/****************************************************************************/
#/* PiTimer - Step 8 - Controlling physical relays.                          */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2015-07-04 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Class to handle the current relay states.                                */
#/****************************************************************************/


import operator
import datetime
import RPi.GPIO
import SystemTime


# Constants to define relay state.
RELAY_OFF = 1
RELAY_ON = 0


class Relays:

   def __init__(self):
# Instance storage for relay states.
      self.RelayState = []

# Configure Raspberry Pi GPIO interfaces.
      RPi.GPIO.setmode(RPi.GPIO.BCM)
      RPi.GPIO.setwarnings(False)


#/*************************************************/
#/* Close Raspberry Pi GPIO use before finishing. */
#/*************************************************/
   def CloseGPIO(self):
      RPi.GPIO.cleanup()


#/***********************************************************/
#/* Add a relay to the relays supported by the application. */
#/***********************************************************/
   def AddRelay(self, RelayNumber, RelayState, RelayPin):
      self.RelayState.append([RelayNumber, RelayState, RelayPin])
      if RelayPin:
         RPi.GPIO.setup(RelayPin, RPi.GPIO.OUT, initial=RelayState)


#/*******************************************/
#/* Display a table of the current relay    */
#/* states and the date/time at that point. */
#/*******************************************/
   def DisplayRelayStates(self):
      ThisSystemTime = SystemTime.SystemTime()
      print("{:>20}".format(ThisSystemTime.SystemTimeString()) + "\r")
      Line1 = ""
      Line2 = ""
      Line3 = ""
      for ThisRelayState in self.RelayState:
         if ThisRelayState[0]:
            RelayDiv = operator.div(ThisRelayState[0], 10)
            RelayMod = operator.mod(ThisRelayState[0], 10)
            if RelayDiv:
               Line1 += str(RelayDiv)
            else:
               Line1 += " "
            Line2 += str(RelayMod)
            Line3 += str(ThisRelayState[1])
      print(Line1 + "\r")
      print(Line2 + "\r")
      print(Line3 + "\r")


#/************************************************/
#/* Get the current state of the specific relay. */
#/************************************************/
   def GetRelayState(self, RelayNumber):
      Result = False
      if RelayNumber - 1 < len(self.RelayState):
         Result = self.RelayState[RelayNumber - 1][1]
      return Result


#/************************************************/
#/* Set the current state of the specific relay. */
#/************************************************/
   def SetRelayState(self, RelayNumber, NewRelayState):
      if RelayNumber - 1 < len(self.RelayState):
         self.RelayState[RelayNumber - 1][1] = NewRelayState
         RPi.GPIO.output(self.RelayState[RelayNumber - 1][2], self.RelayState[RelayNumber - 1][1])


#/***************************************************/
#/* Toggle the current state of the specific relay. */
#/***************************************************/
   def ToggleRelayState(self, RelayNumber):
      Result = False
      if RelayNumber - 1 < len(self.RelayState):
         if self.RelayState[RelayNumber - 1][1] == RELAY_OFF:
            self.RelayState[RelayNumber - 1][1] = RELAY_ON
         else:
            self.RelayState[RelayNumber - 1][1] = RELAY_OFF
         RPi.GPIO.output(self.RelayState[RelayNumber - 1][2], self.RelayState[RelayNumber - 1][1])
         Result = self.RelayState[RelayNumber - 1][1]
      return Result

