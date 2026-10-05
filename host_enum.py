import subprocess

def host_enum():
    commands = [["whoami"],["ip","addr","show"],["ps", "aux"],["ss", "-lntup"],["nonexistent_security_command"],["ip","neigh"]]
    output = []
    for comm in commands:
        try:
            result=subprocess.run(comm,text=True,capture_output=True)
            if result.returncode != 0 :
                output.append(dict(command = comm , out = " " , err = result.stderr , state = 1))
            else:
                output.append(dict(command = comm , out = result.stdout , err = result.stderr , state = result.returncode))
        except FileNotFoundError :    
            output.append(dict(command = comm , out = " " , err = "command not found" , state = 1))
        
    return(output)    
def style(out):
    for each in out:
        if each["state"] == 0:
            print(f"==========================={each['command']}=======================")
            print (f"command : {each['command']}")
            print (f"output : {each['out']}")
            print (f"error : {each['err']}")
            print (f"state : SUCCESS")    
        else :
            print(f"==========================={each['command']}=======================")
            print (f"command : {each['command']}")
            print (f"output : {each['out']}")
            print (f"error : {each['err']}")
            print (f"state : FAILED")

vars = host_enum()
style(vars)

