'''
------------------------------------------------------------------------------
Copyright 2016 Esri
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-----------------------------------------------------------------------------
Configuration.py
Description: Common objects/methods used by test scripts
Requirements: ArcGIS Desktop Standard
 ----------------------------------------------------------------------------
'''

import os

DEBUG = False # this guy is a flag for extra messaging while debugging tests

#NOTE: Logger and Platform are initialized in TestRunner's main()
Logger = None
Platform = None

''' Testing paths '''
currentPath = os.path.dirname(__file__) # should go to .\military-tools-geoprocessing-toolbox\utils\test

''' Log Path '''
logPath = os.path.normpath(os.path.join(currentPath, r"log")) # should go to .\test\log

''' Toolboxes paths '''
ViewshedPath = os.path.normpath(os.path.join(os.path.dirname(currentPath), r"../Viewshed/"))
ViewshedToolboxPath = os.path.normpath(os.path.join(ViewshedPath, "Viewshed.tbx"))

''' Visibility Path '''
visibilityPath = os.path.normpath(currentPath)