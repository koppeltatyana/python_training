def test_delete_first_group(app):
    # вместо передачи параметров передаем объект класса Group
    app.group.delete_first_group()
