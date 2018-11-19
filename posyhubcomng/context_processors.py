def active_menu(request):
    path = request.path.split("/")
    active = None

    if 'about' in path:
        active = "about"
    elif 'contact-us' in path:
        active = 'contact'
    elif 'services' in path:
        active = 'services'
    elif 'blog' in path or 'comments' in path:
        active = 'blog'
    else:
        active = 'home'
    return {'active': active}