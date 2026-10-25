# LACP Robot Framework tests

This suite is separate from the existing `lacp.py` pytest tests; both can be
kept and run independently. `RouterConnectionLibrary.py` handles router
connections, and `LacpLibrary.py` contains the LACP checks.

From the `GNS3-Protocol` folder, install the suite dependencies and run:

```powershell
python -m pip install -r .\robot_tests\requirements.txt
python -m robot --outputdir .\robot_tests\results .\robot_tests\lacp.robot
```

The router lab must be running and reachable by hostname and port:
`localhost:5004` (R1) and `localhost:5005` (R2). The interface IP addresses
are only used to check LACP and peer network traffic, not to open the Telnet
connections. Robot Framework writes `output.xml`, `log.html`, and `report.html`
to the results folder.

To check router connections independently, without running the LACP tests:

```powershell
python -m robot --outputdir .\robot_tests\results .\robot_tests\connectivity.robot
```

Each router has its own test, so a connection problem with one router does not
prevent the other router's connectivity test from running.
