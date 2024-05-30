from django import forms

class NewRecord(forms.Form):
    name = forms.CharField(max_length=75, label="Ваше имя")
    
    choices = (("Аэробика", "Аэробика"), ("Кроссфит", "Кроссфит"), ("Тренировка для начинающих", "Тренировка для начинающих"),
               ("Тренировка для продвинутых", "Тренировка для продвинутых"), ("Тренировка для похудения", "Тренировка для похудения"),
               ("Йога", "Йога"),)
    title = forms.TypedChoiceField(label="Название тренировки", choices=choices)
    date = forms.DateField(label="Дата занятия", input_formats=['%d/%m/%Y'])
    duration = forms.TypedChoiceField(label="Продолжительность занятия", choices=(("1ч", "1ч"), ("1.5ч", "1.5ч"), 
                                                                                  ("2ч", "2ч"), ("2.5ч", "2.5ч")))