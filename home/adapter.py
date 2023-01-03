from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.codice_fiscale = data.get('codice_fiscale')
        user.gender = data.get('gender')
        user.dob = data.get('dob')
        user.region_of_birth = data.get('region_of_birth')
        user.country = data.get('country')
        user.phone_no = data.get('phone_no')
        user.save()
        return user