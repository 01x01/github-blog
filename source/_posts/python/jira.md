---
title: jira
date: 2019-06-21 15:01:01
tags: 
category: python
---
python 第三方框架实现与 jira 的集成
<!-- more -->
# 安装
```py
pip install jira
```
# 认证登陆
```py
from jira import JIRA
jira = JIRA("jira_url",basic_auth=("jira_user","jira_password"))
```
# 建 issue
```py
from datetime import datetime,timedelta
import os
 
def create_issues(project,assignee,summary,description,issuetype,**kw):
        issue_dict = {
            "project":{"key":project},
            "assignee":{"name":assignee},
            "summary":summary,
            "description":description,
            "issuetype":{"name":issuetype},
            "customfield_10001": {
                "value": "3 - Medium"
            },
            "customfield_10024": datetime.strftime(datetime.now() + timedelta(days=30),"%Y-%m-%d")
        }
        if kw:
            issue_dict.update(kw)
        
        new_issue = jira.create_issue(fields=issue_dict) # jira is the result of init 
        print(new_issue) # print issue number but it is issue object
```
# link
```py
def link_issue(self,inwardIssue):
        res = self.jira.create_issue_link("Related",inwardIssue,self.new_issue)
        print(res) # <Response [201]>
```
# close
```py
def close_issue(self):
        res = self.jira.transition_issue(self.new_issue,"2891",fields={"assignee":{"name":"+close_folder"},"resolution":{"name":"Completed"}},comment="close the issue")
        print(res)
```
# spring
```py
def add_to_current_spring(self):
        res = self.jira.sprints(437)
        #print(dir(res[0]))
        #print(res[0].state)
        for sprint in res:
            if sprint.state == "ACTIVE":
                print(isinstance(sprint.id,int))
                print(self.new_issue.key)
                res = self.jira.add_issues_to_sprint(sprint_id=sprint.id,issue_keys=[self.new_issue.key])
                print(res)
```
# attach
```py
 def attach_file(self,file):
        with open(file, 'rb') as f:
            self.jira.add_attachment(issue=self.new_issue, attachment=f,filename="test")
```
