*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pelle  pelle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  pelle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  pe  pelle123
    Output Should Contain  Virheellinen

Register With Valid Username And Too Short Password
    Input Credentials  pelle  pelle12
    Output Should Contain  Virheellinen

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pelle  pellePel
    Output Should Contain  Virheellinen

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command