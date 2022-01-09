Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname> and <address>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | middlename  | lastname  | address             |
  | firstname1 | middlename1 | lastname1 | addressasdasdadsasd |
  | firstname2 | middlename2 | lastname2 | asdaasdasdasdasdasd |
