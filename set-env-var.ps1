# PowerShell script to add system-wide environment variables on Windows

# Run this script as an Administrator

# Set email address environment variable
$variableName1 = "EMAIL_ADDRESS"
$variableValue1 = "<your-email-address>"
[System.Environment]::SetEnvironmentVariable($variableName1, $variableValue1, [System.EnvironmentVariableTarget]::Machine)
Write-Host "Environment variable '$variableName1' set successfully."

# Set email password environment variable
$variableName2 = "EMAIL_PASSWORD"
$variableValue2 = "<your-email-password>"
[System.Environment]::SetEnvironmentVariable($variableName2, $variableValue2, [System.EnvironmentVariableTarget]::Machine)
Write-Host "Environment variable '$variableName2' set successfully."


#run it with this <PowerShell -ExecutionPolicy Bypass -File .\set-env-var.ps1>
#if you get an error, run this 
#<Set-ExecutionPolicy RemoteSigned>
#<PowerShell -ExecutionPolicy Bypass -File .\set-env-var.ps1>
#<Set-ExecutionPolicy Restricted>

# To verify the environment variables are set OR to edit or set environment variables manually:
# Search for "Environment Variables" in the Windows search bar and click on "Edit the system environment variables" 
#the bottom box is for system variables
