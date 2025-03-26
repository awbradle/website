Title: Easy WiFi Connection Tool
Date: 2025-03-21 21:30
Modified: 2025-03-21 21:30
Category: Pages
Slug: projects/gsoc2025
Author: Andie Bradley
Summary: Google Summer of Code Proposal for FreeBSD WiFi project



## General Info ##
Name: Andie Bradley <br/>
Email: abradl26@emich.edu <br/>
Phone: (US) +1 ### ### #### <br/>
IRC: pokeysquirrel at libera.chat <br/>
Discord: pokey at FreeBSD Discord Server <br/>
Location: Madison, WI, USA <br/>
Time Zone: Central Daylight Time (UTC-5) <br/>
<br/>

#### Availability ####
I'm able to commit up to 40 hours/week to this project. I am also  wrapping up a graduate research project with my advisor's lab this semester. I am unfunded for the summer with my lab and university, but I will be spending some time finalizing and submitting a paper to a conference with a submission deadline of August 20. Most of this work will be completed before the start of Community Bonding in May.<br/>
<br/>
I am traveling from May 24 until June 1 to visit family in Portland, Oregon (UTC-7). I will be available for short meetings and calls at this time if scheduled in advance. I will also be reachable via email. 

####  Biography ####
Hi, my name is Andie Bradley (they/them). I am a graduate student at Easter Michigan University (EMU) finishing a MS in Computer Science. Currently I am working with the Embedded AI Systems Lab at EMU. My research involves analysis of art created using a technique called neural style transfer. One common use of neural style transfer is remixing a photograph with the style and works of famous artists. Examples can be seen on [my website](http://emunix.emich.edu/~abradl26). I also hold an unrelated BA in History from the University of Michigan.
<br/>
<br/>
Previously I was employed at a healthcare IT company called Epic in Madison WI, where I worked as both a software developer and project manager from 2018-2024. This involved mostly working with C# and JavaScript/Typescript. I also developed a number of internal tools for customer system configuration analysis using a proprietary database system, and scripting languages such as Perl and Python. I did development from 2018-2022 and later worked as a project manager until 2024.
<br/>
<br/>
My experience with FreeBSD started in October 2024, when I installed it on a spare desktop computer because I was looking for an environment to practice C and learn more about operating systems. I have been working through course materials in the [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) book. Since then, I have contributed a port of [Halloy](https://halloy.squidowl.org), an IRC client. Examples of my work are available on my [GitHub page](https://github.com/awbradle). I do not have any experience with ncurses or creating a TUI program, and this project will provide me with a good learning opportunity.

##Project Information##

####Project Description####
WiFi configuration in FreeBSD is not as simple as other Unix-like operating systems. Currently the [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/network/#network-wireless) instructs the user to perform configuration by running multiple commands and editing numerous text files. While the average FreeBSD user is more comfortable working solely with the command line, recent efforts such as the Laptop and Desktop Workgroup (LDWG) seek to make running FreeBSD as a desktop operating system more feasible for more users. This project will implement a configuration utility with a terminal user interface (TUI) to make initial WiFi configuration faster and easier. Additionally, users who need to connect to different WiFi networks as they go about will also have a tool they can user to do this.
<br/>
<br/>
I am targeting a TUI for this project because a standard FreeBSD installation lacks installation and configuration of a graphic desktop environment. This project will be written in C and limit itself to a library such as ncurses so that it might potentially be included in the base installation in the future. Finally, I would like to generalize what is developed in this project such that it can be used in a future GUI based WiFi configuration tool.
<br/>
<br/>
Configuration parameters of `/etc/wpa_supplicant.conf` are well documented in `man wpa_supplicant.conf`. This tool should allow for full configuration of all global parameters and network block parameters. Additionally the wpa_supplicant [control interface](https://w1.fi/wpa_supplicant/devel/ctrl_iface_page.html) will allow for this tool to communicate with wpa_supplicant, allowing users to scan for available networks or apply changes to WiFi configuration to the wpa_supplicant service.
<br/>
<br/>
<img style="width:70%;" src="{static}/images/gsoc/FreeBSDwifi.png" alt="Image showing where new wifi tool fits in with wpa_supplicant">
<br/>

####Deliverables####
At a minimum, the project should deliver a fully functioning TUI program, documentation, and port. Additionally the WiFi configuration utility should meet all of necessary guidelines specified in the FreeBSD Developers Handbook.

Midterm Deliverable: 
The new tool should at a minimum be able to display current configuration and available WiFi networks. Ideally the user should also be able to connect to a simple WPA-PSK home WiFi network.

Final Deliverable:
The new tool should additionally allow configuration of a WPA-Enterprise network perhaps found at work or school. Users should be able to reasonably edit and configure saved WiFi networks, add and remove networks, etc. Additionally a man page should be available to fully document the program, along with a quick start guide available somewhere online. Finally a port should be available for users to quickly and easily install this program from a pre-built binary.

####Test Plan####
Hardware testing will be done on a Lenovo Thinkpad T450s and Lenovo IdeaCentre 720. Both of these devices. Both of these devices have WiFi cards compatible with FreeBSD.

Usability testing will be important to a project seeking to make WiFi configuration easier for end users. I hope to solicit feedback from the [Laptop and Desktop Working Group](https://wiki.freebsd.org/LaptopDesktopWorkingGroup). The user stories in the [Laptop Support and Usability project](https://github.com/FreeBSDFoundation/proj-laptop) should also considered, particularly:
- [Automatically connect to known Wi-Fi networks](https://github.com/FreeBSDFoundation/proj-laptop/issues/3)
- [Easy connect to WiFi](https://github.com/FreeBSDFoundation/proj-laptop/issues/4)

####Possible Mentors####
I have been in contact with Getz Mikalsen via IRC and email, and Aymeric Wibo via email.

####Project Schedule####
May 8 - June 1: Community Bonding Time </br>
June 2 - July 14: Midterm Deliverables </br>
July 14: Midterm Evaluations </br>
July 14 - August 25: Final Deliverables </br>
August 25 - September 1: Submit Project</br>
September 1 - September 8: Final Evaluations</br>


####Reach Goal####
A potential reach goal involves using code from this project to create a GUI tool to connect to WiFi networks. I would like to begin this work over the summer and continue it after the end of the project.


 