###
# host:
# 
# This is the name of the host you wish to connect to execute the print job
### 
host = ''

###
# user:
# 
# This is the user name you wish to assume whie logging in.
###
user = ''

###
# temp_storage:
# 
# Printing will involve first scp-ing the files from the client machine to the
# host machine and then invoking lpr on those files. This string determines the
# directory to which those files will be scp-ed to.
###
temp_storage = '~/print2remote_files'
