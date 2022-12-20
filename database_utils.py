from peewee import *
import traceback

db = SqliteDatabase('./database/main.db')


class Deal(Model):
    id = AutoField(primary_key=True)
    company_name = CharField()
    relationship_manager = CharField()
    deal_amount = FloatField()

    class Meta:
        database = db


def get_deals():
    deals = [
        {
            "id": deal.id,
            "companyName": deal.company_name,
            "relationshipManager": deal.relationship_manager,
            "dealAmount": deal.deal_amount
        } for deal in Deal.select()]
    return deals


def add_deal(company_name, relationship_manager, deal_amount):
    new_deal = Deal(
        company_name=company_name,
        relationship_manager=relationship_manager.upper(),
        deal_amount=deal_amount
    )
    new_deal.save()
    return new_deal


def delete_deal(deal_id: int):
    res = Deal.delete().where(Deal.id == deal_id).execute()
    return res
