import time
import os

command = input("Enter command:")
if command == ("/boot"):
    print("Welcome to Glass OS")
    while True:
        command = input("Enter command:")
        if command == ("/dir"):
            os.chdir("C:\\Users\\kachu178\\Desktop\\GlassOS")
            files = os.listdir("C:\\Users\\kachu178\\Desktop\\GlassOS")
            for file in files:
                print(file)
        if command == '/exit':
            print("Exiting GlassOS...")
            time.sleep(2)
            break
        if command == ("/info32"):
            import os
            output = os.popen("systeminfo").read()
           
            lines = output.split('\n')
            for line in lines:
                if "Processor" in line:
                    print("CPU:", line.strip())
                elif "Total Physical Memory" in line:
                    print("RAM:", line.strip())
        if command == ("/commands"):
            print("""Commands List
            /boot : Start GlassOS
            /exit : Exit GlassOS
            /info32 : Show System Info
            /credits : GlassOS Credits""")
        if command == ("/credits"):
           print("""Credits :
           MarioCarGuy - Lead Developer
           kachu178 - Logo, Developer""")