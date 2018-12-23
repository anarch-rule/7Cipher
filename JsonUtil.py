import sys
import os
import json


def GetJsonData(path):
	data = None
	with open(path) as json_file:
		data = json.load(json_file)

	json_file.closed

	return data

def WriteJsonData(data, path):
	with open(path, 'w') as json_file:
		json.dump(data, json_file)

	json_file.closed

def CreateJsonFile(path, data):
	json_file = open(path,"w+")
	json.dump(data, json_file)
	json_file.closed
