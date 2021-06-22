from django import forms


class GriForm(forms.Form):
    OPTIONS = (
("non_renewable_materials_used","non_renewable_materials_used"),
("renewable_materials_used","renewable_materials_used"),
("recycled_percentage","recycled_percentage"),
("fuel_consumption_with_non_renewable_sources","fuel_consumption_with_non_renewable_sources"),
("fuel_consumption_with_renewable_sources","fuel_consumption_with_renewable_sources"),
("surface_water_withdrawal_megaliters","surface_water_withdrawal_megaliters"),
("ground_water_withdrawal_megaliters","ground_water_withdrawal_megaliters"),
("surface_water_withdrawal_with_watre_stress","surface_water_withdrawal_with_watre_stress"),
("ground_water_withdrawal_with_watre_stress","ground_water_withdrawal_with_watre_stress")
    )
    QueryOptions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'checked' : 'checked'}),
    choices=OPTIONS)