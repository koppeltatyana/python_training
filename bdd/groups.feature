Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |

Scenario Outline: Delete some group
  Given non empty group list
  Given a random group from non empty group list
  When I delete the group from the list
  Then the new group list is equal to the old list without deleted group


Scenario Outline: Modify some group
  Given non empty group list
  Given a random group from non empty group list
  Given a new group with <new_name>, <new_header> and <new_footer>
  When I modify the group from the list
  Then the new group list is equal to the old list with modify group

  Examples:
  | new_name  | new_header  | new_footer  |
  | new_name1 | new_header1 | new_footer1 |