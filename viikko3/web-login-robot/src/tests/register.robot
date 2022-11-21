*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application and Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Fail With Message  Virheellinen

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle45
    Set Password Confirmation  kalle45
    Submit Credentials
    Register Should Fail With Message  Virheellinen


Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle4567
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Fail With Message  Virheellinen

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  kalle
    Set Password  kalle456
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle45
    Set Password Confirmation  kalle45
    Submit Credentials
    Register Should Fail With Message  Virheellinen
    Go To Login Page
    Set Username  kalle
    Set Password  kalle45
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application and Go To Register Page
    Reset Application
    Go To Register Page
