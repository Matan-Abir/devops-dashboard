import sysinfo

print("===== Devops Dashboard =====")

menu_message = """
– [1] System Info
– [2] Log Checker
– [3] Task List
– [0] Exit
 Input your choice between 0 and 3 now: 
"""

menu_choice = -1
while(menu_choice != 0):
	try:
		print(menu_message)
		menu_choice = int(input())
		if menu_choice >= 0 and menu_choice <=3:
			# Valid input
			if menu_choice == 1:
				sysinfo.show_sysinfo()
			else:
				print("Coming soon...!")
		else:
			# Invalud input
			input("Invalid choice! Press enter to try again..")
	except:
		input("Input has to be a number between 0 and 3! Press enter to try again..")

input("Now exiting the devops dashboard...")
