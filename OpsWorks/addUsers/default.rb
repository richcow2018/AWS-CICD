# recipes/default.rb
user 'new_employee' do
  comment 'New Employee'
  shell '/bin/bash'
  home '/home/new_employee'
  manage_home true
  action :create
end

directory '/home/new_employee/.ssh' do
  owner 'new_employee'
  group 'new_employee'
  mode '0700'
  action :create
end

file '/home/new_employee/.ssh/authorized_keys' do
  owner 'new_employee'
  group 'new_employee'
  mode '0600'
  content 'ssh-rsa AAAAB3... new_employee_key'
  action :create
end
