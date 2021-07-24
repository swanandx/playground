import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Rust playground')
parser.add_argument('-f', dest='filename', type=str, help='Give rust code file', required=True)
parser.add_argument('-c', dest='channel', type=str ,default="stable" ,help='Channel', choices=["stable", "beta", "nightly"])
parser.add_argument('-m', dest='mode', type=str , default="debug" ,help='Mode', choices=["debug", "release"])
parser.add_argument('-e', dest='edition', type=int ,default=2018 ,help='Editon', choices=[2018,2015,2021])

args = parser.parse_args()

filename = args.filename
channel = args.channel
mode = args.mode
edition = str(args.edition)


with open(filename, "r") as rc:
	code = rc.read()

headers = {"Content-Type": "application/json"}

data = '{"channel":"'+ channel +'","mode":"'+mode+'","edition":"'+edition+'","crateType":"bin","tests":false,"code":' + json.dumps(code) +',"backtrace":false}'

res = requests.post("https://play.rust-lang.org/execute", headers=headers, data=data)

parsed_res = json.loads(res.text)

if parsed_res["success"]:
	print(parsed_res["stdout"], end='')
else:
	print(parsed_res["stderr"],end='')
