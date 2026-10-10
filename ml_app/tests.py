from unittest.mock import Mock, patch

from django.test import TestCase

from .forms import TipPredictionForm


class TipPredictionFormTests(TestCase):
    def test_encodes_inputs_in_model_feature_order(self):
        form = TipPredictionForm(
            {
                "total_bill": "24.50",
                "sex": "Male",
                "smoker": "No",
                "day": "Sat",
                "time": "Dinner",
                "size": "3",
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.model_features(), [24.5, 1, 0, 1, 0, 3])

    def test_rejects_missing_and_out_of_range_values(self):
        form = TipPredictionForm(
            {
                "total_bill": "-1",
                "sex": "Unknown",
                "smoker": "No",
                "day": "Sat",
                "time": "Dinner",
                "size": "0",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("total_bill", form.errors)
        self.assertIn("sex", form.errors)
        self.assertIn("size", form.errors)


class TipPredictionViewTests(TestCase):
    def test_home_links_to_how_it_works_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/how-it-works/"')

    def test_how_it_works_page_links_back_to_estimator(self):
        response = self.client.get("/how-it-works/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How Tipwise works")
        self.assertContains(response, 'href="/#estimate"')

    @patch("ml_app.views._load_model")
    def test_home_renders_prediction_using_six_named_features(self, load_model):
        model = Mock()
        model.predict.return_value = [4.25]
        load_model.return_value = model

        response = self.client.post(
            "/",
            {
                "total_bill": "24.50",
                "sex": "Female",
                "smoker": "Yes",
                "day": "Thur",
                "time": "Lunch",
                "size": "2",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "$4.25")
        prediction_input = model.predict.call_args.args[0]
        self.assertEqual(
            list(prediction_input.columns),
            ["total_bill", "sex", "smoker", "day", "time", "size"],
        )
        self.assertEqual(prediction_input.iloc[0].tolist(), [24.5, 0, 1, 3, 1, 2])

    def test_home_displays_validation_errors_without_predicting(self):
        response = self.client.post("/", {"total_bill": "20"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
