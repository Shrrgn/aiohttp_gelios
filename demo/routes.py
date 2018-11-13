from demo.views import index, users, units


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/get_users', users)
    app.router.add_get('/get_units', units)
