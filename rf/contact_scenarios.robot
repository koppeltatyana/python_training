*** Settings ***
Library             rf.AddressBook
Library             Collections
Suite Setup         Init Fixtures
Suite Teardown      Destroy Fixtures



*** Test Cases ***
Add new contact
    ${old_list}=            GET CONTACT LIST
    ${contact}=             NEW CONTACT  firstname1  lastname1
    CREATE CONTACT          ${contact}
    ${new_list}=            get contact list
    APPEND TO LIST          ${old_list}  ${contact}
    CONTACT LISTS SHOULD BE EQUAL  ${old_list}  ${new_list}

Delete group
    ${old_list}=            GET CONTACT LIST
    ${contact_for_del}=     GIVE RANDOM CONTACT FROM LIST  ${old_list}
    DELETE CONTACT          ${contact_for_del}
    ${new_list}=            GET contact LIST
    REMOVE VALUES FROM LIST  ${old_list}  ${contact_for_del}
    CONTACT LISTS SHOULD BE EQUAL  ${old_list}  ${new_list}

Modify group
    ${old_list}=            GET CONTACT LIST
    ${contact_for_modify}=  GIVE RANDOM CONTACT FROM LIST  ${old_list}
    ${new_contact}=         NEW CONTACT  new_firstname1  new_lastname1
    MODIFY CONTACT          ${contact_for_modify}   ${new_contact}
    ${new_list}=            GET CONTACT LIST
    REPLACE OLD CONTACT TO NEW CONTACT  ${old_list}  ${contact_for_modify}  ${new_contact}
    CONTACT LISTS SHOULD BE EQUAL  ${old_list}  ${new_list}