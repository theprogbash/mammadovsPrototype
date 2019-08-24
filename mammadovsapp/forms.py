from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'contact-input font-reg'
        self.fields['name'].widget.attrs['tabindex'] = "1"
        self.fields['name'].widget.attrs['placeholder'] = 'Adınızı daxil edin'
        self.fields['email'].widget.attrs['class'] = 'contact-input font-reg'
        self.fields['email'].widget.attrs['placeholder'] = 'Emailinizi daxil edin'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['tabindex'] = "2"
        self.fields['message'].widget.attrs['class'] = 'contact-text font-reg'
        self.fields['message'].widget.attrs['placeholder'] = 'Mesajınız'
        self.fields['message'].widget.attrs['tabindex'] = "4"



