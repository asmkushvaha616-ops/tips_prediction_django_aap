from django import forms


class TipPredictionForm(forms.Form):
    SEX_CODES = {"Female": 0, "Male": 1}
    SMOKER_CODES = {"No": 0, "Yes": 1}
    DAY_CODES = {"Fri": 0, "Sat": 1, "Sun": 2, "Thur": 3}
    TIME_CODES = {"Dinner": 0, "Lunch": 1}

    total_bill = forms.FloatField(
        label="Total bill",
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "e.g. 32.50", "step": "0.01"}
        ),
    )
    sex = forms.ChoiceField(
        label="Server's gender",
        choices=[("", "Choose an option"), ("Female", "Female"), ("Male", "Male")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    smoker = forms.ChoiceField(
        label="Smoker at the table?",
        choices=[("", "Choose an option"), ("No", "No"), ("Yes", "Yes")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    day = forms.ChoiceField(
        label="Day of the week",
        choices=[
            ("", "Choose an option"),
            ("Thur", "Thursday"),
            ("Fri", "Friday"),
            ("Sat", "Saturday"),
            ("Sun", "Sunday"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    time = forms.ChoiceField(
        label="Meal",
        choices=[("", "Choose an option"), ("Lunch", "Lunch"), ("Dinner", "Dinner")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    size = forms.IntegerField(
        label="Party size",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "e.g. 2", "step": "1"}
        ),
    )

    def model_features(self) -> list[float | int]:
        """Return the six features in the order used to train the XGBoost model."""
        if not self.is_valid():
            raise ValueError("Model features are available only for a valid form.")

        cleaned_data = self.cleaned_data
        return [
            cleaned_data["total_bill"],
            self.SEX_CODES[cleaned_data["sex"]],
            self.SMOKER_CODES[cleaned_data["smoker"]],
            self.DAY_CODES[cleaned_data["day"]],
            self.TIME_CODES[cleaned_data["time"]],
            cleaned_data["size"],
        ]
    