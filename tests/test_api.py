from playwright.sync_api import  expect



def test_consultar_usuario(api_context):
    response = api_context.get("/users/1")

    expect(response).to_be_ok()
    assert response.status == 200

    body = response.json()

    assert body["id"] == 1
    assert "email" in body
    assert isinstance(body["email"], str)
    assert body["email"] != ""
    assert "@" in body["email"]

def test_crear_usuario(api_context):
    response = api_context.get("/users/1")

    request = {
        "name": "gisel",
        "email": "gisel@test.com"
    }

    response = api_context.post("/users", data=request)

    assert response.status == 201

    body = response.json()

    assert body["name"] == request["name"]
    assert body["email"] == request["email"]

    assert "id" in body
    assert isinstance(body["id"], int)
  