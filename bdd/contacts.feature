Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname> and <address>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact

  Examples:
  | firstname  | middlename  | lastname  | address             |
  | firstname1 | middlename1 | lastname1 | addressasdasdadsasd |
  | firstname2 | middlename2 | lastname2 | asdaasdasdasdasdasd |


Scenario Outline: Delete some contact
  Given non empty contact list
  Given a random contact from non empty contact list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without deleted contact


Scenario Outline: Modify some contact
  Given non empty contact list
  Given a random contact from non empty contact list
  Given a new contact with <new_firstname>, <new_middlename>, <new_lastname> and <new_address>
  When I modify the contact from the list
  Then the new contact list is equal to the old contact list with modify contact

  Examples:
  | new_firstname  | new_middlename  | new_lastname  | new_address             |
  | new_firstname1 | new_middlename1 | new_lastname1 | new_address1212jhgfsfgd |