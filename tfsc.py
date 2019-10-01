import requests
import argparse
import sys
import re
from termcolor import colored

def cprint(text, color): # colored print
	sys.stdout.write(colored(text + "\n", color, attrs=["bold"]))

def vcprint(text, color): # verbose-only colored print
	global verbose

	if verbose:
		cprint(text, color)

def httpize(url):
	if not url.startswith("http"):
		cprint("Missing protocol, using http . . .", "yellow")
		url = "http://" + url
	return url

def attack(url):
	global found
	vcprint("Starting request to %s" % url, "yellow")

	try:
		response = requests.get(url)
		if not str(response.status_code).startswith("2"):
			vcprint("[%s] Request code: %d" % (url, response.status_code), "red")
		else:
			found += 1
			cprint("[%s] Request code: %d" % (url, response.status_code), "green")
	except requests.exceptions.Timeout:
		cprint("Request to url %s failed: Timed out" % url)

	return response

cprint("""
                  ________________________________________
         (__)    /                                        \\
         (oo)   (   Temporary File Source Code Disclosure  )
  /-------\\/ --' \\________________________________________/ 
 / |     ||
*  ||----||             
""", "green")

parser = argparse.ArgumentParser(description="TFSC: A tool to search for php backup files (and display their source code)")
parser.add_argument("-u", "--url", help="Base url")
parser.add_argument("-f", "--file", help="File (or comma separated list of files) to search")
parser.add_argument("-v", "--verbose", help="Show debug information")
args = parser.parse_args()

# Both arguments are required
if args.url is None or args.file is None:
	cprint("Missing arguments.\nUsage example:\n" + sys.argv[0] + " -u http://10.10.10.14/ -f index.php\n" + sys.argv[0] + " -u http://10.10.10.14/ -f index.php,stats.php", "red")
	sys.exit()

# configuration
verbose = args.verbose
url = httpize(args.url)
file_list = args.file.split(",") # possible_extensions
cleaned_file_list = [s.rstrip(re.sub(r'\.\w+', "", s)) for s in file_list] # possible_extless || remove file extensions

possible_extensions = ["%s~", "#%s#", "~%s", "%s.bak", "%s.tmp", "%s.old"]
possible_extless    = ["%s.bak", "%s.tmp", "%s.old"]

# Add / at the end of the url
url = url + "/" if not url.endswith("/") else url
attempts = found = 0

def show_results():
	global attempts, found
	color = "green" if found > 0 else "red"
	cprint("%d URLs attempted, %d files found." % (attempts, found), color)

def start():
	global attempts
	cprint("Loading payloads . . .", "green")

	for file in cleaned_file_list:
		for extless in possible_extless:
			attempts +=1
			target = url + extless % file
			attack(target)
	for file in file_list:
		for ext in possible_extensions:
			attempts +=1
			target = url + ext % file
			attack(target)


def main():
	start()
	show_results()

if __name__ == '__main__':
	try:
		main()
	except:
		print "\nBye!!"
