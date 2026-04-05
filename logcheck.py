def check_log():
	filename = input("Please enter a log filename: ")
	try:
		with open(filename, "r", encoding="utf-8") as log:
			loglines = log.readlines()
			error_logs = []
			for logline in loglines:
				if "error" in logline.lower():
					logline.replace("\n","")
					error_logs.append(logline)
			if len(error_logs) > 0:
				print("\nThe following error lines have been found:\n")
				print("\n".join(error_logs))
			else:
				print("No error lines found.")
	except:
		input("No log file with that filename! Press enter to exit..")
