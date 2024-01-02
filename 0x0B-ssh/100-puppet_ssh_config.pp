#!/usr/bin/env bash
# bash script to connect to a ubuntu server RSA with puppet

# Puppet manifest to configure SSH client
class ssh_client_config {

  # Define the SSH client configuration file path
  $ssh_config_path = '/etc/ssh/ssh_config'

  # Ensure the SSH client configuration file is managed
  file { $ssh_config_path:
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
  }

  # Manage the content of the SSH client configuration file
  file_line { 'use_private_key':
    path   => $ssh_config_path,
    line   => '    IdentityFile ~/.ssh/school',
    match  => '^ *IdentityFile.*$',
  }

  file_line { 'refuse_password_auth':
    path   => $ssh_config_path,
    line   => '    PasswordAuthentication no',
    match  => '^ *PasswordAuthentication.*$',
  }
}

