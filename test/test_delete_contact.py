


def test_delete__contact(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_contact()
    app.session.logout()