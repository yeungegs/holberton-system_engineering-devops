##   Issue Summary (that is often what executives will read) must contain:

- duration of the outage with start and end times (including timezone)
- what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
- what was the root cause

At 12:50 PM on August 8, 2017, Twitter user [@egsy](https://twitter.com/egsy) launched a tweet campaign targeting [Slack](https://slack.com/).


##   Timeline (format bullet point, format: `time` - `keep it short, 1 or 2 sentences`) must contain:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">the 10k msg limit kills my classmate&#39;s investment in <a href="https://twitter.com/SlackHQ">@SlackHQ</a>... how I wish they&#39;d recognize <a href="https://twitter.com/holbertonschool">@holbertonschool</a> for the ed discount💸💰 …</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895009313638436864">August 8, 2017</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">…since <a href="https://twitter.com/holbertonschool">@holbertonschool</a> is a non-traditional school and <a href="https://twitter.com/SlackHQ">@slackhq</a> is a non-traditional messaging platform, we should able to negotiate.</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895009426460917761">August 8, 2017</a></blockquote>

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">…since <a href="https://twitter.com/holbertonschool">@holbertonschool</a> is a non-traditional school and <a href="https://twitter.com/SlackHQ">@slackhq</a> is a non-traditional messaging platform, we should able to negotiate.</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895009426460917761">August 8, 2017</a></blockquote>


- when was the issue detected
- how was the issue detected (monitoring alert, an engineer noticed something, a customer complained...)
- actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
- misleading investigation/debugging paths that were taken
- which team/individuals was the incident escalated to
- how the incident was resolved

##  Root cause and resolution must contain:

- explain in detail what was causing the issue
- explain in detail how the issue was fixed

##   Corrective and preventative measures must contain:

- what are the things that can be improved/fixed
- a list of tasks to address the issue (example: patch Nginx server, add monitoring on server memory...)

##   Be brief and straight to the point, between 400 to 600 words
													
While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.
