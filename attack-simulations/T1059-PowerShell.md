# T1059 - PowerShell

## Objective
Detect PowerShell execution.

## Command

Invoke-AtomicTest T1059

## Detection

index=wineventlog powershell.exe

## Result

Successfully detected in Splunk.
