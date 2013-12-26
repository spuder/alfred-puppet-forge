# alfred-puppet-forge-workflow

An alfred workflow that facilitates quick searching of the puppet forge

[puppet forge] (https://forge.puppetlabs.com)  
[alfred] (http://www.alfredapp.com) 

![Screenshot1] (https://raw.github.com/spuder/alfred-puppet-forge/master/img/forge.png)
![Screenshot2] (https://raw.github.com/spuder/alfred-puppet-forge/master/img/forge2.png)  

### Usage

Type 'forge' and the name of the module / user you are looking for


### Special Considerations


The minimum length of a search is 4 characters. This is to prevent delays due to alfred's
constant search feature combined with the forge finding too many results. 

To search for words less than 4 characters, add a trailing space. 

See the following links for further explanation of this limitation. 

[Alfred Fourm](http://www.alfredforum.com/topic/991-anyway-to-delay-script-filter-from-running-ie-wait-until-user-has-stopped-typing-or-at-least-paused/)  
[Alfred Fourm1](http://www.alfredforum.com/topic/3654-passing-an-argument-into-a-python-script/#entry21572)  
[Ask.puppetlabs.com](https://ask.puppetlabs.com/question/4557/limit-results-from-forge-api/)


