from model.contact import Contact


def test_delete_first_contact(app):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John"))
    app.contact.delete_first_contact()
