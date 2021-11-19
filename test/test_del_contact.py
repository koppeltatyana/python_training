def test_delete_first_contact(app):
    # вместо передачи параметров передаем объект класса Group
    app.contact.delete_first_contact()
