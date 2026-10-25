*** Settings ***
Library    Process

*** Test Cases ***
Show ARP Table
    ${result}=    Run Process    powershell    -NoProfile    -Command    arp -a    shell=False
    Log To Console    ${result.stdout}
    Should Be Equal As Integers    ${result.rc}    0

Show IP Configuration
    ${result}=    Run Process    powershell    -NoProfile    -Command    ipconfig    shell=False
    Log To Console  ${result.stdout}
    Should Be Equal As Integers     ${result.rc}   0
