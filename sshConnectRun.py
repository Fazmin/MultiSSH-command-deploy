# Submit commands and capture output on a multi ssh connections using just python.
# Version 1.1 - Tested - Python 3.8 - Fazmin Nizam
# make sure you have paramiko installed - pip intstall paramiko

import paramiko

remote_ip_list = ('xxx.xxx.xxx.xxx','xxx.xxx.xxx.xxx','xxx.xxx.xxx.xxx')

def connect_and_run_ssh(remoteip):
    # Connect
    client = paramiko.SSHClient()    
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(remoteip, username='<user>', password='*******',look_for_keys=False, allow_agent=False)

    # Run a command (execute command to get temperature readings)
    stdin, stdout, stderr = client.exec_command('tempreading c')

    # Print output based on your requirements
    # print(type(stdin))  # <class 'paramiko.channel.ChannelStdinFile'>
    # print(type(stdout))  # <class 'paramiko.channel.ChannelFile'>
    # print(type(stderr))  # <class 'paramiko.channel.ChannelStderrFile'>

    #I used decode UTF-8. you can use decoding options. 
    outinfo = stdout.read().decode("utf8")
    outinfo = stdout.read().decode("utf8")
    outinfo = stdout.read().decode("utf8")
    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    # Close the client itself
    client.close()

    return outinfo

for remoteip in remote_ip_list:
    print (f'\nConnecting to: {remoteip}\n')
    dataout = connect_and_run_ssh(remoteip)
    print (dataout)