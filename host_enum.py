import subprocess

def host_enum():
    commands = [["whoami"],["ip","addr","show"],["ps", "aux"],["ss", "-lntup"]]
    output = []
    for comm in commands:
        result=subprocess.run(comm,text=True,capture_output=True)
        output.append(dict(command = comm , out = result.stdout , err = result.stderr , state = result.returncode))
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

