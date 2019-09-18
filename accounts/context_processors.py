def include_login_form(request):
    """Include Login modal form across site"""
    from accounts.forms import UserLoginForm
    form = UserLoginForm()
    return {'login_form': form}