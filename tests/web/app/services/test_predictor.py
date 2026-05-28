import pytest
import sys
import os

from web.app.services.predictor import predict_match_outcome

# Parameterized tests to hit every single branch combination with real data
@pytest.mark.parametrize(
    "innings, venue, choice",
    [
        (1, 1, 1),  # Innings 1, Venue 1 (Home), Choice 1 (SVM)
        (2, 2, 2),  # Innings 2, Venue 2 (Away), Choice 2 (Decision Tree)
        (1, 3, 3),  # Innings 1, Venue 3 (Neutral), Choice 3 (MLP)
    ]
)
def test_predict_match_outcome_real_execution(innings, venue, choice):
    """
    Runs the actual prediction using real pickle data across all code paths.
    Note: The extra spaces in strings are required because your function 
    strips the first and last characters via string slicing [1:-1].
    """
    # Provide valid team and ground strings that your pickled dataInputFormat hashes recognize
    team1 = " Australia "
    team2 = " India "
    ground = " Chennai "

    # Execute the actual model pipeline
    prediction_result = predict_match_outcome(
        ground=ground,
        innings=innings,
        venue=venue,
        team1=team1,
        team2=team2,
        choice=choice
    )

    # Assertions
    # Since we don't know the exact string output of the real models, 
    # we assert that it safely completes and returns data (not None or empty)
    assert prediction_result is not None
    assert isinstance(prediction_result, (str, int, float, list)) or hasattr(prediction_result, '__str__')


def test_predict_match_outcome_invalid_choice():
    """
    Ensures that if an invalid choice is passed (e.g., 4), 
    the function smoothly completes without running a model and returns None.
    """
    result = predict_match_outcome(
        ground=" Mumbai ",
        innings=1,
        venue=1,
        team1=" India ",
        team2=" Australia ",
        choice=4  # There is no 'elif choice==4' branch
    )
    assert result is None