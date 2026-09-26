from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/register")
def register_page():
    return render_template("register.html")


@app.post("/register")
def register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    if not name or not email:
        return jsonify({
            "success": False,
            "message": "Name and email are required."
        }), 400

    return jsonify({
        "success": True,
        "message": f"Welcome, {name}! Registration received.",
        "email": email
    })


@app.get("/api/health")
def health():
    return jsonify({
        "success": True,
        "status": "healthy"
    })


@app.route("/home-planner", methods=["GET", "POST"])
def home_planner():

    # Normal page opening
    if request.method == "GET" and not request.args:
        return render_template("home-planner.html")

    # Get form data
    data = request.values

    budget = data.get("budget", "5000")
    lights = data.get("lights", "5")
    fans = data.get("fans", "4")
    furniture = data.get("furniture", "2")
    dining_tables = data.get("dining_tables", "1")

    rooms = data.getlist("rooms")

    preferences = data.get(
        "preferences",
        "Clean, elegant and functional design."
    )

    # Simple budget calculation
    try:
        budget_value = float(budget)
    except ValueError:
        budget_value = 5000

    furniture_budget = budget_value * 0.40
    lighting_budget = budget_value * 0.15
    kitchen_budget = budget_value * 0.25
    decor_budget = budget_value * 0.10
    reserve_budget = budget_value * 0.10

    recommendation = {
        "budget": budget_value,
        "rooms": rooms,
        "preferences": preferences,
        "furniture_budget": furniture_budget,
        "lighting_budget": lighting_budget,
        "kitchen_budget": kitchen_budget,
        "decor_budget": decor_budget,
        "reserve_budget": reserve_budget,
        "lights": lights,
        "fans": fans,
        "furniture": furniture,
        "dining_tables": dining_tables
    }

    return render_template(
        "recommendations.html",
        recommendation=recommendation
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

