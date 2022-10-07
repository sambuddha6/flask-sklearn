from app import app
import json
import jsonschema
from jsonschema import validate

predictSchema = {
    "type": "object",
    "properties": {
        "prediction": {"type": "number"}
    },
}

def test_validateJson():
    with app.test_client() as client:
        data = {"CHAS":{"0":0},
                "RM":{"0":6.575},
                "TAX":{"0":296.0},
                "PTRATIO":{"0":15.3},
                "B":{"0":396.9},
                "LSTAT":{"0":4.98}
                }

        response = client.post(
            "/predict",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )

        try:
            validate(instance=data, schema=predictSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

def test_predict():
    with app.test_client() as client:
        inputdata = {"CHAS":{"0":0},
                "RM":{"0":6.575},
                "TAX":{"0":296.0},
                "PTRATIO":{"0":15.3},
                "B":{"0":396.9},
                "LSTAT":{"0":4.98}
                }

        response = client.post(
            "/predict",
            data=json.dumps(inputdata),
            headers={"Content-Type": "application/json"},
        )

        if response.data == { "prediction": [ 20.869782939832444 ] }:
            return True
        return False