if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))  
{  
  $arguments = "& '" +$myinvocation.mycommand.definition + "'"
  Start-Process powershell -Verb runAs -ArgumentList $arguments
  Break
}

## Adding a new local user to Users groups and forcing password change at first logon
$newUserName = Read-Host "New user name: "
New-LocalUser -Name "$newUserName" -NoPassword
Add-LocalGroupMember -Group "Users" -Member "$newUserName"
Set-LocalUser -Name "$newUserName" -PasswordNeverExpires:$false

## Removing a local user
##Remove-LocalUser -Name "$username"

## Mapping a windows share locally
## New-SmbMapping -LocalPath 'X:' -RemotePath '\\nassuporte'

## Installing softwares remotely via windows share
## Invoke-CimMethod -ClassName Win32_Product -MethodName Install -Arguments @{PackageLocation = '\\nassuporte\' }