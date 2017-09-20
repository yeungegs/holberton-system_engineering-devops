[![postmortem](http://i.imgur.com/pQ9YzVY.gif)](https://twitter.com/devopsreact/status/834887829486399488)

Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:

##   Issue Summary (that is often what executives will read) must contain:

*   duration of the outage with start and end times (including timezone)
*   what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
*   what was the root cause

##   Timeline (format bullet point, format: `time` - `keep it short, 1 or 2 sentences`) must contain:

*   when was the issue detected
*   how was the issue detected (monitoring alert, an engineer noticed something, a customer complained...)
*   actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
*   misleading investigation/debugging paths that were taken
*   which team/individuals was the incident escalated to
*   how the incident was resolved

##  Root cause and resolution must contain:

*   explain in detail what was causing the issue
*   explain in detail how the issue was fixed

##   Corrective and preventative measures must contain:

*   what are the things that can be improved/fixed
*   a list of tasks to address the issue (example: patch Nginx server, add monitoring on server memory...)

##   Be brief and straight to the point, between 400 to 600 words
													
While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.
