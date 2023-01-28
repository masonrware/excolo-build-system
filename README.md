```                                             
___  ________ _   _ _____ _____ ___  ________ 
|  \/  |  _  | \ | |  _  /  __ \|  \/  |  _  \
| .  . | | | |  \| | | | | /  \/| .  . | | | |
| |\/| | | | | . ` | | | | |    | |\/| | | | |
| |  | \ \_/ / |\  \ \_/ / \__/\| |  | | |/ / 
\_|  |_/\___/\_| \_/\___/ \____/\_|  |_/___/  
                                              
```                                                              
# <span style="color:maroon">MONOCMD</span>


##### Written By: Mason R. Ware (https://github.com/masonrware)

###### Last Updated: 28/01/2023 (DD/MM/YYYY)

* * *

# Table of Contents
1. [Build & Run](#Build&Run)
2. [Dependencies](#Dependencies)
3. [Description](#Description)

* * *

<a name="Build&Run"></a>

Build & Run
-----------

#### *Build Instructions*


#### *Run Instructions*

* * *

<a name="Dependencies"></a>

Dependencies
-----------

1. 


All dependencies can be found in the `./monocmd/requirements.txt` file. Moreover, they can be automatically installed using the shell command: `pip install -r ./monocmd/requirements.txt` and the most up to date versions of the dependencies can be installed using the shell command: `pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U` .

* * *

<a name="Description"></a>

Description
-----------

This is a program intended to be used as a last step for a build system. Once a program is ready to run in its destination enviornment, this service is intended to abstract all user-defined functionality of the program behind plain english one word cmd, cmd-flag sequences. Think git, git pull, git push.

The way the user is able to outline their projects's functionality is by providing a yaml template config file to this service via the cmd line from the source directory of their project. Then, this service will edit their .bashrc as well as their main source files to provide the intended callability of their program locally.

#### *File Structure*

* * * 

<a name="ToDo"></a>

To Do
-----------

1. *expand language support*
   1. don't need language-specific interpreter script because user will provide runtime (post-compilation) commands in the yaml template. However, will need some logic to compile code, if necessary.
   2. would need to have some form of paramterizable service to edit the files and add CLI arguments to them...
      1. **OR**, just write a different argparser for every language in that language so that it can be used to edit the file
         1. Then, based on provided language, logic can language-wise edit the specified source file(s) to include the language-specific import code
         2. This import code will hopefully be small in practice because most of the implementation will be packaged up into the argparser
            1. all argparesers will ship with the service so that it is available natively to the user on start-up.
               1. Question is: how do I import it in any/every user's source file from their `/usr/local` or `/usr/local/bin`?
2. Make it so that the user can add this service as a single command at the end of their own build system 
   1. Doing this to allow the user to install their program on a system as well as monocmd it!
* * * 

_© 2023 MASON WARE_