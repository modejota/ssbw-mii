from django import forms

class FormularioLibro(forms.Form):
    title = forms.CharField(max_length=120, required=True, label="Título")
    author = forms.CharField(max_length=120, required=True, label="Autor")
    genre = forms.CharField(max_length=120, required=True, label="Género")
    description = forms.CharField(max_length=240, required=True, label="Descripción")
    isbn = forms.CharField(max_length=13, required=True, label="ISBN")
    # image = forms.CharField(max_length=240, required=True, label="Imagen")
    published = forms.DateTimeField(required=False, label="Fecha de publicación",
                                    widget=forms.DateTimeInput(
                                        attrs={'class': 'form-control datetimepicker-input'},
                                        format='%Y-%m-%d'))
    publisher = forms.CharField(max_length=120, required=True, label="Editorial")