# arch-updatechecker-blocklet
i3blocks blocklet that checks for updates on Arch Linux

Works best if you periodically run a pacman -Sy to make sure the package databases are up to date. Otherwise, it may not catch updates due to old data. The way I have it set up is through a systemd timer running every 15 minutes. An example of the timer is pasted below. Cron or other timers work fine as well. 

[Unit]                                                                                                               
Description=sync pacman metadata                                                                                     
                                                                                                                     
[Timer]                                                                                                              
OnBootSec=0                                                                                                          
OnCalendar=*:0/15                                                                                                    
Persistent=true                                                                                                      
Unit=pacman-sync.service                                                                                             
                                                                                                                     
[Install]                                                                                                            
WantedBy=timers.target
