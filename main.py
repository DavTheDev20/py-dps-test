import traceback
from flask import Flask, request, render_template
from database_utils import db, Deal, get_deals, add_deal, delete_deal
from peewee import IntegrityError
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db.connect()
db.create_tables([Deal])


# API Routes


@app.route('/api/deals', methods=["GET", "POST"])
def api_deals():
    if request.method == "GET":
        deals = get_deals()
        return {"success": True, "deals": deals}
    elif request.method == "POST":
        data = request.json
        if not data["companyName"] or not data["relationshipManager"] or not data["dealAmount"]:
            return {
                "success": False,
                "error": "Please include companyName, relationshipManager, and dealAmount in request json body."
            }, 400
        try:
            new_deal = add_deal(
                data["companyName"], data["relationshipManager"], data["dealAmount"])
            return {"success": True, "newDealId": new_deal.id}, 200
        except IntegrityError:
            traceback.print_exc()
            return {"success": False, "error": traceback.format_exc()}, 400


@app.route('/api/deals/delete/<deal_id>', methods=["DELETE"])
def delete_deal_api(deal_id):
    try:
        res = delete_deal(deal_id)
        return {"success": True, "result": res}, 200
    except:
        return {"success": False, "error": traceback.format_exc()}, 400


# UI Routes


@app.route('/')
def home():
    deals = get_deals()

    deals_total = 0

    for deal in deals:
        deals_total += deal["dealAmount"]

    return render_template("index.html", deals=deals, deals_total=deals_total)


@app.route('/create')
def create():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
