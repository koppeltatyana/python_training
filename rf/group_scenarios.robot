*** Settings ***
Library             rf.AddressBook
Library             Collections
Suite Setup         Init Fixtures
Suite Teardown      Destroy Fixtures



*** Test Cases ***
Add new group
    ${old_list}=    GET GROUP LIST
    ${group}=       NEW GROUP  name1  header1  footer1
    CREATE GROUP    ${group}
    ${new_list}=    GET GROUP LIST
    APPEND TO LIST  ${old_list}  ${group}
    GROUP LISTS SHOULD BE EQUAL  ${old_list}  ${new_list}

Delete group
    ${old_list}=    GET GROUP LIST
    ${group_for_del}=  give random group from list  ${old_list}
    DELETE GROUP    ${group_for_del}
    ${new_list}=    GET GROUP LIST
    REMOVE VALUES FROM LIST  ${old_list}  ${group_for_del}
    GROUP LISTS SHOULD BE EQUAL  ${old_list}  ${new_list}

Modify group
    ${old_list}=    GET GROUP LIST
    ${group_for_modify}=  give random group from list  ${old_list}
    ${new_group}=   NEW GROUP  name1  header1  footer1
    MODIFY GROUP    ${group_for_modify}  ${new_group}
    ${new_list}=    GET GROUP LIST
    replace old group to new group  ${old_list}  ${group_for_modify}  ${new_group}
    GROUP LISTS SHOULD BE EQUAL  ${old_list}  ${new_list}