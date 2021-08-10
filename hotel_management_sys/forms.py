from django import forms


class AvailabilityForm(forms.Form):
    # make a package
    ROOM_TYPES = (
        ('SIN', 'Single'),
        ('DOU', 'Double'),
        ('TRI', 'Triple'),
        ('TWI', 'Twin')
    )
    room_type = forms.ChoiceField(choices=ROOM_TYPES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])