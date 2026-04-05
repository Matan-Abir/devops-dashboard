def check_log():
  filename = input("Please enter a log filename: ")
  try:
    with open("file.txt", "r", encoding="utf-8") as log:
      loglines = log.readlines()
      for logline in loglines:
        if "error" in logline.lower():
          print(logline)
  except:
    input("No log file with that filename! Press enter to exit..")
