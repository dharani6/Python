*** Settings ***
Documentation       Check that Robot Framework can connect to each router.
Library             RouterConnectionLibrary.py

*** Test Cases ***
Can Connect To R1
    Verify Router Connectivity    R1

Can Connect To R2
    Verify Router Connectivity    R2
