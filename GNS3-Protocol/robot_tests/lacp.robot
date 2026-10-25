*** Settings ***
Documentation       Verify LACP port-channel status, peer connectivity, and ARP entries.
Library             RouterConnectionLibrary.py    WITH NAME    RouterConnections
Library             LacpLibrary.py
Suite Setup         RouterConnections.Connect To Routers
Suite Teardown      RouterConnections.Disconnect From Routers

*** Test Cases ***
R1 Port Channel Is Up
    Verify Port Channel Is Up    R1

R2 Port Channel Is Up
    Verify Port Channel Is Up    R2

R1 Can Ping R2
    Verify Peer Ping    R1

R2 Can Ping R1
    Verify Peer Ping    R2

R1 Has R2 ARP Entry
    Verify Peer ARP Entry    R1

R2 Has R1 ARP Entry
    Verify Peer ARP Entry    R2
