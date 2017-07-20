# Logs Analysis
A reporting tool that prints out reports (in plain text) based on the data in the news database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

News is a mock database for a news website. It contains tables with information about newspaper articles, authors as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.
Version of Python used: 3.6.1

### Contents
Project files : <br/>
newsreport.py - Python program file that connects to the news database and executes the sql to print to results.<br/>
newsdata.txt - Copy of the result that the program printed out.<br/>
newsdata.sql - File used to create tables and populate them with data.


### Installation
1. Install [Python](https://www.python.org )<br/>

2. **Create the news database** <Br/>
This project makes use of Linux-based virtual machine (VM). This will give you the PostgreSQL database and support software needed for this project.  Install the virtual machine.  We're using tools called Vagrant and VirtualBox to install and manage the VM

**Install VirtualBox** <br/>
VirtualBox is the software that actually runs the virtual machine. You can download it from [virtualbox.org](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system.

**Install Vagrant**<br/>
Vagrant is the software that configures the VM and lets share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.<br/>
From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while. Then log into it with `vagrant ssh`.

3. Download the news zip file and unzip the file. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
<br/>

4. To load the data, use the command `psql -d news -f newsdata.sql`. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Operating Instructions
To Start the news logs analysis report application:<br/>
1. Open the command line tool<br/>
2. Inside the vagrant subdirectory(cd /vagrant), navigate to the directory containing the newsreport.py folder. Run the command `python3 newsreport.py`<br/>
3. The three project questions are printed along with the answer


### Acknowledgments
The news logs data is provided by Udacity.
