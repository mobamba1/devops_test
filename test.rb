package 'httpd' do
    action :install
  end
  
  file '/etc/motd' do
    owner 'root'
    group 'root'
    mode '0644'
    content 'Hello world'
  end
  
  service 'httpd' do
    action [:enable, :start]
  end
  
  user 'john.delacruz' do
    comment 'New User john dela cruz'
    home '/home/john.delacruz'
    shell '/bin/bash'
    manage_home true
  end
  