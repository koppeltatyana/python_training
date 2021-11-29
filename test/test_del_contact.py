from model.contact import Contact


def test_delete_first_contact(app):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="John"))
    old_groups = app.group.get_group_list()
    app.contact.delete_first_contact()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
