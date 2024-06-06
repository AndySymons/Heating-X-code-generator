# Heating-X-code-generator DEPRECATED

**HEATING X IS SUPERCEDED by HEATING X2, CALENDAR SWITCH Y2, and ZONE SWITCH Z2** 

**The code generator for all three is Heating XYZ Code Cenerator**

- [Heating X2](https://gist.github.com/AndySymons/3592c942ebeca2d5852f7d0c181edf55)
- [Calendar Switch Y2](https://gist.github.com/AndySymons/869e9a34d84c4ddc03fc762a1fc6d88b)
- [Zone Switch Z2](https://gist.github.com/AndySymons/7e21dacb6cd76921640121d73cc62dba)
- [Heating XYZ Code Cenerator](https://github.com/AndySymons/Heating-XYZ-code-generator)
- The all require the [logging script](https://gist.github.com/AndySymons/105062c71de2badad995618fec0fe1ee) 

The release 1 Code Generator is retained solely for existing users of Heating X (release 1). Upgrade to release 2 is recommended, but is not upward compatible, so requires a reinstall. The two versions can co-exist on one system. Use the code generator corresponding to your Heating X release; they cannot be mixed! 

---

Use Microsoft Mail Merge to create YAML files for all the template sensors and helpers required for a complete home installation of Heating X zones. 
Microsoft Office (WORD and EXCEL) is a prerequisite (sorry I could not find a free package to do this) 

To get started: 
1. Download the ZIP file to a temporary location on a local disk drive. Problems can occur if it is used on a drive that is synchronised to a cloud service, such as iCloud or OneDrive (but you can keep a copy of the ZIP file if you wish). 
2. Unzip it. 
3. In the resulting folder there are detailed instructions in $README on how to use the Code Generator to generate and install all the YAML code you need for even the most conplex installation. 

Basically you enter the details of your installation (zones and thermostats) in the EXCEL file, then use each of the five WORD files to generate the contents of a YAML file. They each generate a whole file except the dashboard card generator, which has to be installed one card at a time.    
