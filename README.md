# arch-updatechecker-blocklet
i3blocks blocklet that checks for updates on Arch Linux

Works best if you periodically run a pacman -Sy to make sure the package databases are up to date. Otherwise, it may not catch updates due to old data. The way I have it set up is through a systemd timer running every 15 minutes. An example of the timer is pasted below. Cron or other timers work fine as well. Alternatively, you can also add the pacman -Sy command to the updatechecker script itself, though you have to keep in mind two important things. First, it has to run as root. Second,  you want to make sure the output of the command isn't sent to stdout, otherwise it will show up in your i3blocks bar. 

[Unit]                                                                                                               
Description=sync pacman metadata                                                                                     
                                                                                                                    
[Timer]                                                                                                              
OnBootSec=0                                                                                                          
OnCalendar=*:0/15                                                                                                    
Persistent=true                                                                                                      
Unit=pacman-sync.service                                                                                             
                                                                                                                     
[Install]                                                                                                            
WantedBy=timers.target
