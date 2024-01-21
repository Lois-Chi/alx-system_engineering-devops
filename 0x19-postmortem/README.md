			#POSTMORTEM

##Issue Summary: 

###Duration: 1 hour and 15 minutes (from 2:00PM to 3:15PM GMT+1)

###Impact: The service was down for about 1 hour and 15 minutes, causing users to be unable to access it. Approximately 60% of the users were affected.

##Root Cause: A typo in the shell script caused the service to fail.

##Timeline:
- 2:00 PM: The service goes down.
- 2:05 PM: An engineer notices the outage and alerts the team.
- 2:10 PM: The engineering team investigates the issue and determines the cause.
- 2:20 PM: The engineering team tries to fix the typo but is unsuccessful.
- 2:30 PM: The team determines that the typo is in a critical part of the shell script.
- 3:00 PM: The team fixes the typo and deploys the fix to the production environment.
- 3:15 PM: The service is back up and running

##Root Cause And Resolution: The root cause of the issue was a typo in the shell script. The typo caused the service to fail because the script was unable to execute the critical part of the code. The issue was resolved by fixing the typo in the shell script.

##Corrective And Preventive Measures:
- The code will be reviewed to ensure that there are no typos.
- A monitoring system will be implemented to track the status of the service and alert the engineering team if there is an issue
- A process will be put in place to ensure that the code is tested thoroughly before it is deployed to the production environment.

