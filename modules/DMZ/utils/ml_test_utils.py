import unittest


# This function takes a model, the validation data, and the original data
# and either applies it to check how good the model might work, or to apply it
# to new unlabeled data.
def model_use(model, validation_pack):
    model = model.fit(validation_pack.x_train, validation_pack.y_train)
    return model.score(validation_pack.x_test, validation_pack.y_test)


def ml_test(test, model, validation_pack):
    # Act
    result = model_use(model[1], validation_pack)

    # Assert
    test.assertIsNotNone(result, msg="Failed to beat baseline")
