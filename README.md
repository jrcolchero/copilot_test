# copilot_test

Initially, Copilot generated the code using the "net stats srv" command. However, this code wouldn't run on the device because the SERVER service wasn't running. The error the script was throwing was shared with Copilot, and Copilot suggested using the "wmic os get lastbootuptime" command.

Once the code was functional, I asked Copilot to optimize the code to make it more secure and reliable. For this request, Copilot generated functions for each OS with exception handling and changed the os.popen instruction to subprocess.run.
