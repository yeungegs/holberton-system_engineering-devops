_**Full disclosure: the author of this report [@yeungegs](https://github.com/yeungegs) is [@egsy](https://twitter.com/egsy).**_

# Social Media Campaign Incident Report

##   Issue Summary
At 12:50 PM PDT on August 8, 2017, Twitter user Elaine Yeung ([@egsy](https://twitter.com/egsy)) launched a tweet campaign targeting [Slack](https://slack.com/). The goal of the campaign was to apply social pressure on Slack so that they would make an exception to their [Slack for Education](https://get.slack.help/hc/en-us/articles/206646877-Slack-for-Education) screening process and recognize [Holberton School](https://www.holbertonschool.com/) as an educational organization. The parent tweet was retweeted 6 times and received 14 likes. Within three hours, Slack responded and held firm to their existing policy. The goal of receiving an education discount was not achieved, rendering the tweet campaign a failure.


## Timeline
### Definitions

According to [Twitter's documentation](https://business.twitter.com/en/help/campaign-measurement-and-analytics/tweet-activity-dashboard.html), every tweet generates a number of analytic points. The three points of analysis referenced in this report are:

- Impressions: Times people were served a Tweet in timeline or search results
- Engagements: Total number of times someone interacted with a Tweet. Clicks anywhere on the Tweet, including Retweets, replies, follows, likes, links, cards, hashtags, embedded media, username, profile photo, or Tweet expansion
- Engagement rate: The number of engagements divided by the number of impressions

### Issue detection

With each new batch of students enrolled, the number of users on the Holberton School Slack team is ever increasing. Holberton School is currently using a free account. Free accounts are limited to a 10,000 message limit. With more members sending more messages, messages are quickly lost. One of Slack's hallmark functions is its ability to search message archives. At the school's current rate of slack usage, 10,000 messages are sent within a three week period, rendering all messages older than that unsearchable. 

Before joining Holberton School, Elaine led her school's adoption of Slack and is a self-proclaimed fan of the service. 

### how was the issue detected (monitoring alert, an engineer noticed something, a customer complained...)
### actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
### misleading investigation/debugging paths that were taken
### which team/individuals was the incident escalated to
### how the incident was resolved
The root issue is still unresolved and Holberton School's slack team is still limited to 10,000 message limit.


Tweets (all times listed in PDT) | Impressions | Engagements | Engagement rate
:--- | :--- | :--- | :---
the 10k msg limit kills my classmate&#39;s investment in <a href="https://twitter.com/SlackHQ">@SlackHQ</a>... how I wish they&#39;d recognize <a href="https://twitter.com/holbertonschool">@holbertonschool</a> for the ed discount💸💰 …</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895009313638436864">August 8, 2017</a> 12:50 PM | 1,045|57|5.4%
…since <a href="https://twitter.com/holbertonschool">@holbertonschool</a> is a non-traditional school and <a href="https://twitter.com/SlackHQ">@slackhq</a> is a non-traditional messaging platform, we should able to negotiate.</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895009426460917761">August 8, 2017</a> 12:50 PM | 782|13|1.7%
pidea💡set a goal number <a href="https://twitter.com/github">@github</a> commits that all <a href="https://twitter.com/holbertonschool">@holbertonschool</a> students here reach.</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895009609181667328">August 8, 2017</a> 12:51 PM | 842|12|1.4% 
if met, then we qualify for the slack for education discount. 6 months ago I was a novice coder and have made 1,982 commits since.</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895009675569094657">August 8, 2017</a> 12:51 PM | 701|16|2.3%
by that metric, if all students <a href="https://twitter.com/holbertonschool">@holbertonschool</a> reach 100k commits by end of month, then <a href="https://twitter.com/SlackHQ">@slackhq</a> approves us for the ed discount? 🙏🤓</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895010116377862144">August 8, 2017</a> 12:53 PM  |259| 5 | 1.9%
second idea💡name a number of thread retweets we need in order to receive the discount.</p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895010316219670528">August 8, 2017</a> 12:54 PM  | 256| 6| 2.3% 
I was really expecting a more empathetic response from <a href="https://twitter.com/SlackHQ">@SlackHQ</a> 😔😔😔 <a href="https://t.co/AtBdHP1RGf">https://t.co/AtBdHP1RGf</a></p>&mdash; Elaine Y (@egsy) <a href="https://twitter.com/egsy/status/895031815924203520">August 8, 2017</a> 2:19 PM | 341 |15 | 4.4%

##  Root cause and resolution

- explain in detail what was causing the issue
- explain in detail how the issue was fixed

##   Corrective and preventative measures

- what are the things that can be improved/fixed
- a list of tasks to address the issue (example: patch Nginx server, add monitoring on server memory...)

