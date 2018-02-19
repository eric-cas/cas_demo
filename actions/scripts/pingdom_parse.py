import sys
import json

from st2actions.runners.pythonrunner import Action

class PingdomParse(Action):
  def run(self, json_body):
    webhook_info = dict()
    webhook_info["current_state"] = json_body["current_state"]
    webhook_info["previous_state"] = json_body["previous_state"]
    if (webhook_info["current_state"] == "DOWN") and (webhook_info["previous_state"] == "UP"):
      webhook_info["site_failed"] = True
    else:
      webhook_info["site_failed"] = False
    webhook_info["url"] = json_body["check_params"]["full_url"]
    webhook_info["host"] = json_body["check_params"]["full_url"].split("/")[2]
    return (True,webhook_info)

